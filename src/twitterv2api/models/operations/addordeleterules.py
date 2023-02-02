import dataclasses
from typing import Any,Optional
from ..shared import security as shared_security
from ..shared import addrulesrequest as shared_addrulesrequest
from ..shared import deleterulesrequest as shared_deleterulesrequest
from ..shared import addordeleterulesresponse as shared_addordeleterulesresponse
from ..shared import error as shared_error
from ..shared import problem as shared_problem


@dataclasses.dataclass
class AddOrDeleteRulesQueryParams:
    dry_run: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'dry_run', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class AddOrDeleteRulesSecurity:
    bearer_token: shared_security.SchemeBearerToken = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class AddOrDeleteRulesRequest:
    query_params: AddOrDeleteRulesQueryParams = dataclasses.field()
    request: Any = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: AddOrDeleteRulesSecurity = dataclasses.field()
    

@dataclasses.dataclass
class AddOrDeleteRulesResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    add_or_delete_rules_response: Optional[shared_addordeleterulesresponse.AddOrDeleteRulesResponse] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
