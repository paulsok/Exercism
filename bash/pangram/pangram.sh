#!/bin/bash

main () {
string="$(echo "$1" | tr '[:upper:]' '[:lower:]')"

for char in {a..z}; do
  if [[ "$string" != *$char* ]]; then
    echo false
    exit
  fi
done

echo true
}

main "$@"