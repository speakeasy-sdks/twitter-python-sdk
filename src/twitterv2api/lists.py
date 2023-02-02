import requests
from typing import Optional
from twitterv2api.models import shared, operations
from . import utils

class Lists:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def get_user_list_memberships(self, request: operations.GetUserListMembershipsRequest) -> operations.GetUserListMembershipsResponse:
        r"""Get a User's List Memberships
        Get a User's List Memberships.
        https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-users-id-list_memberships
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/list_memberships", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetUserListMembershipsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersIDListMembershipsResponse])
                res.get2_users_id_list_memberships_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_add_member(self, request: operations.ListAddMemberRequest) -> operations.ListAddMemberResponse:
        r"""Add a List member
        Causes a User to become a member of a List.
        https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/post-lists-id-members
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/lists/{id}/members", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListAddMemberResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListMutateResponse])
                res.list_mutate_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_id_create(self, request: operations.ListIDCreateRequest) -> operations.ListIDCreateResponse:
        r"""Create List
        Creates a new List.
        https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/post-lists
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/lists"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListIDCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListCreateResponse])
                res.list_create_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_id_delete(self, request: operations.ListIDDeleteRequest) -> operations.ListIDDeleteResponse:
        r"""Delete List
        Delete a List that you own.
        https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/delete-lists-id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/lists/{id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListIDDeleteResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListDeleteResponse])
                res.list_delete_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_id_get(self, request: operations.ListIDGetRequest) -> operations.ListIDGetResponse:
        r"""List lookup by List ID.
        Returns a List.
        https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-lists-id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/lists/{id}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListIDGetResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2ListsIDResponse])
                res.get2_lists_id_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_id_update(self, request: operations.ListIDUpdateRequest) -> operations.ListIDUpdateResponse:
        r"""Update List.
        Update a List that you own.
        https://developer.twitter.com/en/docs/twitter-api/lists/manage-lists/api-reference/put-lists-id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/lists/{id}", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListIDUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListUpdateResponse])
                res.list_update_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_remove_member(self, request: operations.ListRemoveMemberRequest) -> operations.ListRemoveMemberResponse:
        r"""Remove a List member
        Causes a User to be removed from the members of a List.
        https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/delete-lists-id-members-user_id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/lists/{id}/members/{user_id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListRemoveMemberResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListMutateResponse])
                res.list_mutate_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_user_follow(self, request: operations.ListUserFollowRequest) -> operations.ListUserFollowResponse:
        r"""Follow a List
        Causes a User to follow a List.
        https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/post-users-id-followed-lists
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/followed_lists", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListUserFollowResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListFollowedResponse])
                res.list_followed_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_user_owned_lists(self, request: operations.ListUserOwnedListsRequest) -> operations.ListUserOwnedListsResponse:
        r"""Get a User's Owned Lists.
        Get a User's Owned Lists.
        https://developer.twitter.com/en/docs/twitter-api/lists/list-lookup/api-reference/get-users-id-owned_lists
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/owned_lists", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListUserOwnedListsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersIDOwnedListsResponse])
                res.get2_users_id_owned_lists_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_user_pin(self, request: operations.ListUserPinRequest) -> operations.ListUserPinResponse:
        r"""Pin a List
        Causes a User to pin a List.
        https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/post-users-id-pinned-lists
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/pinned_lists", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ListUserPinResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListPinnedResponse])
                res.list_pinned_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_user_pinned_lists(self, request: operations.ListUserPinnedListsRequest) -> operations.ListUserPinnedListsResponse:
        r"""Get a User's Pinned Lists
        Get a User's Pinned Lists.
        https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/get-users-id-pinned_lists
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/pinned_lists", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListUserPinnedListsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersIDPinnedListsResponse])
                res.get2_users_id_pinned_lists_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_user_unfollow(self, request: operations.ListUserUnfollowRequest) -> operations.ListUserUnfollowResponse:
        r"""Unfollow a List
        Causes a User to unfollow a List.
        https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/delete-users-id-followed-lists-list_id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/followed_lists/{list_id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListUserUnfollowResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListFollowedResponse])
                res.list_followed_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_user_unpin(self, request: operations.ListUserUnpinRequest) -> operations.ListUserUnpinResponse:
        r"""Unpin a List
        Causes a User to remove a pinned List.
        https://developer.twitter.com/en/docs/twitter-api/lists/pinned-lists/api-reference/delete-users-id-pinned-lists-list_id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/pinned_lists/{list_id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ListUserUnpinResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.ListUnpinResponse])
                res.list_unpin_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def user_followed_lists(self, request: operations.UserFollowedListsRequest) -> operations.UserFollowedListsResponse:
        r"""Get User's Followed Lists
        Returns a User's followed Lists.
        https://developer.twitter.com/en/docs/twitter-api/lists/list-follows/api-reference/get-users-id-followed_lists
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/followed_lists", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.UserFollowedListsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersIDFollowedListsResponse])
                res.get2_users_id_followed_lists_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    