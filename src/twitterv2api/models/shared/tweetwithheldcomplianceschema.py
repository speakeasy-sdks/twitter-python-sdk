import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import tweettakedowncomplianceschema as shared_tweettakedowncomplianceschema


@dataclass_json
@dataclasses.dataclass
class TweetWithheldComplianceSchema:
    withheld: shared_tweettakedowncomplianceschema.TweetTakedownComplianceSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('withheld') }})
    
