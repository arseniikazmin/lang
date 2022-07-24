import json
import time
import subprocess
import os
import csv
from termcolor import colored


# const
articles_list= "das", "die", "der", "el", "la", "lo", "los", "las"

lang = "es"
lang_name = "Spanish"


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
    with open(os.getcwd() + f"/languages/{lang}/{name}.csv", "r") as f:
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
    elif settings_file["def_lang"] == "es":
        lang = "es"
        lang_name = "Spanish"
    else:
        print("Select language:")
        print("1. Turkish")
        print("2. German")
        print("3. Spanish")

        while True:
            usrinput = input(colored(" ==> ", "cyan")).lower()

            if usrinput == "1" or usrinput == "turkish":
                lang = "tr"
                lang_name = "Turkish"
                break
            elif usrinput == "2" or usrinput == "german":
                lang = "de"
                lang_name = "German"
                break
            elif usrinput == "3" or usrinput == "spanish":
                lang = "es"
                lang_name = "Spanish"
                break
            elif usrinput == "clear":
                clear()
                print("Select language:")
                print("1. Turkish")
                print("2. German")
                print("3. Spanish")
            elif usrinput == "exit":
                q = 1

                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid option.")

        if q == 1:
            return

    if lang in ["tr", "de", "es"]:
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
                print("3. Spanish")
            elif usrinput == "exit":
                q = 1

                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid option.")
            
        if q == 1:
            return
        
        words = load_words(lang, name)

    if q == 1:
        return

    rows, fields = load_words(lang, name)

    for row in rows:
        word = row[0]
        lword = row[1]
        formal = row[2]
        article = row[3]
        articles = settings_file["grammatical_articles"]
        hint_number = 0
        try_number = 0
        formality = ""

        if formal == "0":
            formality = "no"
        elif formal == "1":
            formality = "yes"
        elif formal == "1":
            formality = "no"

        while True:
            if formal != "2":
                if articles == True:
                    print(f"Enter the {lang_name} word for " + colored(word, "magenta") + " with the proper grammatical article. Formal?: " + colored(formality, "cyan"))
                else:
                    print(f"Enter the {lang_name} word for " + colored(word, "magenta") + ". Formal?: " + colored(formality, "cyan"))
            else:
                if articles == True:
                    print(f"Enter the {lang_name} word for " + colored(word, "magenta") + " with the proper grammatical article.")
                else:
                    print(f"Enter the {lang_name} word for " + colored(word, "magenta") + ".")

            print(colored(" ╰─> ", "cyan"), end="")

            usrinput = input().lower()

            if article not in articles_list:
                articles = False

            if True:
                if articles == True and usrinput != "hint" and usrinput != "exit":
                    if usrinput == article + " " + lword.lower():
                        print(colored("Correct", "green") + "!")
                        break
                    else:
                        try_number += 1

                        if try_number <= 2:
                            print(colored("Incorrect", "red") + ". Try again.")
                        else:
                            print(colored("Incorrect", "red") + ". The right answer was: " + colored(article, "cyan"), colored(lword, "cyan"))
                            break
                elif articles != False and usrinput != "hint" and usrinput != "exit":
                    if usrinput == lword.lower():
                        print(colored("Correct", "green") + "!")
                        break
                    else:
                        try_number += 1

                        if try_number <= 2:
                            print(colored("Incorrect", "red") + ". Try again.")
                        else:
                            print(colored("Incorrect", "red") + ". The right answer was: " + colored(article, "cyan"), colored(lword, "cyan"))
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
                    print("what")
            else:
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
    elif settings_file["def_lang"] == "es":
        lang = "es"
        lang_name = "Spanish"
    else:
        print("Select language:")
        print("1. Turkish")
        print("2. German")
        print("3. Spanish")

        while True:
            usrinput = input(colored(" ==> ", "cyan")).lower()

            if usrinput == "1" or usrinput == "turkish":
                lang = "tr"
                lang_name = "Turkish"
                break
            elif usrinput == "2" or usrinput == "german":
                lang = "de"
                lang_name = "German"
                break
            elif usrinput == "2" or usrinput == "spanish":
                lang = "es"
                lang_name = "Spanish"
                break
            elif usrinput == "clear":
                clear()
                print("Select language:")
                print("1. Turkish")
                print("2. German")
                print("3. Spanish")
            elif usrinput == "exit":
                q = 1
                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid option.")
        
        if q == 1:
            return


    if lang in ["tr", "de", "es"]:
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
                print("3. Spanish")
            elif usrinput == "exit":
                q = 1
                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid option.")
            
        
            words = load_words(lang, name)

        if q == 1:
            return

    rows, fields = load_words(lang, name)
    articles = settings_file["grammatical_articles"]

    i = 0
    for row in rows:
        article = row[3]

        if articles == True:
            if article != "none":
                print(colored(i + 1, "green") + ".", colored(row[0], "blue"), "-", colored(row[3], "cyan"), colored(row[1], "cyan"))
            else:
                print(colored(i + 1, "green") + ".", colored(row[0], "blue"), "-", colored(row[1], "cyan"))
        else:
            print(colored(i + 1, "green") + ".", colored(row[0], "blue"), "-", colored(row[1], "cyan"))

        i += 1

    input("Press ENTER to go back...")


