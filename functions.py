import json
import time
import subprocess
import os
import csv
from termcolor import colored


ARTICLES_LIST= "das", "die", "der", "el", "la", "lo", "los", "las"
# The clear() function uses this variable. If you are using Microsoft Windows,
# you should either change it to "cls" or run the script inside a Powershell.
CLEAR_FUNCTION = "clear"
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

print(DIR_PATH)

# the default language is Spanish
lang = "es" # language code
lang_name = "Spanish" # language name


def clear():
    subprocess.run(CLEAR_FUNCTION, shell=True)


def settings(tp="load", set_dict=[]):
    if tp == "save":
        with open(DIR_PATH + "/gamefiles/settings.json", "w") as f:
            json.dump(set_dict, f, indent=4) # wrting to json with indentation 4
    elif tp == "load":
        with open(DIR_PATH + "/gamefiles/settings.json", "r") as f:
            return json.load(f) # returning the loaded settings file


def load_words(lang=lang, name="all"):
    with open(DIR_PATH + f"/languages/{lang}/{name}.csv", "r") as f:
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

    # If there is already a default language set in settings,
    # change the lang_name to the language's name, i.e. "es"
    # will be changed to Spanish.
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

    if lang in ["tr", "de", "es"]: # Technically this should always be executed
        print("Choose a category: ")
        print("1. All words")
        print("2. Colours")
        print("3. Days")
        print("4. Food")
        print("5. Months")
        print("6. Numbers")
        print("7. Numbers (extended)")

        # This asks for user's input and based on what they enter
        # the "name" variable will be changed. It is used for
        # opennig .csv files with all the words.
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
        word = row[0] # The English word
        lword = row[1] # The word in another language the user selected
        # Formality of the word. 0 = informal, 1 = formal, 2 = doesn't
        # matter/can be used in both formal/informal situations
        formal = row[2]
        article = row[3] # Article of the word, i.e.
        articles = settings_file["grammatical_articles"] # Should the user enter grammatical articles? True/False
        hint_number = 0 # How many hints the user has already used. When this reaches 3, the word skips
        try_number = 0 # How many tries the user has made. Has a limit of 3
        formality = "" # 0 = no, 1 = yes

        if formal == "0":
            formality = "no"
        elif formal == "1":
            formality = "yes"
        elif formal == "1":
            formality = "no"

        while True:
            if formal != "2": # If formality doesn't matter
                if articles == True:
                    print(f"Enter the {lang_name} word for " + colored(word, "magenta") + " with the proper grammatical article. Formal?: " + colored(formality, "cyan"))
                else:
                    print(f"Enter the {lang_name} word for " + colored(word, "magenta") + ". Formal?: " + colored(formality, "cyan"))
            else: # If it does
                if articles == True:
                    print(f"Enter the {lang_name} word for " + colored(word, "magenta") + " with the proper grammatical article.")
                else:
                    print(f"Enter the {lang_name} word for " + colored(word, "magenta") + ".")

            print(colored(" ╰─> ", "cyan"), end="")

            usrinput = input().lower()

            if article not in ARTICLES_LIST:
                articles = False

            if True: # idk why I added this
                # If articles are enabled AND the user hasn't tried to use a hint/exit
                if articles == True and usrinput != "hint" and usrinput != "exit":
                    # If the word that the user is article+word, i.e. "el pan"
                    if usrinput == article + " " + lword.lower():
                        print(colored("Correct", "green") + "!")
                        break
                    else:
                        lword = list(lword)

                        for i in range(0, len(lword)):
                            if lword[i].lower() in ["í", "ó", "é", "ä", "ö", "ü", "ß", "ı", "ç", "ş"]:
                                if lword[i].lower() == "í":
                                    lword[i] = "i"
                                elif lword[i].lower() == "ó":
                                    lword[i] = "o"
                                elif lword[i].lower() == "é":
                                    lword[i] = "e"
                                elif lword[i].lower() == "ä":
                                    lword[i] = "a"
                                elif lword[i].lower() == "ü":
                                    lword[i] = "u"
                                elif lword[i].lower() == "ß":
                                    lword[i] = "ss"
                                elif lword[i].lower() == "ı":
                                    lword[i] = "i"
                                elif lword[i].lower() == "ç":
                                    lword[i] = "c"
                                elif lword[i].lower() == "ş":
                                    lword[i] = "s"
                        lword = ''.join(lword)

                        if usrinput == article + " " + lword.lower():
                            print(colored("Correct", "green") + "!")
                            break
                        else:
                            try_number += 1 # Increment try_number by 1

                            if try_number <= 2: # If try_number hasn't reached 3
                                print(colored("Incorrect", "red") + ". Try again.")
                            else: # Else, tell the user the word
                                print(colored("Incorrect", "red") + ". The right answer was: " + colored(article, "cyan"), colored(lword, "cyan"))
                                break
                # If articles are disabled AND the user hasn't tried to use a hint/exit
                elif articles == False and usrinput != "hint" and usrinput != "exit":
                    if usrinput == lword.lower():
                        print(colored("Correct", "green") + "!")
                        break
                    else:
                        lword = list(lword)

                        for i in range(0, len(lword)):
                            if lword[i].lower() in ["í", "ó", "é", "ä", "ö", "ü", "ß", "ı", "ç", "ş",]:
                                if lword[i].lower() == "í":
                                    lword[i] = "i"
                                elif lword[i].lower() == "ó":
                                    lword[i] = "o"
                                elif lword[i].lower() == "é":
                                    lword[i] = "e"
                                elif lword[i].lower() == "ä":
                                    lword[i] = "a"
                                elif lword[i].lower() == "ü":
                                    lword[i] = "u"
                                elif lword[i].lower() == "ß":
                                    lword[i] = "ss"
                                elif lword[i].lower() == "ı": # this is "ı"
                                    lword[i] = "i"
                                elif lword[i].lower() == "ç":
                                    lword[i] = "c"
                                elif lword[i].lower() == "ş":
                                    lword[i] = "s"
                        lword = ''.join(lword)

                        if usrinput == lword.lower():
                            print(colored("Correct", "green") + "!" + colored(" However, next time pay attention to the accents.", "yellow"))
                            print(colored("They are essential in language learning.", "yellow"))
                            break
                        else:
                            try_number += 1 # Increment try_number by 1

                            if try_number <= 2: # If try_number hasn't reached 3
                                print(colored("Incorrect", "red") + ". Try again.")
                            else: # Else, tell the user the word
                                print(colored("Incorrect", "red") + ". The right answer was: " + colored(lword, "cyan"))
                                break
                elif usrinput == "hint":
                    hints = 3
                    # I honestly don't even understand what this does
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
                elif usrinput == "":
                    try_number += 1 # Increment try_number by 1

                    if try_number <= 2: # If try_number hasn't reached 3
                        print(colored("Incorrect", "red") + ". Try again.")
                    else: # Else, tell the user the word
                        print(colored("Incorrect", "red") + ". The right answer was: " + colored(article, "cyan"), colored(lword, "cyan"))
                        break
                else:
                    print(usrinput, lword, word, hint_number, try_number, article, articles, formal, formality)
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

        if q == 1: # If the user typed "exit" then this will break the loop
            break

    input("Press ENTER to go back...") # Self explanatory


