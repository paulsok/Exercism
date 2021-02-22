#!/bin/bash

main () {
plain='abcdefghijklmnopqrstuvwxyz'
cipher='zyxwvutsrqponmlkjihgfedcba'

if [[ $1 -eq 'encode' ]]; then
    echo ${@:2} | tr "[:upper:]" "[:lower:]" | tr -d "[:space:].,"  | tr $plain $cipher

elif [[ $1 -eq 'decode' ]]; then
    echo ${@:2} | tr -d "[:space:].," | tr $plain $cipher
fi
}

main "$@"