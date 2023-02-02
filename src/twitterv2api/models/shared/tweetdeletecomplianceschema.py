import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import tweetcomplianceschema as shared_tweetcomplianceschema


@dataclass_json
@dataclasses.dataclass
class TweetDeleteComplianceSchema:
    delete: shared_tweetcomplianceschema.TweetComplianceSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('delete') }})
    
