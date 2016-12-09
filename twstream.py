import tweepy
import twauth


class InfluentialStreamListener(tweepy.StreamListener):

    def __init__(self, callback=None):
        super().__init__()
        self.callback = callback


    def on_status(self, status):
        # status === the tweet itself
        # see: https://dev.twitter.com/overview/api/tweets
        if self.callback:
            self.callback(status)


    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


def stream(callback=None):
    return tweepy.Stream(auth=twauth.TwitterAuth().api().auth,
                         listener=InfluentialStreamListener(callback))
