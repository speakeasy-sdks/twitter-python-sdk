import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import space as shared_space
from ..shared import problem as shared_problem
from ..shared import expansions as shared_expansions


@dataclass_json
@dataclasses.dataclass
class Get2SpacesIDResponse:
    data: Optional[shared_space.Space] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    errors: Optional[list[shared_problem.Problem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors') }})
    includes: Optional[shared_expansions.Expansions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('includes') }})
    
