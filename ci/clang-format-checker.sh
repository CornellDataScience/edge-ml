#!/usr/bin/env python

## Open all modified files in the current branch and run clang-format on them.
import subprocess

# Get the list of modified files. from git
modified_files = subprocess.check_output(
    "find src/ -iname *.h -o -iname *.cpp",
    shell=True,
).splitlines()

# convert to list of strings
modified_files = [f.decode("utf-8") for f in modified_files]

for f in modified_files:
  result = subprocess.run(["clang-format", "--dry-run", "--Werror", f])
  if result.returncode:
    exit(1)