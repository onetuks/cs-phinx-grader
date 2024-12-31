import logging
from datetime import datetime

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from app.common.consts import MODEL_NAME, SYSTEM_ROLE_CONTENT, FORMAT_CONTENT, \
  MAX_NEW_TOKENS, INSTRUCTION_CONTENT


class DescriptiveAnswerGrader:
  def __init__(self):
    self.model = None
    self.tokenizer = None
    self.terminators = None

  def initialize(self, model_id: str = MODEL_NAME):
    self.tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)
    self.model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    self.terminators = [
      self.tokenizer.convert_tokens_to_ids("<|end_of_text|>"),
      self.tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

  def generate_evaluation(self, question: str, answer: str) -> str:
    logging.info(f"evaluate_answer start: {datetime.now()}")

    if not question.strip():
      raise ValueError("Blank question")
    if not answer.strip():
      raise ValueError("Blank answer")

    messages = [
      {"role": "system", "content": SYSTEM_ROLE_CONTENT},
      {"role": "user", "content": FORMAT_CONTENT},
      {"role": "user", "content": INSTRUCTION_CONTENT},
      {"role": "user", "content": f"주어진 문제: {question}"},
      {"role": "user", "content": f"제시된 답안: {answer}"}
    ]

    input_ids = (self.tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt",
    )).to(self.model.device)

    outputs = self.model.generate(
        input_ids,
        max_new_tokens=MAX_NEW_TOKENS,
        eos_token_id=self.terminators,
        do_sample=True,
        temperature=0.2,
        top_p=0.8
    )

    logging.info(f"evaluate_answer end: {datetime.now()}")

    return self.tokenizer.decode(outputs[0][input_ids.shape[-1]:])

  def evaluate_answer(self, question: str, answer: str) -> str:
    evaluation = self.generate_evaluation(question, answer).replace("<|eot_id|>", "")
    return evaluation
