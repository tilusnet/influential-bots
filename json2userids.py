import sys
import json

assert len(sys.argv) == 4

def opt_way():
    try:
        posting_users, retweeted_users = [
            (e['user']['screen_name'],
             # e['retweeted_status']['user']['screen_name'] if 'retweeted_status' in e else " ") for e in d]
             " ") for e in d]
    except ValueError as e:
        print(d)
        raise e


d = json.load(open(sys.argv[1]))
posting_users = []
retweeted_users = []
for e in d:
    posting_users.append(e['user']['screen_name'])
    retweeted_users.append(e['retweeted_status']['user']['screen_name'] if 'retweeted_status' in e else " ")

with open(sys.argv[2], 'w') as f:
    for username in set(posting_users):
        print(username, file=f)

with open(sys.argv[3], 'w') as f:
    for username in set(retweeted_users):
        print(username, file=f)
