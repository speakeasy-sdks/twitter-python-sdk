import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import security as shared_security
from ..shared import tweetdeletecomplianceschema as shared_tweetdeletecomplianceschema
from ..shared import tweetwithheldcomplianceschema as shared_tweetwithheldcomplianceschema
from ..shared import tweetdropcomplianceschema as shared_tweetdropcomplianceschema
from ..shared import tweetundropcomplianceschema as shared_tweetundropcomplianceschema
from ..shared import tweeteditcomplianceschema as shared_tweeteditcomplianceschema
from ..shared import problem as shared_problem
from ..shared import error as shared_error


@dataclasses.dataclass
class GetTweetsComplianceStreamQueryParams:
    partition: int = dataclasses.field(metadata={'query_param': { 'field_name': 'partition', 'style': 'form', 'explode': True }})
    backfill_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'backfill_minutes', 'style': 'form', 'explode': True }})
    end_time: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_time', 'style': 'form', 'explode': True }})
    start_time: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start_time', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetTweetsComplianceStreamSecurity:
    bearer_token: shared_security.SchemeBearerToken = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclass_json
@dataclasses.dataclass
class GetTweetsComplianceStream200ApplicationJSON1:
    r"""GetTweetsComplianceStream200ApplicationJSON1
    Compliance event.
    """
    
    data: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclass_json
@dataclasses.dataclass
class GetTweetsComplianceStream200ApplicationJSON2:
    errors: list[shared_problem.Problem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors') }})
    

@dataclasses.dataclass
class GetTweetsComplianceStreamRequest:
    query_params: GetTweetsComplianceStreamQueryParams = dataclasses.field()
    security: GetTweetsComplianceStreamSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetTweetsComplianceStreamResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    tweet_compliance_stream_response: Optional[Any] = dataclasses.field(default=None)
    
