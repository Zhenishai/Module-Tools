#!/bin/bash

set -euo pipefail

awk '{print $1}' scores-table.txt

# TODO: Write a command to output just the names of each player in `scores-table.txt`.
# Your output should contain 6 lines, each with just one word on it.
