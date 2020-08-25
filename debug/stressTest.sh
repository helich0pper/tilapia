#!/bin/bash

#TEST HOW MANY REQUESTS YOUR SITE CAN HANDLE


if [ -z $1 ]
then
	echo "You did not add a URL to test. Do:\n test.sh <URL>"
else
	req=1;
	while true
	do
		curl -q -u hello@anything.com:helichopper $1/login.php
		echo Request: $req
	   	req=$(($req+1))	
	done
fi

