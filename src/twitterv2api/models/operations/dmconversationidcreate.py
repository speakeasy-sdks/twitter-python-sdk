import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import createdmconversationrequest as shared_createdmconversationrequest
from ..shared import createdmeventresponse as shared_createdmeventresponse
from ..shared import error as shared_error
from ..shared import problem as shared_problem


@dataclasses.dataclass
class DmConversationIDCreateSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class DmConversationIDCreateRequest:
    security: DmConversationIDCreateSecurity = dataclasses.field()
    request: Optional[shared_createdmconversationrequest.CreateDmConversationRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class DmConversationIDCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_dm_event_response: Optional[shared_createdmeventresponse.CreateDmEventResponse] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
