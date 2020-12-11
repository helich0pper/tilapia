#!/bin/bash
echo Starting server...
chmod u+rw www/user.txt
echo  > www/user.txt
php -S 0.0.0.0:8069 -t www/ >& /dev/null &
echo Forwarding URL...
if [ $1 = "ng" ]
then
  echo  > shell/tunnel.json
  killall -q ngrok
  shell/ngrok http 8069 -config=shell/ngrok.yml >/dev/null &
else
  killall -q loclx
  shell/loclx tunnel http --to 127.0.0.1:8069 --subdomain $1 >/dev/null &
fi
