from typing import List

import torch
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import pytorch_cos_sim

from src.app.schemas.grade_result import GradeResult


class GradeService:
    _model = None

    def __init__(self):
        if GradeService._model is None:
            GradeService._model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
        self.model = GradeService._model
        self.top_k = 5
        self.INVALID_SCORE = -1

    def grade(self, user_answer: str, desirable_answers: List[str]) -> GradeResult:
        if not desirable_answers:
            return GradeResult(best_score=self.INVALID_SCORE, best_answer="no desirable answers provided")

        corpus_embeddings = self.model.encode(desirable_answers, convert_to_tensor=True)
        query_embeddings = self.model.encode([user_answer], convert_to_tensor=True)

        cos_scores = pytorch_cos_sim(query_embeddings, corpus_embeddings)
        cos_scores = cos_scores.squeeze(0)

        top_k = min(self.top_k, len(desirable_answers))
        values, indices = torch.topk(cos_scores, k=top_k)

        best_score = float(values[0].item())
        best_index = int(indices[0].item())

        return GradeResult(
            best_score=int(best_score * 100),
            best_answer=desirable_answers[best_index],
        )
