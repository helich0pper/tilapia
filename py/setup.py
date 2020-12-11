#!usr/bin/env python3
import os
import time
from termcolor import colored
from .mens import showTitle
####CONFIG######################################################################
def fsetup():
    showTitle();
    print(colored('Ngrok\n', 'red'), "Please sign up or log in to avoid unexpected server crashes");
    print(" You can do that here: ", end="");
    print(colored("https://dashboard.ngrok.com/login", "blue"));
    print(" Adding an authtoken can allow 200+ connections. You can skip this step by leaving it blank", colored("but you will be limit to a few connections", "red"), end="\n\n");
    print(" You will be given an authtoken, paste it here [MAKE SURE IT IS CORRECT]: ", end="");
    auth = str(input());
    os.system("touch shell/config.yml");
    os.system("chmod a+rw shell/config.yml");
    with open("shell/config.yml", "w") as config:
        config.write(auth);
        config.close();
    os.system("shell/setup.sh");
    valid = open("shell/valid.txt", "w");
    val = False;
    if auth == "":
        print(colored("\nYou did not add an authtoken!\nWe will remind you next time", "red"));
        time.sleep(3);
    else:
        print(colored("\nSuccess!\nYou can change your authtoken in the main menu", "green"));
        time.sleep(3);
        val = True;
    if val == True:
        valid.truncate();
        valid.write("1");
    valid.close();
    os.system("clear");

def setup():
    print("\nIf you do not have an account or want to retrieve your authtoken go here: ", end="");
    print(colored("https://dashboard.ngrok.com/login", "blue"));
    print("\nTake your time!");
    print("Enter authtoken here (leave blank to do this later): ", end="");
    auth = str(input());
    if auth == "":
        print(colored("\nYou did not add an authtoken!\nYou can back and do it later", "red"));
        time.sleep(3);
    else:
        with open("shell/config.yml", "w") as config:
            config.write(auth);
            config.close();
        os.system("shell/setup.sh");
        print(colored("\nAuthtoken updated!", "green"));
        time.sleep(3);

def checkval():
    valid = open("shell/valid.txt");
    val = valid.read();
    valid.close();
    if "1" in val:
        return True;
    else:
        return False;
