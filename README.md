# Twitter API V2 - Python SDK

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install twitterv2api
```
<!-- End SDK Installation -->

## SDK Example Usage
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

<!-- Start SDK Available Operations -->
## SDK Available Operations

### Bookmarks

* `get_users_id_bookmarks` - Bookmarks by User
* `post_users_id_bookmarks` - Add Tweet to Bookmarks
* `users_id_bookmarks_delete` - Remove a bookmarked Tweet

### Compliance

* `create_batch_compliance_job` - Create compliance job
* `get_batch_compliance_job` - Get Compliance Job
* `get_tweets_compliance_stream` - Tweets Compliance stream
* `get_tweets_label_stream` - Tweets Label stream
* `get_users_compliance_stream` - Users Compliance stream
* `list_batch_compliance_jobs` - List Compliance Jobs

### Direct Messages

* `dm_conversation_by_id_event_id_create` - Send a new message to a DM Conversation
* `dm_conversation_id_create` - Create a new DM Conversation
* `dm_conversation_with_user_event_id_create` - Send a new message to a user
* `get_dm_conversations_id_dm_events` - Get DM Events for a DM Conversation
* `get_dm_conversations_with_participant_id_dm_events` - Get DM Events for a DM Conversation
* `get_dm_events` - Get recent DM Events

### General

* `get_open_api_spec` - Returns the OpenAPI Specification document.

### Lists

* `get_user_list_memberships` - Get a User's List Memberships
* `list_add_member` - Add a List member
* `list_id_create` - Create List
* `list_id_delete` - Delete List
* `list_id_get` - List lookup by List ID.
* `list_id_update` - Update List.
* `list_remove_member` - Remove a List member
* `list_user_follow` - Follow a List
* `list_user_owned_lists` - Get a User's Owned Lists.
* `list_user_pin` - Pin a List
* `list_user_pinned_lists` - Get a User's Pinned Lists
* `list_user_unfollow` - Unfollow a List
* `list_user_unpin` - Unpin a List
* `user_followed_lists` - Get User's Followed Lists

### Spaces

* `find_space_by_id` - Space lookup by Space ID
* `find_spaces_by_creator_ids` - Space lookup by their creators
* `find_spaces_by_ids` - Space lookup up Space IDs
* `search_spaces` - Search for Spaces
* `space_buyers` - Retrieve the list of Users who purchased a ticket to the given space
* `space_tweets` - Retrieve Tweets from a Space.

### Tweets

* `add_or_delete_rules` - Add/Delete rules
* `create_tweet` - Creation of a Tweet
* `delete_tweet_by_id` - Tweet delete by Tweet ID
* `find_tweet_by_id` - Tweet lookup by Tweet ID
* `find_tweets_by_id` - Tweet lookup by Tweet IDs
* `find_tweets_that_quote_a_tweet` - Retrieve Tweets that quote a Tweet.
* `get_rules` - Rules lookup
* `get_tweets_firehose_stream` - Firehose stream
* `get_tweets_sample10_stream` - Sample 10% stream
* `hide_reply_by_id` - Hide replies
* `lists_id_tweets` - List Tweets timeline by List ID.
* `sample_stream` - Sample stream
* `search_stream` - Filtered stream
* `space_buyers` - Retrieve the list of Users who purchased a ticket to the given space
* `space_tweets` - Retrieve Tweets from a Space.
* `tweet_counts_full_archive_search` - Full archive search counts
* `tweet_counts_recent_search` - Recent search counts
* `tweets_fullarchive_search` - Full-archive search
* `tweets_recent_search` - Recent search
* `users_id_like` - Causes the User (in the path) to like the specified Tweet
* `users_id_liked_tweets` - Returns Tweet objects liked by the provided User ID
* `users_id_mentions` - User mention timeline by User ID
* `users_id_retweets` - Causes the User (in the path) to retweet the specified Tweet.
* `users_id_timeline` - User home timeline by User ID
* `users_id_tweets` - User Tweets timeline by User ID
* `users_id_unlike` - Causes the User (in the path) to unlike the specified Tweet
* `users_id_unretweets` - Causes the User (in the path) to unretweet the specified Tweet

### Users

* `find_my_user` - User lookup me
* `find_user_by_id` - User lookup by ID
* `find_user_by_username` - User lookup by username
* `find_users_by_id` - User lookup by IDs
* `find_users_by_username` - User lookup by usernames
* `list_get_followers` - Returns User objects that follow a List by the provided List ID
* `list_get_members` - Returns User objects that are members of a List by the provided List ID.
* `tweets_id_liking_users` - Returns User objects that have liked the provided Tweet ID
* `tweets_id_retweeting_users` - Returns User objects that have retweeted the provided Tweet ID
* `users_id_block` - Block User by User ID
* `users_id_blocking` - Returns User objects that are blocked by provided User ID
* `users_id_follow` - Follow User
* `users_id_followers` - Followers by User ID
* `users_id_following` - Following by User ID
* `users_id_mute` - Mute User by User ID.
* `users_id_muting` - Returns User objects that are muted by the provided User ID
* `users_id_unblock` - Unblock User by User ID
* `users_id_unfollow` - Unfollow User
* `users_id_unmute` - Unmute User by User ID

<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
