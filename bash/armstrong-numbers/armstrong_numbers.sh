#!/bin/bash

main () {
length=${#1}
sum=0

for (( i = 0; i < length; i++ ))
    do
	    (( sum += ${1:i:1} ** length ))
	done

(( sum == $1 )) && echo true || echo false
}

main "$@"