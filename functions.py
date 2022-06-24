import json
import time
import subprocess
import os
import csv
from termcolor import colored

lang = "tr"
lang_name = "Turkish"

CLEAR_FUNCTION = "clear"


def clear():
    subprocess.run(CLEAR_FUNCTION, shell=True)


def settings(tp="load", set_dict=[]):
    if tp == "save":
        with open("settings.json", "w") as f:
            json.dump(set_dict, f, indent=4)
    elif tp == "load":
        with open("settings.json", "r") as f:
            return json.load(f)


def load_words(lang=lang, name="all"):
    if lang == "tr":
        with open(os.getcwd() + f"/languages/tr/{name}.csv", "r") as f:
            csvReader = csv.reader(f)

            fields = next(csvReader)
            rows = []

            for row in csvReader:
                rows.append(row)
            
            return rows, fields
    elif lang == "de":
        with open(os.getcwd() + f"/languages/de/{name}.csv", "r") as f:
            csvReader = csv.reader(f)

            fields = next(csvReader)
            rows = []

            for row in csvReader:
                rows.append(row)
            
            return rows, fields


def learn_words():
    global lang
    global lang_name
    q = 0
    name = ""
    settings_file = settings("load")

    if settings_file["def_lang"] == "tr":
        lang = "tr"
        lang_name = "Turkish"
    elif settings_file["def_lang"] == "de":
        lang = "de"
        lang_name = "German"
    else:
        print("Select language:")
        print("1. Turkish")
        print("2. German")

        while True:
            usrinput = input(colored(" ==> ", "cyan")).lower()

            if usrinput == "1" or usrinput == "turkish":
                lang = "tr"
                lang_name = "Turkish"
                break
            elif usrinput == "2" or usrinput == "german":
                lang = "de"
                lang_name = "german"
                break
            elif usrinput == "clear":
                clear()
                print("Select language:")
                print("1. Turkish")
                print("2. German")
            elif usrinput == "exit":
                q = 1

                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid option.")

        if q == 1:
            return

    if lang == "tr":
        print("Choose a category: ")
        print("1. All words")
        print("2. Colours")
        print("3. Days")
        print("4. Food")
        print("5. Months")
        print("6. Numbers")
        print("7. Numbers (extended)")

        while True:
            usrinput = input(colored(" ==> ", "cyan")).lower()

            if usrinput == "1":
                name = "all"
                break
            elif usrinput == "2":
                name = "colours"
                break
            elif usrinput == "3":
                name = "days"
                break
            elif usrinput == "4":
                name = "food"
                break
            elif usrinput == "5":
                name = "months"
                break
            elif usrinput == "6":
                name = "numbers"
                break
            elif usrinput == "7":
                name = "numbers_full"
                break
            elif usrinput == "clear":
                clear()
                print("Select language:")
                print("1. Turkish")
                print("2. German")
            elif usrinput == "exit":
                q = 1

                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid option.")
    elif lang == "de":
        print("Choose a category: ")
        print("1. All words")

        while True:
            usrinput = input(colored(" ==> ", "cyan")).lower()

            if usrinput == "1":
                name = "all"

                break
            elif usrinput == "clear":
                clear()
                print("Select language:")
                print("1. Turkish")
                print("2. German")
            elif usrinput == "exit":
                q = 1

                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid option.")
            
        
        words = load_words(lang, name)

        if q == 1:
            return

    if q == 1:
        return
    

    rows, fields = load_words(lang, name)

    for row in rows:
        word = row[0]
        lword = row[1]
        formal = row[2]
        hint_number = 0
        try_number = 0

        while True:
            print(f"Enter the {lang_name} word for {word}")
            print(colored(" ╰─> ", "cyan"), end="")

            usrinput = input().lower()

            if usrinput == lword.lower():
                print(colored("Correct", "green") + "!")

                break
            elif usrinput == "hint":
                hints = 3

                if len(lword) <= hints:
                    hints = len(lword) - 1
                else:
                    pass


                if hint_number < hints:
                    print(colored("Hint", "magenta") + f": {lword[hint_number]}")
                    hint_number += 1
                else:
                    print("No hints left")
            elif usrinput == "exit":
                q = 1
                break
            else:
                try_number += 1

                if try_number <= 2:
                    print(colored("Incorrect", "red") + ". Try again.")
                else:
                    print(colored("Incorrect", "red") + ". The right answer was: " + colored(lword, "cyan"))
                    break
        
        if q == 1:
            break
        else:
            pass
    
    input("Press ENTER to go back...")


