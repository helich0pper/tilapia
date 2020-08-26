#!/usr/bin/python3
from os import system
from py.mens import *
from py.pages import *
from py.files import *
from py.nav import *
# Main
if os.geteuid() == 0:
    os.system("clear")
    os.system("chmod a+rwx shell/*")
    try:
        start()
    except (KeyboardInterrupt):
        pass
    os.system("shell/close.sh")
else:
    showTitle()
    print(colored("Please run this tool as root to avoid errors!", "red"))
exit()
