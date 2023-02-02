import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import problem as shared_problem
from ..shared import ruleslookupresponse as shared_ruleslookupresponse


@dataclasses.dataclass
class GetRulesQueryParams:
    ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'ids', 'style': 'form', 'explode': True }})
    max_results: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'max_results', 'style': 'form', 'explode': True }})
    pagination_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pagination_token', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetRulesSecurity:
    bearer_token: shared_security.SchemeBearerToken = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class GetRulesRequest:
    query_params: GetRulesQueryParams = dataclasses.field()
    security: GetRulesSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetRulesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    rules_lookup_response: Optional[shared_ruleslookupresponse.RulesLookupResponse] = dataclasses.field(default=None)
    
