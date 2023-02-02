import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import contextannotationdomainfields as shared_contextannotationdomainfields
from ..shared import contextannotationentityfields as shared_contextannotationentityfields


@dataclass_json
@dataclasses.dataclass
class ContextAnnotation:
    r"""ContextAnnotation
    Annotation inferred from the Tweet text.
    """
    
    domain: shared_contextannotationdomainfields.ContextAnnotationDomainFields = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('domain') }})
    entity: shared_contextannotationentityfields.ContextAnnotationEntityFields = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('entity') }})
    
