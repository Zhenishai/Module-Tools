import argparse
import glob
import sys

parser = argparse.ArgumentParser(prog="wc")

parser.add_argument("-l", action="store_true", help="Count lines")
parser.add_argument("-w", action="store_true", help="Count words")
parser.add_argument("-c", action="store_true", help="Count bytes")
parser.add_argument("files", nargs="+", help="Files to read")

args = parser.parse_args()

file_list = []
for pattern in args.files:
    matches = glob.glob(pattern)
    if matches:
        file_list.extend(matches)
    else:
        file_list.append(pattern)

def count_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            lines = content.count("\n")
            words = len(content.split())
            chars = len(content)

            return lines, words, chars

    except FileNotFoundError:
        print(f"wc: {filename}: No such file or directory", file=sys.stderr)
        return None

totals = [0, 0, 0]
results = []

for file in file_list:
    counts = count_file(file)
    if counts:
        results.append((file, counts))
        totals = [totals[i] + counts[i] for i in range(3)]

def format_output(counts):
    l, w, c = counts

    if args.l:
        return f"{l}"
    elif args.w:
        return f"{w}"
    elif args.c:
        return f"{c}"
    else:
        return f"{l:7} {w:7} {c:7}"

for file, counts in results:
    print(f"{format_output(counts)} {file}")

if len(results) > 1:
    print(f"{format_output(totals)} total")

#python3 wc.py sample-files/*
#lines only python3 wc.py -l sample-files/3.txt
#words only: python3 wc.py -w sample-files/3.txt
#characters:python3 wc.py -c sample-files/3.txt
#multiplefiles:python3 wc.py -l sample-files/*