#!/bin/bash
gcd () {
m=$1
n=$2
while ((m-n))
do
    if [ $m -gt $n ]
    then
        ((m-=n))
    else
        ((n-=m))
    fi
done
echo "GCD is $m"
}
read m n
while ((m+n))
do
    gcd $m $n
    read m n
done
echo "bye"
