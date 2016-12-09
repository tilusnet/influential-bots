
import sys
import json
import ast

assert len(sys.argv) == 3

l = []
with open(sys.argv[1]) as f:
    for line in f:
        d = ast.literal_eval(line)
        l.append(d)
json.dump(l, open(sys.argv[2], 'w'), indent=2)
