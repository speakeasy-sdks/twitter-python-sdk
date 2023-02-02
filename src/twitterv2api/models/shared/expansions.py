import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import media as shared_media
from ..shared import place as shared_place
from ..shared import poll as shared_poll
from ..shared import topic as shared_topic
from ..shared import tweet as shared_tweet
from ..shared import user as shared_user


@dataclass_json
@dataclasses.dataclass
class Expansions:
    media: Optional[list[shared_media.Media]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('media') }})
    places: Optional[list[shared_place.Place]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('places') }})
    polls: Optional[list[shared_poll.Poll]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('polls') }})
    topics: Optional[list[shared_topic.Topic]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('topics') }})
    tweets: Optional[list[shared_tweet.Tweet]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tweets') }})
    users: Optional[list[shared_user.User]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('users') }})
    
