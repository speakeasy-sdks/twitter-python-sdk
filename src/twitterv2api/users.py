import requests
from typing import Optional
from twitterv2api.models import shared, operations
from . import utils

class Users:
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

    
    def find_my_user(self, request: operations.FindMyUserRequest) -> operations.FindMyUserResponse:
        r"""User lookup me
        This endpoint returns information about the requesting User.
        https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-me
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/users/me"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.FindMyUserResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersMeResponse])
                res.get2_users_me_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def find_user_by_id(self, request: operations.FindUserByIDRequest) -> operations.FindUserByIDResponse:
        r"""User lookup by ID
        This endpoint returns information about a User. Specify User by ID.
        https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.FindUserByIDResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersIDResponse])
                res.get2_users_id_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def find_user_by_username(self, request: operations.FindUserByUsernameRequest) -> operations.FindUserByUsernameResponse:
        r"""User lookup by username
        This endpoint returns information about a User. Specify User by username.
        https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/by/username/{username}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.FindUserByUsernameResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersByUsernameUsernameResponse])
                res.get2_users_by_username_username_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def find_users_by_id(self, request: operations.FindUsersByIDRequest) -> operations.FindUsersByIDResponse:
        r"""User lookup by IDs
        This endpoint returns information about Users. Specify Users by their ID.
        https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/users"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.FindUsersByIDResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersResponse])
                res.get2_users_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def find_users_by_username(self, request: operations.FindUsersByUsernameRequest) -> operations.FindUsersByUsernameResponse:
        r"""User lookup by usernames
        This endpoint returns information about Users. Specify Users by their username.
        https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/users/by"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.FindUsersByUsernameResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersByResponse])
                res.get2_users_by_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_get_followers(self, request: operations.ListGetFollowersRequest) -> operations.ListGetFollowersResponse:
        r"""Returns User objects that follow a List by the provided List ID
        Returns a list of Users that follow a List by the provided List ID
        https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-followers
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/lists/{id}/followers", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListGetFollowersResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2ListsIDFollowersResponse])
                res.get2_lists_id_followers_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_get_members(self, request: operations.ListGetMembersRequest) -> operations.ListGetMembersResponse:
        r"""Returns User objects that are members of a List by the provided List ID.
        Returns a list of Users that are members of a List by the provided List ID.
        https://developer.twitter.com/en/docs/twitter-api/lists/list-members/api-reference/get-users-id-list_memberships
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/lists/{id}/members", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListGetMembersResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2ListsIDMembersResponse])
                res.get2_lists_id_members_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def tweets_id_liking_users(self, request: operations.TweetsIDLikingUsersRequest) -> operations.TweetsIDLikingUsersResponse:
        r"""Returns User objects that have liked the provided Tweet ID
        Returns a list of Users that have liked the provided Tweet ID
        https://developer.twitter.com/en/docs/twitter-api/tweets/likes/api-reference/get-tweets-id-liking_users
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/tweets/{id}/liking_users", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.TweetsIDLikingUsersResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2TweetsIDLikingUsersResponse])
                res.get2_tweets_id_liking_users_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def tweets_id_retweeting_users(self, request: operations.TweetsIDRetweetingUsersRequest) -> operations.TweetsIDRetweetingUsersResponse:
        r"""Returns User objects that have retweeted the provided Tweet ID
        Returns a list of Users that have retweeted the provided Tweet ID
        https://developer.twitter.com/en/docs/twitter-api/tweets/retweets/api-reference/get-tweets-id-retweeted_by
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/tweets/{id}/retweeted_by", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.TweetsIDRetweetingUsersResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2TweetsIDRetweetedByResponse])
                res.get2_tweets_id_retweeted_by_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def users_id_block(self, request: operations.UsersIDBlockRequest) -> operations.UsersIDBlockResponse:
        r"""Block User by User ID
        Causes the User (in the path) to block the target User. The User (in the path) must match the User context authorizing the request
        https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/post-users-user_id-blocking
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/blocking", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UsersIDBlockResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.BlockUserMutationResponse])
                res.block_user_mutation_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def users_id_blocking(self, request: operations.UsersIDBlockingRequest) -> operations.UsersIDBlockingResponse:
        r"""Returns User objects that are blocked by provided User ID
        Returns a list of Users that are blocked by the provided User ID
        https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/get-users-blocking
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/blocking", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.UsersIDBlockingResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersIDBlockingResponse])
                res.get2_users_id_blocking_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def users_id_follow(self, request: operations.UsersIDFollowRequest) -> operations.UsersIDFollowResponse:
        r"""Follow User
        Causes the User(in the path) to follow, or “request to follow” for protected Users, the target User. The User(in the path) must match the User context authorizing the request
        https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/post-users-source_user_id-following
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/following", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UsersIDFollowResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.UsersFollowingCreateResponse])
                res.users_following_create_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def users_id_followers(self, request: operations.UsersIDFollowersRequest) -> operations.UsersIDFollowersResponse:
        r"""Followers by User ID
        Returns a list of Users who are followers of the specified User ID.
        https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-followers
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/followers", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.UsersIDFollowersResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersIDFollowersResponse])
                res.get2_users_id_followers_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def users_id_following(self, request: operations.UsersIDFollowingRequest) -> operations.UsersIDFollowingResponse:
        r"""Following by User ID
        Returns a list of Users that are being followed by the provided User ID
        https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/get-users-id-following
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/following", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.UsersIDFollowingResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersIDFollowingResponse])
                res.get2_users_id_following_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def users_id_mute(self, request: operations.UsersIDMuteRequest) -> operations.UsersIDMuteResponse:
        r"""Mute User by User ID.
        Causes the User (in the path) to mute the target User. The User (in the path) must match the User context authorizing the request.
        https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/post-users-user_id-muting
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/muting", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.UsersIDMuteResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.MuteUserMutationResponse])
                res.mute_user_mutation_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def users_id_muting(self, request: operations.UsersIDMutingRequest) -> operations.UsersIDMutingResponse:
        r"""Returns User objects that are muted by the provided User ID
        Returns a list of Users that are muted by the provided User ID
        https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/get-users-muting
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/muting", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.UsersIDMutingResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersIDMutingResponse])
                res.get2_users_id_muting_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def users_id_unblock(self, request: operations.UsersIDUnblockRequest) -> operations.UsersIDUnblockResponse:
        r"""Unblock User by User ID
        Causes the source User to unblock the target User. The source User must match the User context authorizing the request
        https://developer.twitter.com/en/docs/twitter-api/users/blocks/api-reference/delete-users-user_id-blocking
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{source_user_id}/blocking/{target_user_id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.UsersIDUnblockResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.BlockUserMutationResponse])
                res.block_user_mutation_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def users_id_unfollow(self, request: operations.UsersIDUnfollowRequest) -> operations.UsersIDUnfollowResponse:
        r"""Unfollow User
        Causes the source User to unfollow the target User. The source User must match the User context authorizing the request
        https://developer.twitter.com/en/docs/twitter-api/users/follows/api-reference/delete-users-source_id-following
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{source_user_id}/following/{target_user_id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.UsersIDUnfollowResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.UsersFollowingDeleteResponse])
                res.users_following_delete_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def users_id_unmute(self, request: operations.UsersIDUnmuteRequest) -> operations.UsersIDUnmuteResponse:
        r"""Unmute User by User ID
        Causes the source User to unmute the target User. The source User must match the User context authorizing the request
        https://developer.twitter.com/en/docs/twitter-api/users/mutes/api-reference/delete-users-user_id-muting
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{source_user_id}/muting/{target_user_id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.UsersIDUnmuteResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.MuteUserMutationResponse])
                res.mute_user_mutation_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    