from typing import List

import torch
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import pytorch_cos_sim

from app.schemas.grade_result import GradeResult


class GradeService:
    def __init__(self):
        self.model = SentenceTransformer("distiluse-base-multilingual-cased-v1")
        self.top_k = 5

    def grade(self, user_answer: str, desirable_answers: List[str]) -> GradeResult:
        if not desirable_answers:
            return GradeResult(score=0, comment="no desirable answers provided")

        corpus_embeddings = self.model.encode(desirable_answers, convert_to_tensor=True)
        query_embeddings = self.model.encode([user_answer], convert_to_tensor=True)

        cos_scores = pytorch_cos_sim(query_embeddings, corpus_embeddings)
        cos_scores = cos_scores.squeeze(0)

        top_k = min(self.top_k, len(desirable_answers))
        values, indices = torch.topk(cos_scores, k=top_k)

        best_score = float(values[0].item())
        best_index = int(indices[0].item())
        top_matches = [(desirable_answers[int(i.item())], float(v.item())) for v, i in zip(values, indices)]

        return GradeResult(
            score=int(best_score * 100),
            comment=desirable_answers[best_index],
        )
