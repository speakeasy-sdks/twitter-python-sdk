import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import tweet as shared_tweet
from ..shared import problem as shared_problem
from ..shared import expansions as shared_expansions


@dataclass_json
@dataclasses.dataclass
class Get2TweetsSearchAllResponseMeta:
    newest_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('newest_id') }})
    next_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next_token') }})
    oldest_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('oldest_id') }})
    result_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('result_count') }})
    

@dataclass_json
@dataclasses.dataclass
class Get2TweetsSearchAllResponse:
    data: Optional[list[shared_tweet.Tweet]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    errors: Optional[list[shared_problem.Problem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors') }})
    includes: Optional[shared_expansions.Expansions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('includes') }})
    meta: Optional[Get2TweetsSearchAllResponseMeta] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta') }})
    
