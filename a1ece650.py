import sys
import re

from cmdparser import CmdParser


def main():

    while True:
        line = sys.stdin.readline()
        if not line:
            print 'EOF detected. Exiting...'
            break

    sys.exit(0)

if __name__ == '__main__':
    main()
