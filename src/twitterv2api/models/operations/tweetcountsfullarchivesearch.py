import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from enum import Enum
from ..shared import searchcountfieldsparameter_enum as shared_searchcountfieldsparameter_enum
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import get2tweetscountsallresponse as shared_get2tweetscountsallresponse
from ..shared import problem as shared_problem

class TweetCountsFullArchiveSearchGranularityEnum(str, Enum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"


@dataclasses.dataclass
class TweetCountsFullArchiveSearchQueryParams:
    query: str = dataclasses.field(metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    end_time: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_time', 'style': 'form', 'explode': True }})
    granularity: Optional[TweetCountsFullArchiveSearchGranularityEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'granularity', 'style': 'form', 'explode': True }})
    next_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'next_token', 'style': 'form', 'explode': True }})
    pagination_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pagination_token', 'style': 'form', 'explode': True }})
    search_count_fields: Optional[list[shared_searchcountfieldsparameter_enum.SearchCountFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search_count.fields', 'style': 'form', 'explode': False }})
    since_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'since_id', 'style': 'form', 'explode': True }})
    start_time: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start_time', 'style': 'form', 'explode': True }})
    until_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'until_id', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class TweetCountsFullArchiveSearchSecurity:
    bearer_token: shared_security.SchemeBearerToken = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    

@dataclasses.dataclass
class TweetCountsFullArchiveSearchRequest:
    query_params: TweetCountsFullArchiveSearchQueryParams = dataclasses.field()
    security: TweetCountsFullArchiveSearchSecurity = dataclasses.field()
    

@dataclasses.dataclass
class TweetCountsFullArchiveSearchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get2_tweets_counts_all_response: Optional[shared_get2tweetscountsallresponse.Get2TweetsCountsAllResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
