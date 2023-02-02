import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import tweetnotice as shared_tweetnotice


@dataclass_json
@dataclasses.dataclass
class TweetNoticeSchema:
    public_tweet_notice: shared_tweetnotice.TweetNotice = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('public_tweet_notice') }})
    
