import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import tweetcreaterequest as shared_tweetcreaterequest
from ..shared import error as shared_error
from ..shared import problem as shared_problem
from ..shared import tweetcreateresponse as shared_tweetcreateresponse


@dataclasses.dataclass
class CreateTweetSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class CreateTweetRequest:
    request: shared_tweetcreaterequest.TweetCreateRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: CreateTweetSecurity = dataclasses.field()
    

@dataclasses.dataclass
class CreateTweetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    tweet_create_response: Optional[shared_tweetcreateresponse.TweetCreateResponse] = dataclasses.field(default=None)
    