def view_words():
    global lang
    global lang_name
    q = 0
    settings_file = settings("load")

    # The same chunk of code learn_words() has.
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


    if lang in ["tr", "de", "es"]: # This should also be always executed
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


    # This is probably useless. I am not deleting it because it can break the code
    enword = "" # The English word
    lword = "" # The word in the language the user has selected
    formality = 0 # Formality. 0 = no, 1 = yes, 2 = doesn't matter. Set to 0 by default
    article = ""

    if lang in ["tr", "de", "es"]:
        print(colored("\x1B[3mi\x1B[0m", "green") + f": Enter an English word and then the {lang_name} counterpart afterwards.")
        print(colored("\x1B[3mi\x1B[0m", "green") + ": If you spelled a word incorrectly, you can type \"!back\". It will cancel the process.")

        while True:
            lword = "" # The English word
            enword = "" # The word in the language the user has selected
            formality = 0 # Formality. 0 = no, 1 = yes, 2 = doesn't matter. Set to 0 by default

            usrinput = input(" en ==> ")
            if usrinput.lower() == "!back":
                break
            else:
                enword = usrinput

            usrinput = input(f" {lang} ==> ")
            if usrinput.lower() == "!back":
                break
            else:
                lword = usrinput

            print("Now choose the formality of the word. 0 means informal, 1 means formal, 2 means that it doesn't matter.")
            usrinput = input(" formality ==> ")
            if usrinput.lower() == "!back":
                break
            elif usrinput == "0":
                formality = 0
            elif usrinput == "1":
                formality = 1
            elif usrinput == "2":
                formality = 2
            else:
                formality = 2
            
            print("Enter the grammatical article for the word. Enter !skip if there is no article.")
            usrinput = input(" article ==> ")
            if usrinput.lower() != "!skip":
                article = usrinput

            print(f"English word: {enword}")
            print(f"{lang_name} word: {lword}")
            print(f"Formality: {formality}")

            if article == "":
                print(f"Grammatical article: none")
            else:
                print(f"Grammatical article: {article}")

            print("Is this correct? [Y/n] ", end='')
            usrinput = input().lower()
            if usrinput == "" or usrinput == "yes" or usrinput == "y":
                print("add the word") # WORK IN PROGRESS
            else:
                return
            
            input("Press ENTER to continue...")
            return


