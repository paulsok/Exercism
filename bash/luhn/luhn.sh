#!/bin/bash

main () {
    input="${1//[[:space:]]/}"
	
	if [[ ! $input =~ ^[0-9]{2,}$ ]]; then
		echo "false"
	else
		state=1
		sum=0

		for (( i = ${#input} - 1; i >= 0; i-- )); do
			digit=${input:i:1}
			if (( state <= 0 )); then
				(( digit *= 2 ))
				(( digit >= 10 )) && (( digit -= 9 ))
			fi
			(( sum += digit ))
			(( state *= -1 ))
		done

		if [[ $sum == *0 ]]; then
			echo "true"
		else
			echo "false"
		fi
	fi
}

main "$@"
