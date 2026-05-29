from dataclasses import dataclass

from .types import JsonDict


@dataclass(frozen=True)
class SuggestedCorrection:
    message_to_firefighter: str
    suggested_reason_rewrite: str | None = None

    def to_dict(self) -> JsonDict:
        return {
            "message_to_firefighter": self.message_to_firefighter,
            "suggested_reason_rewrite": self.suggested_reason_rewrite,
        }
