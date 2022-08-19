#!/usr/bin/bash
i=3
three=3
if [ $(( i % three )) -eq 0 ]
then
	echo "Fizz"
fi
