# Extract twitter user ids which contain the target hashtags over a period of time.

from util import *

tweet_ctr = 0
matched_within_dates_ctr = 0
unique_users = set()


def twparser(status):
    # status -- see: https://dev.twitter.com/overview/api/tweets

    # TODO - filter by:
    # - date
    # - bot?
    global tweet_ctr, matched_within_dates_ctr, unique_users

    from_date = datetime(2016, 9, 7)
    to_date = datetime(2016, 9, 8)
    tw_created_at = status.created_at ## type = datetime
    if from_date <= tw_created_at <= to_date:
        matched_within_dates_ctr += 1

    tw_user_id = status.user.id_str
    unique_users.add(tw_user_id)

    # dump regardless of date
    print(status._json)

    tweet_ctr += 1
    if tweet_ctr % 1000 == 0:
        printerr_ts("Tweets found: {:,d}".format(tweet_ctr))
        printerr_ts("Unique users within: {:,d}".format(len(unique_users)))
        printerr_ts("Tweets within the targeted date range: {:,d}".format(matched_within_dates_ctr))
        printerr_ts("Last visited twitter status was posted on %s." % tw_created_at.strftime("%x %X"))
        printerr("-------------------")


def test_twitter():
    import twstream

    stream = twstream.stream(twparser)

    import hashtags as ht
    target_hashtags = ht.get_pro_trump().union(ht.get_pro_hillary())
    printerr_ts("Streaming of tweets started...")
    stream.filter(track=target_hashtags)


if __name__ == '__main__':
    test_twitter()
