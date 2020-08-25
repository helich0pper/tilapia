#/bin/bash
which apache2
if [[ $? != 0 ]]
	then
		apt install apache2
		apt install php libapache2-mod-php
		systemctl restart apache2
fi
which tar
if [[ $? != 0 ]]
	then
		apt install tar
fi

tar -xzvf templates.tar.gz
if test -d "www"
then
	:
else
	mkdir www
fi
rm -f templates.tar.gz
chown -R $USER:$USER *
chmod a+rwx shell/*
echo Done.
