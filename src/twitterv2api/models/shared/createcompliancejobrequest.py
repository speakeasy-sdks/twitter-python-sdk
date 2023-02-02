import dataclasses
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from twitterv2api import utils

class CreateComplianceJobRequestTypeEnum(str, Enum):
    TWEETS = "tweets"
    USERS = "users"


@dataclass_json
@dataclasses.dataclass
class CreateComplianceJobRequest:
    r"""CreateComplianceJobRequest
    A request to create a new batch compliance job.
    """
    
    type: CreateComplianceJobRequestTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    resumable: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('resumable') }})
    
