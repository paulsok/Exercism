#!/bin/bash

main () {
hamming_distance=0
var1=$1
var2=$2

if (( $# != 2 )); then
    echo "Usage: hamming.sh <string1> <string2>"
    return 1
fi
if (( ${#var1} != ${#var2} )); then
    echo "left and right strands must be of equal length"
    return 1
fi

for (( i=0; i<${#var1}; i++ )); do
    if [[ "${var1:$i:1}" != "${var2:$i:1}" ]]; then
            (( hamming_distance++ ))
    fi
done

echo $hamming_distance
}

main "$@"
