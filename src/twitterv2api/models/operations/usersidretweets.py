import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import usersretweetscreaterequest as shared_usersretweetscreaterequest
from ..shared import error as shared_error
from ..shared import problem as shared_problem
from ..shared import usersretweetscreateresponse as shared_usersretweetscreateresponse


@dataclasses.dataclass
class UsersIDRetweetsPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UsersIDRetweetsSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class UsersIDRetweetsRequest:
    path_params: UsersIDRetweetsPathParams = dataclasses.field()
    security: UsersIDRetweetsSecurity = dataclasses.field()
    request: Optional[shared_usersretweetscreaterequest.UsersRetweetsCreateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UsersIDRetweetsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    users_retweets_create_response: Optional[shared_usersretweetscreateresponse.UsersRetweetsCreateResponse] = dataclasses.field(default=None)
    