def view_words():
    global lang
    global lang_name
    q = 0
    settings_file = settings("load")

    if settings_file["def_lang"] == "tr":
        lang = "tr"
        lang_name = "Turkish"
    elif settings_file["def_lang"] == "de":
        lang = "de"
        lang_name = "German"
    else:
        print("Select language:")
        print("1. Turkish")
        print("2. German")

        while True:
            usrinput = input(colored(" ==> ", "cyan")).lower()

            if usrinput == "1" or usrinput == "turkish":
                lang = "tr"
                lang_name = "Turkish"
                break
            elif usrinput == "2" or usrinput == "german":
                lang = "de"
                lang_name = "german"
                break
            elif usrinput == "clear":
                clear()
                print("Select language:")
                print("1. Turkish")
                print("2. German")
            elif usrinput == "exit":
                q = 1
                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid option.")
        
        if q == 1:
            return


    if lang == "tr":
        print("Choose a category: ")
        print("1. All words")
        print("2. Colours")
        print("3. Days")
        print("4. Food")
        print("5. Months")
        print("6. Numbers")
        print("7. Numbers (extended)")

        while True:
            usrinput = input(colored(" ==> ", "cyan")).lower()

            if usrinput == "1":
                name = "all"
                break
            elif usrinput == "2":
                name = "colours"
                break
            elif usrinput == "3":
                name = "days"
                break
            elif usrinput == "4":
                name = "food"
                break
            elif usrinput == "5":
                name = "months"
                break
            elif usrinput == "6":
                name = "numbers"
                break
            elif usrinput == "7":
                name = "numbers_full"
                break
            elif usrinput == "clear":
                clear()
                print("Select language:")
                print("1. Turkish")
            elif usrinput == "exit":
                q = 1
                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid option.")
            
        
            words = load_words(lang, name)

        if q == 1:
            return
    elif lang == "de":
        print("Choose a category: ")
        print("1. All words")

        while True:
            usrinput = input(colored(" ==> ", "cyan")).lower()

            if usrinput == "1":
                name = "all"

                break
            
            elif usrinput == "clear":
                clear()
                print("Select language:")
                print("1. Turkish")
                print("2. German")
            elif usrinput == "exit":
                q = 1

                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid option.")
            
        if q == 1:
            return

    rows, fields = load_words(lang, name)

    i = 0
    for row in rows:
        print(colored(i + 1, "green") + ".", colored(row[0], "blue"), "-", colored(row[1], "cyan"))

        i += 1

    input("Press ENTER to go back...")


def settings_change():
    settings_file = settings("load")

    print(colored("Settings", "magenta"))
    print("1. Change default language")


    while True:
        usrinput = input(colored(" ==> ", "cyan"))

        if usrinput == "1" or usrinput == "":
            print("Enter your preferred language")
            usrinput = input(colored("  ==> ", "cyan")).lower()

            if usrinput == "turkish" or usrinput == "tr":
                settings_file["def_lang"] = "tr"
                print("Successfully changed default language to Turkish (tr).")
                settings("save", settings_file)

                time.sleep(1.5)

                break
            elif usrinput == "german" or usrinput == "de":
                settings_file["def_lang"] = "de"
                print("Successfully changed default language to German (de).")
                settings("save", settings_file)

                time.sleep(1.5)

                break
            elif usrinput == "exit":
                pass
            else:
                print(colored("error", "red") + f": {usrinput}: ivalid language number/name/code.")
        else:
            print(colored("error", "red") + f": {usrinput}: ivalid choice.")


def add_words():
    global lang
    global lang_name
    q = 0
    settings_file = settings("load")

    if settings_file["def_lang"] == "tr":
        lang = "tr"
        lang_name = "Turkish"
    elif settings_file["def_lang"] == "tr":
        lang = "de"
        lang_name = "German"
    
    print("Select language:")
    print("1. Turkish")
    print("2. German")

    while True:
        usrinput = input(colored(" ==> ", "cyan")).lower()

        if usrinput == "1" or usrinput == "turkish":
            lang = "tr"
            lang_name = "Turkish"
            break
        elif usrinput == "2" or usrinput == "german":
            lang = "de"
            lang_name = "german"
            break
        elif usrinput == "clear":
            clear()
            print("Select language:")
            print("1. Turkish")
            print("2. German")
        elif usrinput == "exit":
            q = 1

            break
        else:
            print(colored("error", "red") + f": {usrinput}: invalid option.")
    
    if q == 1:
        return


    lword = ""
    enword = ""
    formality = 0

    if lang == "tr":
        print(f"You can add words here without editing the .json files. Just enter an English name, then the {lang_name} counterpart afterwards,")
        print("then the formality: 0 (informal) or 1 (formal). If you spelled a word incorrectly, you can type \"!back\"; it will cancel the process.")

        while True:
            lword = ""
            enword = ""
            formality = 0

            usrinput = input(colored(" en ==> "))
            if usrinput.lower() == "!back":
                break
            else:
                enword = usrinput

            usrinput = input(colored(f" {lang} ==> "))
            if usrinput.lower() == "!back":
                break
            else:
                lword = usrinput

            usrinput = input(colored(f" formality ==> "))
            if usrinput.lower() == "!back":
                break
            elif usrinput == "0":
                formality = 0
                break
            elif usrinput == "1":
                formality == 1
                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid input. Only 0 or 1 is acceptable.")
        
        if enword and lword != "":
            print("asdasd")    
    elif lang == "de":
        print(colored("\x1B[3mi\x1B[0m", "green") + f": Enter an English name and then the {lang_name} counterpart afterwards.")
        print(colored("\x1B[3mi\x1B[0m", "green") + ": If you spelled a word incorrectly, you can type \"!back\"; it will cancel the process.")

        while True:
            lword = ""
            enword = ""
            formality = 0

            usrinput = input(colored(" en ==> "))
            if usrinput.lower() == "!back":
                break
            else:
                enword = usrinput
            usrinput = input(colored(f" {lang} ==> "))
            if usrinput.lower() == "!back":
                break
            else:
                lword = usrinput
                break

            usrinput = input(colored(f" formality ==> "))
            if usrinput.lower() == "!back":
                break
            elif usrinput == "0":
                formality = 0
                break
            elif usrinput == "1":
                formality == 1
                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid input. Only 0 or 1 is acceptable.")
        
        if enword and lword != "":
            print("asdasd")
        else:
            print(enword, lword, formality)




    if q == 1:
        return