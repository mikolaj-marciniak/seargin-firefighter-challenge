from typing import Any, Literal, TypeAlias


Verdict = Literal["PASS", "REJECT", "NEEDS_CORRECTION"]
Severity = Literal["low", "medium", "high", "critical"]
JsonDict: TypeAlias = dict[str, Any]
