from dataclasses import dataclass

from .types import JsonDict, Severity


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: Severity
    location: str
    description: str
    evidence: str

    def to_dict(self) -> JsonDict:
        return {
            "rule_id": self.rule_id,
            "severity": self.severity,
            "location": self.location,
            "description": self.description,
            "evidence": self.evidence,
        }
