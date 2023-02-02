import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import muteusermutationresponse as shared_muteusermutationresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class UsersIDUnmutePathParams:
    source_user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'source_user_id', 'style': 'simple', 'explode': False }})
    target_user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'target_user_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UsersIDUnmuteSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class UsersIDUnmuteRequest:
    path_params: UsersIDUnmutePathParams = dataclasses.field()
    security: UsersIDUnmuteSecurity = dataclasses.field()
    

@dataclasses.dataclass
class UsersIDUnmuteResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    mute_user_mutation_response: Optional[shared_muteusermutationresponse.MuteUserMutationResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
