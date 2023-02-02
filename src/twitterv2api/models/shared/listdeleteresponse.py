import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import problem as shared_problem


@dataclass_json
@dataclasses.dataclass
class ListDeleteResponseData:
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted') }})
    

@dataclass_json
@dataclasses.dataclass
class ListDeleteResponse:
    data: Optional[ListDeleteResponseData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    errors: Optional[list[shared_problem.Problem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors') }})
    
