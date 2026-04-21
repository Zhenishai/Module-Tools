import argparse
import cowsay

animals = cowsay.char_names

parser = argparse.ArgumentParser(
    prog="cowsay",
    description="Make animals say things"
)

parser.add_argument(
    "message",
    nargs="+",
    help="The message to say."
)

parser.add_argument(
    "--animal",
    choices=animals,
    default="cow",
    help="The animal to be saying things."
)

args = parser.parse_args()

text = " ".join(args.message)

getattr(cowsay, args.animal)(text)