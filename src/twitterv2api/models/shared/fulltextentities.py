import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import cashtagentity as shared_cashtagentity
from ..shared import hashtagentity as shared_hashtagentity
from ..shared import mentionentity as shared_mentionentity
from ..shared import urlentity as shared_urlentity


@dataclass_json
@dataclasses.dataclass
class FullTextEntitiesAnnotations:
    r"""FullTextEntitiesAnnotations
    Represents the data for the annotation.
    """
    
    end: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('end') }})
    start: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('start') }})
    normalized_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('normalized_text') }})
    probability: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('probability') }})
    type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class FullTextEntities:
    annotations: Optional[list[FullTextEntitiesAnnotations]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('annotations') }})
    cashtags: Optional[list[shared_cashtagentity.CashtagEntity]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('cashtags') }})
    hashtags: Optional[list[shared_hashtagentity.HashtagEntity]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('hashtags') }})
    mentions: Optional[list[shared_mentionentity.MentionEntity]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('mentions') }})
    urls: Optional[list[shared_urlentity.URLEntity]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('urls') }})
    
