
import sys
from datetime import datetime

def printerr(msg):
    print(msg, file=sys.stderr)


def printerr_ts(msg):
    print("[{}] ".format(datetime.now().strftime("%x %X")) + msg, file=sys.stderr)