def add_words():
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
    elif settings_file["def_lang"] == "es":
        lang = "es"
        lang_name = "Spanish"
    
    print("Select language:")
    print("1. Turkish")
    print("2. German")
    print("3. Spanish")

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
        elif usrinput == "3" or usrinput == "spanish":
            lang = "es"
            lang_name = "spanish"
            break
        elif usrinput == "clear":
            clear()
            print("Select language:")
            print("1. Turkish")
            print("2. German")
            print("3. Spanish")
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

    if lang in ["tr", "de", "es"]:
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

            usrinput = input(colored(f" formality ==> "))
            if usrinput.lower() == "!back":
                break
            elif usrinput == "0":
                formality = 0
                break
            elif usrinput == "1":
                formality == 1
                break
            elif usrinput == "2":
                formality == 1
                break
            else:
                print(colored("error", "red") + f": {usrinput}: invalid input. Only 0, 1 and 2 are acceptable.")
        
        if enword and lword != "":
            print("asdasd")
        else:
            print(enword, lword, formality)

    if q == 1:
        return

def settings_change():
    settings_file = settings("load")

    print(colored("Settings", "magenta"))
    print("1. Change default language")
    print("2. Toggle formality on/off (showing if the word is formal or not)")
    print("3. Toggle articles on/off")


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
            elif usrinput == "spanish" or usrinput == "es":
                settings_file["def_lang"] = "es"
                print("Successfully changed default language to Spanish (es).")
                settings("save", settings_file)

                time.sleep(1.5)

                break
            elif usrinput == "exit":
                pass
            else:
                print(colored("error", "red") + f": {usrinput}: ivalid language number/name/code.")
        elif usrinput == "2":
            t = 0

            if settings_file["formality"] == False:
                print("This feature is turned off. Turn it on? [Y/n] ", end="")
                t = 1
            else:
                print("This feature is turned on. Turn it off? [Y/n] ", end="")

            usrinput = input()

            if usrinput == "" or usrinput == "y" or usrinput == "yes":
                if t == 0:
                    settings_file["formality"] = False
                else:
                    settings_file["formality"] = True

                print("Successfully changed to " + colored(settings_file["formality"], "cyan") + ".")
            else:
                pass
        elif usrinput == "3":
            t = 0

            if settings_file["grammatical_articles"] == False:
                print("This feature is turned off. Turn it on? [Y/n] ", end="")
                t = 1
            else:
                print("This feature is turned on. Turn it off? [Y/n] ", end="")

            usrinput = input()

            if usrinput == "" or usrinput == "y" or usrinput == "yes":
                if t == 0:
                    settings_file["grammatical_articles"] = False
                else:
                    settings_file["grammatical_articles"] = True
            else:
                pass
            
            settings("save", settings_file)
            print("Successfully changed to " + colored(settings_file["grammatical_articles"], "cyan") + ".")
        elif usrinput == "exit":
            break
        else:
            print(colored("error", "red") + f": {usrinput}: ivalid choice.")

