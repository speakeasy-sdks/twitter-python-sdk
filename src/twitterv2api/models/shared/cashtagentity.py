import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils


@dataclass_json
@dataclasses.dataclass
class CashtagEntity:
    r"""CashtagEntity
    Represent the portion of text recognized as a Cashtag, and its start and end position within the text.
    """
    
    end: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('end') }})
    start: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('start') }})
    tag: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag') }})
    
