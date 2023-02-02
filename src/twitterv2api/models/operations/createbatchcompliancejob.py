import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import createcompliancejobrequest as shared_createcompliancejobrequest
from ..shared import createcompliancejobresponse as shared_createcompliancejobresponse
from ..shared import error as shared_error
from ..shared import problem as shared_problem


@dataclasses.dataclass
class CreateBatchComplianceJobSecurity:
    bearer_token: shared_security.SchemeBearerToken = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class CreateBatchComplianceJobRequest:
    request: shared_createcompliancejobrequest.CreateComplianceJobRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: CreateBatchComplianceJobSecurity = dataclasses.field()
    

@dataclasses.dataclass
class CreateBatchComplianceJobResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_compliance_job_response: Optional[shared_createcompliancejobresponse.CreateComplianceJobResponse] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
