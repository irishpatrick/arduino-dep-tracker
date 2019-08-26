#!/usr/bin/python3

import sys
import commands

def parse(argv):
    cmd = argv[1]
    if not commands.exists(cmd):
        print("command does not exist")
        return 1
    flags = []
    opts = []
    for e in argv[2:]:
        if e.startswith("-"):
            flags.append(e)
        else:
            opts.append(e)

    commands.call(cmd, flags, opts)

    return 0

def main(argc, argv):
    if argc < 2:
        commands.call("")
    else:
        parse(argv)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
