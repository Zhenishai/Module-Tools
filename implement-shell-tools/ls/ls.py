import argparse
import os
import sys

parser = argparse.ArgumentParser(prog="ls")

parser.add_argument("-1", action="store_true", help="List one file per line")
parser.add_argument("-a", action="store_true", help="Include hidden files")
parser.add_argument("path", nargs="?", default=".", help="Directory path")

args = parser.parse_args()

try:
    items = os.listdir(args.path)

    if not args.a:
        items = [item for item in items if not item.startswith(".")]

    items.sort()

    if args.__dict__["1"]:
        for item in items:
            print(item)
    else:
        print("  ".join(items))

except FileNotFoundError:
    print(f"ls: cannot access '{args.path}': No such file or directory", file=sys.stderr)


#test:python3 ls.py -1
#specific:python3 ls.py -1 sample-files
#hidden:python3 ls.py -1 -a sample-files
