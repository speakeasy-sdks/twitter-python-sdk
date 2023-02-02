import dataclasses
from enum import Enum

class ComplianceJobStatusEnum(str, Enum):
    CREATED = "created"
    IN_PROGRESS = "in_progress"
    FAILED = "failed"
    COMPLETE = "complete"
    EXPIRED = "expired"

