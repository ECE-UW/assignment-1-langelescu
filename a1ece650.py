import sys
import re

from __future__ import print_function
from cmdparser import CmdParser

def main():

    cmdparser = CmdParser()
    database = {}

    while True:
        line = sys.stdin.readline()
        if not line:
            print ('EOF detected. Exiting...')
            break
        else:
            try:
                command = cmdparser.parse(line)
                status, msg, _ = command.execute(database)
            except Exception as e:
                print (e, file=sys.stderr)

    sys.exit(0)

if __name__ == '__main__':
    main()