def settings_change():
    settings_file = settings("load")

    print(colored("Settings", "magenta"))
    print("1. Change default language")
    print("2. Toggle formality on/off (showing if the word is formal or not)")
    print("3. Toggle articles on/off")
    print("4. Reset settings")


    while True:
        usrinput = input(colored(" settings ==> ", "cyan"))

        if usrinput == "1":
            print("Enter your preferred language")
            usrinput = input(" [ES/de/tr] " + colored("==> ", "cyan")).lower()

            if usrinput == "tr" or usrinput == "turkish":
                if usrinput == settings_file["def_lang"]:
                    print("Your language is already set to Turkish (tr).")
                    input("Press ENTER to go back...")

                else:
                    settings_file["def_lang"] = "tr"
                    print("Successfully changed default language to Turkish (tr).")
                    settings("save", settings_file)
                    time.sleep(1.5)
                break

            elif usrinput == "de" or usrinput == "german":
                if usrinput == settings_file["def_lang"]:
                    print("Your language is already set to German (de).")
                    input("Press ENTER to go back...")
                else:
                    settings_file["def_lang"] = "de"
                    print("Successfully changed default language to German (de).")
                    settings("save", settings_file)
                    time.sleep(1.5)
                break

            elif usrinput == "es" or usrinput == "spanish":
                if usrinput == settings_file["def_lang"]:
                    print("Your language is already set to Spanish (es).")
                    input("Press ENTER to go back...")
                else:
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
            # This is set to 1 and if the user types y/yes/nothing it changes
            # the formality setting to True.
            t = 0

            if settings_file["formality"] == False:
                print("This feature is turned off. Turn it on? [Y/n] ", end="")
                t = 1
            else:
                print("This feature is turned on. Turn it off? [Y/n] ", end="")

            usrinput = input()

            if usrinput == "" or usrinput == "y" or usrinput == "yes":
                if t == 0:
                    if settings_file["formality"] == True:
                        settings_file["formality"] = False
                        print("Successfully changed to " + colored(settings_file["formality"], "cyan") + ".")
                    else:
                        print(colored("Cancelled", "cyan") + ".")
                else:
                    if settings_file["formality"] == False:
                        settings_file["formality"] = True
                        print("Successfully changed to " + colored(settings_file["formality"], "cyan") + ".")
                    else:
                        print(colored("Cancelled", "cyan") + ".")
            else:
                print(colored("Cancelled", "cyan") + ".")

        elif usrinput == "3":
            # This is set to 1 and if the user types y/yes/nothing it changes
            # the formality setting to True.
            t = 0

            if settings_file["grammatical_articles"] == False:
                print("This feature is turned off. Turn it on? [Y/n] ", end="")
                t = 1
            else:
                print("This feature is turned on. Turn it off? [Y/n] ", end="")

            usrinput = input()

            if usrinput == "" or usrinput == "y" or usrinput == "yes":
                if t == 0:
                    if settings_file["grammatical_articles"] == True:
                        settings_file["grammatical_articles"] = False
                        print("Successfully changed to " + colored(settings_file["grammatical_articles"], "cyan") + ".")
                    else:
                        print(colored("Cancelled", "cyan") + ".")
                else:
                    if settings_file["grammatical_articles"] == False:
                        settings_file["grammatical_articles"] = True
                        print("Successfully changed to " + colored(settings_file["grammatical_articles"], "cyan") + ".")
                    else:
                        print(colored("Cancelled", "cyan") + ".")
            else:
                print(colored("Cancelled", "cyan") + ".")

        elif usrinput == "4":
            print("Are you sure you want to reset settings? This " + colored("cannot", "red") + " be undone.")
            confirm = input(" [y/N] " + colored("==> ", "magenta")).lower()

            if confirm == "y" or confirm == "yes":
                settings_file["def_lang"] = ""
                settings_file["formality"] = False
                settings_file["grammatical_articles"] = True

                settings("save", settings_file)

        elif usrinput == "exit":
            break

        else:
            print(colored("error", "red") + f": {usrinput}: ivalid choice.")
