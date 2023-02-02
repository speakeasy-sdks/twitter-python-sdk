import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import dmmediaattachment as shared_dmmediaattachment


@dataclass_json
@dataclasses.dataclass
class CreateTextMessageRequest:
    text: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('text') }})
    attachments: Optional[list[shared_dmmediaattachment.DmMediaAttachment]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attachments') }})
    
