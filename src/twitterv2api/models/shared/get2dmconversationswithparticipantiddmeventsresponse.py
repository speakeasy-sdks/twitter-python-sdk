import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import dmevent as shared_dmevent
from ..shared import problem as shared_problem
from ..shared import expansions as shared_expansions


@dataclass_json
@dataclasses.dataclass
class Get2DmConversationsWithParticipantIDDmEventsResponseMeta:
    next_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next_token') }})
    previous_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous_token') }})
    result_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('result_count') }})
    

@dataclass_json
@dataclasses.dataclass
class Get2DmConversationsWithParticipantIDDmEventsResponse:
    data: Optional[list[shared_dmevent.DmEvent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    errors: Optional[list[shared_problem.Problem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors') }})
    includes: Optional[shared_expansions.Expansions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('includes') }})
    meta: Optional[Get2DmConversationsWithParticipantIDDmEventsResponseMeta] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta') }})
    
