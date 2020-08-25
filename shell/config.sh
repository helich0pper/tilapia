echo Starting server...
chmod 766 www/user.txt
service apache2 start
mount -o bind www/ /var/www/html
echo  > www/user.txt
echo Forwarding URL...
ng="ng"
if [ $1 = "ng" ]
then
  echo  > shell/tunnel.json
  killall -q ngrok
  shell/ngrok http 80 -config=shell/ngrok.yml >/dev/null &
else
  killall -q loclx
  shell/loclx tunnel http --to 127.0.0.1:80 --subdomain $1 >/dev/null &
fi
