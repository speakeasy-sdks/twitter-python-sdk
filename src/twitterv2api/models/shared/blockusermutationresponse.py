import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import problem as shared_problem


@dataclass_json
@dataclasses.dataclass
class BlockUserMutationResponseData:
    blocking: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('blocking') }})
    

@dataclass_json
@dataclasses.dataclass
class BlockUserMutationResponse:
    data: Optional[BlockUserMutationResponseData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    errors: Optional[list[shared_problem.Problem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors') }})
    
