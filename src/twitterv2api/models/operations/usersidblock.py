import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import blockuserrequest as shared_blockuserrequest
from ..shared import blockusermutationresponse as shared_blockusermutationresponse
from ..shared import error as shared_error
from ..shared import problem as shared_problem


@dataclasses.dataclass
class UsersIDBlockPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UsersIDBlockSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class UsersIDBlockRequest:
    path_params: UsersIDBlockPathParams = dataclasses.field()
    request: shared_blockuserrequest.BlockUserRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: UsersIDBlockSecurity = dataclasses.field()
    

@dataclasses.dataclass
class UsersIDBlockResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    block_user_mutation_response: Optional[shared_blockusermutationresponse.BlockUserMutationResponse] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
