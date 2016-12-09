import botornot
import json
import twauth
from dateutil.relativedelta import *
from util import *

assert len(sys.argv) == 3

bon = botornot.BotOrNot(**twauth.TwitterAuth().auth())

start_time = datetime.now()
# Check a sequence of accounts

with open(sys.argv[1]) as f:
    accounts = ['@' + uid for uid in f]
acct_sum = len(accounts)
printerr_ts("Attempting to identify {:,d} twitter users...".format(acct_sum))

with open(sys.argv[2], 'w') as f:
    for i, result in enumerate(bon.check_accounts_in(accounts), start=1):
        # result is a list
        sres = json.dumps(result, indent=2)
        print(sres, file=f, end='\n')
        printerr(sres)
        printerr_ts("-- {:,d} of {:,d} processed. --".format(i, acct_sum))

printerr_ts('Done. Took {}.'.format(str(relativedelta(datetime.now(), start_time))))
