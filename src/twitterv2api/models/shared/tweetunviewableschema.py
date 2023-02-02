import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import tweetunviewable as shared_tweetunviewable


@dataclass_json
@dataclasses.dataclass
class TweetUnviewableSchema:
    public_tweet_unviewable: shared_tweetunviewable.TweetUnviewable = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('public_tweet_unviewable') }})
    
