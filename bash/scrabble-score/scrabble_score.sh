#!/bin/bash

main () {
shopt -s nocasematch
sum=0

for (( i = 0; i < ${#1}; i++ )) 
do
  [[ "${1:i:1}" =~ [AEIOULNRST] ]] && (( sum+=1 ))
  [[ "${1:i:1}" =~ [DG] ]] && (( sum+=2 ))
  [[ "${1:i:1}" =~ [BCMP] ]] && (( sum+=3 ))
  [[ "${1:i:1}" =~ [FHVWY] ]] && (( sum+=4 ))
  [[ "${1:i:1}" =~ [K] ]] && (( sum+=5 ))
  [[ "${1:i:1}" =~ [JX] ]] && (( sum+=8 ))
  [[ "${1:i:1}" =~ [QZ] ]] && (( sum+=10 ))
done

echo $sum
}

main "$@"
