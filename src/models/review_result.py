from dataclasses import dataclass, field

from .correction import SuggestedCorrection
from .finding import Finding
from .types import JsonDict, Verdict


@dataclass(frozen=True)
class ReviewResult:
    session_id: str
    verdict: Verdict
    confidence: float
    findings: list[Finding] = field(default_factory=list)
    suggested_correction: SuggestedCorrection | None = None

    def to_dict(self) -> JsonDict:
        return {
            "session_id": self.session_id,
            "verdict": self.verdict,
            "confidence": self.confidence,
            "findings": [finding.to_dict() for finding in self.findings],
            "suggested_correction": (
                self.suggested_correction.to_dict()
                if self.suggested_correction is not None
                else None
            ),
        }
