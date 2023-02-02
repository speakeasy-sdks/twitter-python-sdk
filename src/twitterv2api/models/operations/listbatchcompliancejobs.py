import dataclasses
from typing import Optional
from enum import Enum
from ..shared import compliancejobfieldsparameter_enum as shared_compliancejobfieldsparameter_enum
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import get2compliancejobsresponse as shared_get2compliancejobsresponse
from ..shared import problem as shared_problem

class ListBatchComplianceJobsStatusEnum(str, Enum):
    CREATED = "created"
    IN_PROGRESS = "in_progress"
    FAILED = "failed"
    COMPLETE = "complete"

class ListBatchComplianceJobsTypeEnum(str, Enum):
    TWEETS = "tweets"
    USERS = "users"


@dataclasses.dataclass
class ListBatchComplianceJobsQueryParams:
    type: ListBatchComplianceJobsTypeEnum = dataclasses.field(metadata={'query_param': { 'field_name': 'type', 'style': 'form', 'explode': True }})
    compliance_job_fields: Optional[list[shared_compliancejobfieldsparameter_enum.ComplianceJobFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'compliance_job.fields', 'style': 'form', 'explode': False }})
    status: Optional[ListBatchComplianceJobsStatusEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'status', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListBatchComplianceJobsSecurity:
    bearer_token: shared_security.SchemeBearerToken = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class ListBatchComplianceJobsRequest:
    query_params: ListBatchComplianceJobsQueryParams = dataclasses.field()
    security: ListBatchComplianceJobsSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ListBatchComplianceJobsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get2_compliance_jobs_response: Optional[shared_get2compliancejobsresponse.Get2ComplianceJobsResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
