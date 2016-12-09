# Extract tweets of a list of users.
# input: file with a list of twitter screen_names like that in bots.txt

from util import *
import sys
import twauth
import tweepy

assert len(sys.argv) >= 3

OCT_26_ID = 791274127361323009
NOV_06_ID = 795398620346458113
NOV_10_ID = 796488796921413632

dest = sys.argv[2]
if not dest.endswith('/'):
    dest += '/'

skip_records = int(sys.argv[3]) if (len(sys.argv) > 3) else 0

api = twauth.TwitterAuth().api()
with open(sys.argv[1]) as i:
    entries = i.readlines()
entries = entries[skip_records:]
printerr_ts("About to process tweets of %d users..." % len(entries))
printerr_ts("Streaming of tweets started...")
for i, e in enumerate(entries, start=1):
    tweet_ctr = 0
    userid, username, _ = e.split(sep='\t', maxsplit=2)
    printerr_ts("[%d/%d] Getting tweets of user '%s'..." % (i, len(entries), username))
    with open(dest + username + '.txt', 'w') as fout:
        for status in tweepy.Cursor(api.user_timeline, user_id=userid, since_id=OCT_26_ID, max_id=NOV_10_ID).items():
            print(status._json['text'], file=fout)
            tweet_ctr += 1
    printerr_ts("-- Captured a total of %d tweets for this user. --" % tweet_ctr)
printerr_ts("Done. Check the %s folder." % dest)


