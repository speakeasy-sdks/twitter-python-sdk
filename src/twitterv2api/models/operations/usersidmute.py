import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import muteuserrequest as shared_muteuserrequest
from ..shared import error as shared_error
from ..shared import muteusermutationresponse as shared_muteusermutationresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class UsersIDMutePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UsersIDMuteSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class UsersIDMuteRequest:
    path_params: UsersIDMutePathParams = dataclasses.field()
    security: UsersIDMuteSecurity = dataclasses.field()
    request: Optional[shared_muteuserrequest.MuteUserRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UsersIDMuteResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    mute_user_mutation_response: Optional[shared_muteusermutationresponse.MuteUserMutationResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
