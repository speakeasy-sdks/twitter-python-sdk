import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from enum import Enum
from ..shared import searchcountfieldsparameter_enum as shared_searchcountfieldsparameter_enum
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import get2tweetscountsrecentresponse as shared_get2tweetscountsrecentresponse
from ..shared import problem as shared_problem

class TweetCountsRecentSearchGranularityEnum(str, Enum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"


@dataclasses.dataclass
class TweetCountsRecentSearchQueryParams:
    query: str = dataclasses.field(metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    end_time: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_time', 'style': 'form', 'explode': True }})
    granularity: Optional[TweetCountsRecentSearchGranularityEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'granularity', 'style': 'form', 'explode': True }})
    next_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'next_token', 'style': 'form', 'explode': True }})
    pagination_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pagination_token', 'style': 'form', 'explode': True }})
    search_count_fields: Optional[list[shared_searchcountfieldsparameter_enum.SearchCountFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search_count.fields', 'style': 'form', 'explode': False }})
    since_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'since_id', 'style': 'form', 'explode': True }})
    start_time: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start_time', 'style': 'form', 'explode': True }})
    until_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'until_id', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class TweetCountsRecentSearchSecurity:
    bearer_token: shared_security.SchemeBearerToken = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class TweetCountsRecentSearchRequest:
    query_params: TweetCountsRecentSearchQueryParams = dataclasses.field()
    security: TweetCountsRecentSearchSecurity = dataclasses.field()
    

@dataclasses.dataclass
class TweetCountsRecentSearchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get2_tweets_counts_recent_response: Optional[shared_get2tweetscountsrecentresponse.Get2TweetsCountsRecentResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
