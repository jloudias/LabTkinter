#!/usr/bin/python
import os
import sys
import time

EXIT_LOGO = """
   _____                 _ _
  / ____|               | | |
 | |  __  ___   ___   __| | |__  _   _  ___
 | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \ 
 | |__| | (_) | (_) | (_| | |_) | |_| |  __/
  \_____|\___/ \___/ \__,_|_.__/ \__, |\___|
                                  __/ |
                                 |___/
"""
# Constants
# ---------
WIDTH = 30
SITEDIR = "/var/www/html/"
OPTIONS = {
    "1": "Update System",
    "2": "Start LAMP",
    "3": "Stop LAMP",
    "4": "Update LAMP permissions",
    "9": "Shutdown Computer",
    "0": "Exit Application",
}
WEB_USER = 'www-data'
WEB_GROUP = 'dev'

def show_menu():
    print(f"+{'-'*WIDTH}+")
    print(f"|{'UTILITIES':^{WIDTH}}|")
    print(f"+{'-' *WIDTH}+")
    for k, v in OPTIONS.items():
        print(f"|{f' {k} - {v}':{WIDTH}}|")
    print(f"+{'-' *WIDTH}+")
    print("Enter your option: ")


def update_system():
    LINE=40
    print(f"{'='*LINE}\n*** The system is updating... ***\n{'='*LINE}\n")
    try:
        if os.system("sudo apt update 2>/dev/null") != 0:
            raise Exception("Command <update> failed.")
        elif os.system("sudo apt -y upgrade 2>/dev/null") != 0:
            raise Exception("Command <upgrade> failed.")
        elif os.system("sudo apt autoclean 2>/dev/null") != 0:
            raise Exception("Command <autoclean> failed.")
        elif os.system("sudo apt autoremove 2>/dev/null") != 0:
            raise Exception("Command <autoremove> failed.")
    except Exception as e:
        print(f"\n{'='*LINE}\nERROR! {e}\n{'='*LINE}")
    else:
        print(f"\n{'='*LINE}\nSUCCESS! System updated,cache cleaned.\n{'='*LINE}")
    finally:
        p = input("\nPress any key...")

def update_web_permissions():           
    if not os.system(f"chown -R {WEB_USER}.{WEB_GROUP} {SITEDIR}"):
        print("\nOwner and Group configured.")
        if not os.system(f"chmod -R 2775 {SITEDIR}"):
            print("File permissions configured.")
            print("-" * 30)
            print(f"Directory: {SITEDIR}")
            os.system(f"ls -l {SITEDIR}")
        else:
            print(f"\n{'='*30}Error setting up file's permissions.\n{'='*30}")
    else:
        print("Error setting up owner and group!")
    answer = input("\nPress any key to continue...")

def main():
    while True:
        os.system("clear")
        show_menu()
        resp = input("> ")
        if resp == "0":
            os.system("clear")
            sys.exit(EXIT_LOGO)
        elif resp == "1":
            update_system()
        elif resp == "2":
            os.system("/usr/local/bin/lamp.sh start")
        elif resp == "3":
            os.system("/usr/local/bin/lamp.sh stop")
        elif resp == "4":
           update_web_permissions()
        elif resp == "9":
            os.system("shutdown -h now")
        else:
            print("\n>>>>>  Invalid option! Try again.  <<<<<")
            time.sleep(1)
            continue


if __name__ == "__main__":
    if os.geteuid() != 0:
        sys.exit("You must be root!")
    else:
        main()
