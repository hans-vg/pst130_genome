#!/usr/bin/env python

"""A simple python script to convert a delta file to bed file (ignoring indels).
"""

from __future__ import print_function
import os
import sys
import argparse



def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input Delta file", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="Output file", default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    dataDict = dict()
    lines = args.infile.readlines()
    ref = ""
    hit = ""
    for i in range(0, len(lines)):
        line = lines[i].rstrip()
        #print(line)
        if ">" in line:
            line = line.replace(">", "")
            ref = line.split(" ")[0]
            hit = line.split(" ")[1]
            #print(ref, hit)
        elif len(line.split(" ")) > 2:
            start = line.split(" ")[0]
            end = line.split(" ")[1]
            print("%s\t%s\t%s\t%s" % (ref, start, end, hit))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
