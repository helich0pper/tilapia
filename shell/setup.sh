str=$(cat shell/config.yml)
echo authtoken: $str > shell/ngrok.yml
echo web_addr: 4444 >> shell/ngrok.yml
