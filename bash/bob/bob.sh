#!/bin/bash
is_question () {
  [[ $message =~ .*\?\ *$ ]]
}

is_yell () {
  [[ $message =~ ^[^a-z]*$ && $message =~ [A-Z]+ ]]
}

is_nothing () {
  [[ $message =~ ^[^a-zA-Z0-9]*$ ]]
}

main () {

  message=$1

  if is_question && is_yell
  then
    echo "Calm down, I know what I'm doing!"

  elif is_question
  then
    echo "Sure."
  
  elif is_yell
  then
    echo "Whoa, chill out!"

  elif is_nothing
  then
    echo "Fine. Be that way!"

  else
    echo "Whatever."
  fi
}

main "$@"
