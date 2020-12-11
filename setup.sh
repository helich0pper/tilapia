#/bin/bash
which php
if [[ $? != 0 ]]
	then
		apt install php libapache2-mod-php
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
chmod u+rwx shell/*
chmod u+rw safe.txt
echo Done.
