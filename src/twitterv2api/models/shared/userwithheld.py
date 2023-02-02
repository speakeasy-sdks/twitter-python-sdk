import dataclasses
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from twitterv2api import utils

class UserWithheldScopeEnum(str, Enum):
    USER = "user"


@dataclass_json
@dataclasses.dataclass
class UserWithheld:
    r"""UserWithheld
    Indicates withholding details for [withheld content](https://help.twitter.com/en/rules-and-policies/tweet-withheld-by-country).
    """
    
    country_codes: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('country_codes') }})
    scope: Optional[UserWithheldScopeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('scope') }})
    
