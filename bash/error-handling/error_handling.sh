#!/usr/bin/env bash

main() {
    if [[ $# == 1 ]]
    then
        echo "Hello, $*"
        exit 0
    else
        echo "Usage: error_handling.sh <person>"
        exit 1
    fi
}

main "$@"