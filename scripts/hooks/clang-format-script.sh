#!/bin/sh
command -v clang-format >/dev/null 2>&1 || { echo >&2 "clang-format is not installed. Aborting."; exit 1; }
for file in "$@"
do
  echo "Formatting $file"
  clang-format -i -style=file "$file"
done
