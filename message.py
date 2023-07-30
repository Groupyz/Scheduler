import datetime
from dataclasses import dataclass, fields
from log.log_handler import log


@dataclass
class Message:
    user_id: str
    group_ids: list
    message_data: str
    time_to_send: datetime.datetime

    @log
    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if not value:
                raise ValueError(f"{field.name.replace('_', ' ').title()} is required.")
            if field.name == "time_to_send" and not isinstance(
                value, datetime.datetime
            ):
                raise ValueError("Time to send is not in correct datetime format.")
