import subprocess
import time
import json
import os
import functions

try:
	from termcolor import colored
except:
    print("Termcolor module not installed. Installing...")
    time.sleep(0.5)
    subprocess.run("pip3 install termcolor", shell=True)
    functions.clear()
    print("Dependencies successfully installed.")
    print("Please restart the program to start using it.")
    exit()

data = []
version = ""
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

with open(DIR_PATH + "/gamefiles/data.json", "r") as f:
    data = json.load(f)
    version = data["version"]

if __name__ == "__main__":
    while True:
        functions.clear()

        print(colored(f" --- lang v{version} ---", "green"))
        print("1. Learn words")
        print("2. View words")
        print("3. Add custom words")
        print("4. Help")
        print("5. Settings")
        print("Type exit to quit.")

        usrinput = input(colored(" ==> ", "cyan"))

        if usrinput == "1":
            functions.learn_words()
        elif usrinput == "2":
            functions.view_words()
        elif usrinput == "3":
            functions.add_words()
        elif usrinput == "4":
            functions.help()
        elif usrinput == "exit" or usrinput == "quit":
            exit()
        elif usrinput == "5":
            functions.settings_change()
        else:
            print(colored("error", "red") + f": {usrinput}: invalid option.")
