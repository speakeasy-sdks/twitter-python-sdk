import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import problem as shared_problem


@dataclass_json
@dataclasses.dataclass
class CreateDmEventResponseData:
    dm_conversation_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dm_conversation_id') }})
    dm_event_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dm_event_id') }})
    

@dataclass_json
@dataclasses.dataclass
class CreateDmEventResponse:
    data: Optional[CreateDmEventResponseData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    errors: Optional[list[shared_problem.Problem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors') }})
    
