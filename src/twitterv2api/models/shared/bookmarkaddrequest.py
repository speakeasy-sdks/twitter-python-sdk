import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils


@dataclass_json
@dataclasses.dataclass
class BookmarkAddRequest:
    tweet_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('tweet_id') }})
    
