#!/bin/bash

main () {
  acronym=""
  IFS+="-_*"
  
  for word in $1; do
    acronym+="${word:0:1}"
  done

  echo $acronym | tr '[:lower:]' '[:upper:]'
}

main "$@"