import dataclasses
from typing import Any
from enum import Enum
from dataclasses_json import dataclass_json
from twitterv2api import utils

class CreateDmConversationRequestConversationTypeEnum(str, Enum):
    GROUP = "Group"


@dataclass_json
@dataclasses.dataclass
class CreateDmConversationRequest:
    conversation_type: CreateDmConversationRequestConversationTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('conversation_type') }})
    message: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    participant_ids: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('participant_ids') }})
    
