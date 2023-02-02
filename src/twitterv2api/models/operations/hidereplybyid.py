import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import tweethiderequest as shared_tweethiderequest
from ..shared import error as shared_error
from ..shared import problem as shared_problem
from ..shared import tweethideresponse as shared_tweethideresponse


@dataclasses.dataclass
class HideReplyByIDPathParams:
    tweet_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'tweet_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class HideReplyByIDSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class HideReplyByIDRequest:
    path_params: HideReplyByIDPathParams = dataclasses.field()
    security: HideReplyByIDSecurity = dataclasses.field()
    request: Optional[shared_tweethiderequest.TweetHideRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class HideReplyByIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    tweet_hide_response: Optional[shared_tweethideresponse.TweetHideResponse] = dataclasses.field(default=None)
    
