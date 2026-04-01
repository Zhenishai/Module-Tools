#!/bin/bash

set -euo pipefail
grep -i -v "Hello" dialogue.txt
# TODO: Write a command to output every line in dialogue.txt that does not contain the word "Hello" (regardless of case).
# The output should contain 10 lines.
