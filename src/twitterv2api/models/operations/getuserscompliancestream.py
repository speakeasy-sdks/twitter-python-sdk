import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import security as shared_security
from ..shared import userprotectcomplianceschema as shared_userprotectcomplianceschema
from ..shared import userunprotectcomplianceschema as shared_userunprotectcomplianceschema
from ..shared import userdeletecomplianceschema as shared_userdeletecomplianceschema
from ..shared import userundeletecomplianceschema as shared_userundeletecomplianceschema
from ..shared import usersuspendcomplianceschema as shared_usersuspendcomplianceschema
from ..shared import userunsuspendcomplianceschema as shared_userunsuspendcomplianceschema
from ..shared import userwithheldcomplianceschema as shared_userwithheldcomplianceschema
from ..shared import userscrubgeoschema as shared_userscrubgeoschema
from ..shared import userprofilemodificationcomplianceschema as shared_userprofilemodificationcomplianceschema
from ..shared import problem as shared_problem
from ..shared import error as shared_error


@dataclasses.dataclass
class GetUsersComplianceStreamQueryParams:
    partition: int = dataclasses.field(metadata={'query_param': { 'field_name': 'partition', 'style': 'form', 'explode': True }})
    backfill_minutes: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'backfill_minutes', 'style': 'form', 'explode': True }})
    end_time: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_time', 'style': 'form', 'explode': True }})
    start_time: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start_time', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetUsersComplianceStreamSecurity:
    bearer_token: shared_security.SchemeBearerToken = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclass_json
@dataclasses.dataclass
class GetUsersComplianceStream200ApplicationJSON1:
    r"""GetUsersComplianceStream200ApplicationJSON1
    User compliance event.
    """
    
    data: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    

@dataclass_json
@dataclasses.dataclass
class GetUsersComplianceStream200ApplicationJSON2:
    errors: list[shared_problem.Problem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors') }})
    

@dataclasses.dataclass
class GetUsersComplianceStreamRequest:
    query_params: GetUsersComplianceStreamQueryParams = dataclasses.field()
    security: GetUsersComplianceStreamSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetUsersComplianceStreamResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    user_compliance_stream_response: Optional[Any] = dataclasses.field(default=None)
    
