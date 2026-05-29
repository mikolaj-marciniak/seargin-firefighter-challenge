from dataclasses import dataclass, field
from typing import Any

from .types import JsonDict


@dataclass(frozen=True)
class Session:
    session_id: str
    firefighter_id: str
    firefighter_user: str
    controller: str
    system: str
    client: str
    start_time: str
    end_time: str
    reason_code: str
    ticket_reference: str
    transaction_log: list[JsonDict] = field(default_factory=list)
    change_log: list[JsonDict] = field(default_factory=list)
    system_log: list[JsonDict] = field(default_factory=list)
    os_command_log: list[JsonDict] = field(default_factory=list)
    ticket_requester: str | None = None
    alert_source: str | None = None
    raw: JsonDict = field(default_factory=dict, repr=False)

    @classmethod
    def from_dict(cls, data: JsonDict) -> "Session":
        return cls(
            session_id=str(data.get("session_id", "")),
            firefighter_id=str(data.get("firefighter_id", "")),
            firefighter_user=str(data.get("firefighter_user", "")),
            controller=str(data.get("controller", "")),
            system=str(data.get("system", "")),
            client=str(data.get("client", "")),
            start_time=str(data.get("start_time", "")),
            end_time=str(data.get("end_time", "")),
            reason_code=str(data.get("reason_code", "")),
            ticket_reference=str(data.get("ticket_reference", "")),
            transaction_log=list(data.get("transaction_log") or []),
            change_log=list(data.get("change_log") or []),
            system_log=list(data.get("system_log") or []),
            os_command_log=list(data.get("os_command_log") or []),
            ticket_requester=_optional_str(data.get("ticket_requester")),
            alert_source=_optional_str(data.get("alert_source")),
            raw=data,
        )

    @property
    def tcodes(self) -> set[str]:
        return {
            str(entry.get("tcode", "")).upper()
            for entry in self.transaction_log
            if entry.get("tcode")
        }


def _optional_str(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None
