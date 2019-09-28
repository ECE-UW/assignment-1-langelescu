from __future__ import print_function

import sys
import re

from cmdparser import CmdParser

def main():

    cmdparser = CmdParser()
    database = {}

    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
            
            try:
                command = cmdparser.parse(line)
                status, msg, _ = command.execute(database)
            
            except Exception as e:
                print (e, file=sys.stderr)

        except KeyboardInterrupt:
            sys.exit(-1) 

    sys.exit(0)

if __name__ == '__main__':
    main()
