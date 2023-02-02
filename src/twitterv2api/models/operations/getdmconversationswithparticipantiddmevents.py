import dataclasses
from typing import Optional
from enum import Enum
from ..shared import dmeventfieldsparameter_enum as shared_dmeventfieldsparameter_enum
from ..shared import dmeventexpansionsparameter_enum as shared_dmeventexpansionsparameter_enum
from ..shared import mediafieldsparameter_enum as shared_mediafieldsparameter_enum
from ..shared import tweetfieldsparameter_enum as shared_tweetfieldsparameter_enum
from ..shared import userfieldsparameter_enum as shared_userfieldsparameter_enum
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import get2dmconversationswithparticipantiddmeventsresponse as shared_get2dmconversationswithparticipantiddmeventsresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class GetDmConversationsWithParticipantIDDmEventsPathParams:
    participant_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'participant_id', 'style': 'simple', 'explode': False }})
    
class GetDmConversationsWithParticipantIDDmEventsEventTypesEnum(str, Enum):
    MESSAGE_CREATE = "MessageCreate"
    PARTICIPANTS_JOIN = "ParticipantsJoin"
    PARTICIPANTS_LEAVE = "ParticipantsLeave"


@dataclasses.dataclass
class GetDmConversationsWithParticipantIDDmEventsQueryParams:
    dm_event_fields: Optional[list[shared_dmeventfieldsparameter_enum.DmEventFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'dm_event.fields', 'style': 'form', 'explode': False }})
    event_types: Optional[list[GetDmConversationsWithParticipantIDDmEventsEventTypesEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'event_types', 'style': 'form', 'explode': False }})
    expansions: Optional[list[shared_dmeventexpansionsparameter_enum.DmEventExpansionsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'expansions', 'style': 'form', 'explode': False }})
    max_results: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'max_results', 'style': 'form', 'explode': True }})
    media_fields: Optional[list[shared_mediafieldsparameter_enum.MediaFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'media.fields', 'style': 'form', 'explode': False }})
    pagination_token: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pagination_token', 'style': 'form', 'explode': True }})
    tweet_fields: Optional[list[shared_tweetfieldsparameter_enum.TweetFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tweet.fields', 'style': 'form', 'explode': False }})
    user_fields: Optional[list[shared_userfieldsparameter_enum.UserFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user.fields', 'style': 'form', 'explode': False }})
    

@dataclasses.dataclass
class GetDmConversationsWithParticipantIDDmEventsSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class GetDmConversationsWithParticipantIDDmEventsRequest:
    path_params: GetDmConversationsWithParticipantIDDmEventsPathParams = dataclasses.field()
    query_params: GetDmConversationsWithParticipantIDDmEventsQueryParams = dataclasses.field()
    security: GetDmConversationsWithParticipantIDDmEventsSecurity = dataclasses.field()
    

@dataclasses.dataclass
class GetDmConversationsWithParticipantIDDmEventsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get2_dm_conversations_with_participant_id_dm_events_response: Optional[shared_get2dmconversationswithparticipantiddmeventsresponse.Get2DmConversationsWithParticipantIDDmEventsResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
