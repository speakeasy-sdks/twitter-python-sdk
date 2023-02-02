import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import tweeteditcomplianceobjectschema as shared_tweeteditcomplianceobjectschema


@dataclass_json
@dataclasses.dataclass
class TweetEditComplianceSchema:
    tweet_edit: shared_tweeteditcomplianceobjectschema.TweetEditComplianceObjectSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('tweet_edit') }})
    
