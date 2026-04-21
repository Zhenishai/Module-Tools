import argparse
import glob
import sys

parser = argparse.ArgumentParser(prog="cat")

parser.add_argument("-n", action="store_true", help="Number all lines")
parser.add_argument("-b", action="store_true", help="Number non-empty lines")
parser.add_argument("files", nargs="+", help="Files to read")

args = parser.parse_args()

file_list = []
for pattern in args.files:
    matches = glob.glob(pattern)
    if matches:
        file_list.extend(matches)
    else:
        file_list.append(pattern)

line_number = 1

for filename in file_list:
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.rstrip("\n")

                if args.b:
                    if line.strip() != "":
                        print(f"{line_number:6}\t{line}")
                        line_number += 1
                    else:
                        print()
                elif args.n:
                    print(f"{line_number:6}\t{line}")
                    line_number += 1
                else:
                    print(line)

    except FileNotFoundError:
        print(f"cat: {filename}: No such file or directory", file=sys.stderr)

#run to test: python3 cat.py sample-files/1.txt
#run all numbers:python3 cat.py -n sample-files/1.txt
#multiple files: python3 cat.py sample-files/*.txt
#number non empty: python3 cat.py -b sample-files/3.txt