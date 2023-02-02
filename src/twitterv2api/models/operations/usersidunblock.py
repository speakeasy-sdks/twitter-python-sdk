import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import blockusermutationresponse as shared_blockusermutationresponse
from ..shared import error as shared_error
from ..shared import problem as shared_problem


@dataclasses.dataclass
class UsersIDUnblockPathParams:
    source_user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'source_user_id', 'style': 'simple', 'explode': False }})
    target_user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'target_user_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UsersIDUnblockSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class UsersIDUnblockRequest:
    path_params: UsersIDUnblockPathParams = dataclasses.field()
    security: UsersIDUnblockSecurity = dataclasses.field()
    

@dataclasses.dataclass
class UsersIDUnblockResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    block_user_mutation_response: Optional[shared_blockusermutationresponse.BlockUserMutationResponse] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
