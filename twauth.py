import tweepy


class TwitterAuth():
    def __init__(self):
        self.twitter_app_auth = {}
        with open(".config.py") as f:
            code = compile(f.read(), ".config.py", 'exec')
            exec(code, self.twitter_app_auth)

    def auth(self):
        return self.twitter_app_auth

    def api(self):
        taa = self.auth()
        auth = tweepy.OAuthHandler(taa['consumer_key'], taa['consumer_secret'])
        auth.set_access_token(taa['access_token'], taa['access_token_secret'])
        return tweepy.API(auth)
