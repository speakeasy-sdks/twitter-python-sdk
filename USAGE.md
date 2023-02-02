<!-- Start SDK Example Usage -->
```python
import twitterv2api
from twitterv2api.models import operations, shared

s = twitterv2api.TwitterV2API()
    
req = operations.GetUsersIDBookmarksRequest(
    security=operations.GetUsersIDBookmarksSecurity(
        o_auth2_user_token=shared.SchemeOAuth2UserToken(
            authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
        ),
    ),
    path_params=operations.GetUsersIDBookmarksPathParams(
        id="sit",
    ),
    query_params=operations.GetUsersIDBookmarksQueryParams(
        expansions=[
            "entities.mentions.username",
        ],
        max_results=501233450539197794,
        media_fields=[
            "public_metrics",
            "width",
            "width",
        ],
        pagination_token="fugit",
        place_fields=[
            "contained_within",
        ],
        poll_fields=[
            "voting_status",
            "options",
            "id",
        ],
        tweet_fields=[
            "id",
        ],
        user_fields=[
            "url",
            "public_metrics",
            "name",
        ],
    ),
)
    
res = s.bookmarks.get_users_id_bookmarks(req)

if res.get2_users_id_bookmarks_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->