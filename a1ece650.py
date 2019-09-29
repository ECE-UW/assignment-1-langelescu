
import sys

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
                has_out, out = command.execute(database)
                if has_out:
                    sys.stdout.write(out)

            except Exception as e:
                sys.stderr.write(str(e) + "\n")

        except KeyboardInterrupt:
            sys.exit(-1)

    sys.exit(0)


if __name__ == '__main__':
    main()
