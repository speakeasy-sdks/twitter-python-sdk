import dataclasses
from typing import Any,Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import createtextmessagerequest as shared_createtextmessagerequest
from ..shared import createattachmentsmessagerequest as shared_createattachmentsmessagerequest
from ..shared import createdmeventresponse as shared_createdmeventresponse
from ..shared import error as shared_error
from ..shared import problem as shared_problem


@dataclasses.dataclass
class DmConversationByIDEventIDCreatePathParams:
    dm_conversation_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dm_conversation_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DmConversationByIDEventIDCreateSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class DmConversationByIDEventIDCreateRequest:
    path_params: DmConversationByIDEventIDCreatePathParams = dataclasses.field()
    security: DmConversationByIDEventIDCreateSecurity = dataclasses.field()
    request: Optional[Any] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class DmConversationByIDEventIDCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_dm_event_response: Optional[shared_createdmeventresponse.CreateDmEventResponse] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
