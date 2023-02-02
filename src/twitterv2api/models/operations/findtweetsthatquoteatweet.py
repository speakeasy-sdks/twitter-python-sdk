import dataclasses
from typing import Optional
from enum import Enum
from ..shared import tweetexpansionsparameter_enum as shared_tweetexpansionsparameter_enum
from ..shared import mediafieldsparameter_enum as shared_mediafieldsparameter_enum
from ..shared import placefieldsparameter_enum as shared_placefieldsparameter_enum
from ..shared import pollfieldsparameter_enum as shared_pollfieldsparameter_enum
from ..shared import tweetfieldsparameter_enum as shared_tweetfieldsparameter_enum
from ..shared import userfieldsparameter_enum as shared_userfieldsparameter_enum
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import get2tweetsidquotetweetsresponse as shared_get2tweetsidquotetweetsresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class FindTweetsThatQuoteATweetPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    
class FindTweetsThatQuoteATweetExcludeEnum(str, Enum):
    REPLIES = "replies"
    RETWEETS = "retweets"


@dataclasses.dataclass
class FindTweetsThatQuoteATweetQueryParams:
    exclude: Optional[list[FindTweetsThatQuoteATweetExcludeEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'exclude', 'style': 'form', 'explode': False }})
    expansions: Optional[list[shared_tweetexpansionsparameter_enum.TweetExpansionsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'expansions', 'style': 'form', 'explode': False }})
    max_results: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'max_results', 'style': 'form', 'explode': True }})
    media_fields: Optional[list[shared_mediafieldsparameter_enum.MediaFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'media.fields', 'style': 'form', 'explode': False }})
    pagination_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pagination_token', 'style': 'form', 'explode': True }})
    place_fields: Optional[list[shared_placefieldsparameter_enum.PlaceFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'place.fields', 'style': 'form', 'explode': False }})
    poll_fields: Optional[list[shared_pollfieldsparameter_enum.PollFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'poll.fields', 'style': 'form', 'explode': False }})
    tweet_fields: Optional[list[shared_tweetfieldsparameter_enum.TweetFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tweet.fields', 'style': 'form', 'explode': False }})
    user_fields: Optional[list[shared_userfieldsparameter_enum.UserFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user.fields', 'style': 'form', 'explode': False }})
    

@dataclasses.dataclass
class FindTweetsThatQuoteATweetSecurity:
    bearer_token: Optional[shared_security.SchemeBearerToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class FindTweetsThatQuoteATweetRequest:
    path_params: FindTweetsThatQuoteATweetPathParams = dataclasses.field()
    query_params: FindTweetsThatQuoteATweetQueryParams = dataclasses.field()
    security: FindTweetsThatQuoteATweetSecurity = dataclasses.field()
    

@dataclasses.dataclass
class FindTweetsThatQuoteATweetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get2_tweets_id_quote_tweets_response: Optional[shared_get2tweetsidquotetweetsresponse.Get2TweetsIDQuoteTweetsResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
