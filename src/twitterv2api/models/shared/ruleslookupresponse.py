import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import rule as shared_rule
from ..shared import rulesresponsemetadata as shared_rulesresponsemetadata


@dataclass_json
@dataclasses.dataclass
class RulesLookupResponse:
    meta: shared_rulesresponsemetadata.RulesResponseMetadata = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('meta') }})
    data: Optional[list[shared_rule.Rule]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    
