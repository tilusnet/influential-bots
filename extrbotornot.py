# Extracts the list of bot-likely twitter users
# Uses the output of qbotornot.py

# e.g. input: botornot_rt.json

import sys
import ast
from util import *


BOT_THRESHOLD = 0.5

# ---

bots = 0
total_entries = 0

assert len(sys.argv) == 4

with open(sys.argv[1], 'rt') as i, \
     open(sys.argv[2], 'w') as o_bot, \
     open(sys.argv[3], 'w') as o_notbot:
    for chunk in i.read().split(sep=']'):
        if not chunk:
            # empty/last entry
            continue
        e = bon_entry = ast.literal_eval(chunk + ']')[1]
        try:
            bon_score = e['score']
            bon_username = e['meta']['screen_name']
            bon_userid = e['meta']['user_id']
        except KeyError as e:
            continue
        entry = '\t'.join([bon_userid, bon_username, str(bon_score)])
        if bon_score >= BOT_THRESHOLD:
            bots += 1
            print(entry, file=o_bot)
        else:
            print(entry, file=o_notbot)
        total_entries += 1
printerr("Bot identifying threshold: %s" % BOT_THRESHOLD)
printerr("Found {:,d} users to be bots out of {:,d}.".format(bots, total_entries))

