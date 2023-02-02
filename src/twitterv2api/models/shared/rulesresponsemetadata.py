import dataclasses
from typing import Any,Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils


@dataclass_json
@dataclasses.dataclass
class RulesResponseMetadataSummary1:
    r"""RulesResponseMetadataSummary1
    A summary of the results of the addition of user-specified stream filtering rules.
    """
    
    created: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created') }})
    invalid: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('invalid') }})
    not_created: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('not_created') }})
    valid: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('valid') }})
    

@dataclass_json
@dataclasses.dataclass
class RulesResponseMetadataSummary2:
    deleted: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted') }})
    not_deleted: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('not_deleted') }})
    

@dataclass_json
@dataclasses.dataclass
class RulesResponseMetadata:
    sent: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('sent') }})
    next_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next_token') }})
    result_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('result_count') }})
    summary: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('summary') }})
    
