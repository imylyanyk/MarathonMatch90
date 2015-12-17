import sys

_log = True

def log(*objs):
    if _log:
        print("LOG: ", *objs, file=sys.stderr)