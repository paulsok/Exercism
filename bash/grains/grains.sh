#!/bin/bash

main () {
    if [[ $1 -gt 0 && $1 -le 64 ]]; then
        bc <<< "2^$(( $1-1 ))"
    elif [[ $1 == total ]]; then 
        bc <<< "2^64 -1"
    else
        echo "Error: invalid input"; exit 1
    fi
}

main "$@"
