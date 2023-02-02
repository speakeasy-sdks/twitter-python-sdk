import dataclasses
from typing import Optional
from enum import Enum
from ..shared import compliancejobfieldsparameter_enum as shared_compliancejobfieldsparameter_enum
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import get2compliancejobsidresponse as shared_get2compliancejobsidresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class GetBatchComplianceJobPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetBatchComplianceJobQueryParams:
    compliance_job_fields: Optional[list[shared_compliancejobfieldsparameter_enum.ComplianceJobFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'compliance_job.fields', 'style': 'form', 'explode': False }})
    

@dataclasses.dataclass
class GetBatchComplianceJobSecurity:
    bearer_token: shared_security.SchemeBearerToken = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class GetBatchComplianceJobRequest:
    path_params: GetBatchComplianceJobPathParams = dataclasses.field()
    query_params: GetBatchComplianceJobQueryParams = dataclasses.field()
    security: GetBatchComplianceJobSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetBatchComplianceJobResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get2_compliance_jobs_id_response: Optional[shared_get2compliancejobsidresponse.Get2ComplianceJobsIDResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
