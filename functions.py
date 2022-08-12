import json
import time
import subprocess
import os
import csv
import sys
from termcolor import colored


ARTICLES_LIST= "das", "die", "der", "el", "la", "lo", "los", "las", "ال"
# The clear() function uses this variable. If you are using Microsoft Windows,
# you should either change it to "cls" or run the script inside a Powershell.
CLEAR_FUNCTION = ""

if sys.platform in ["linux", "linux1", "linux2", "darwin", "win32"]:
    if sys.platform in ["linux", "linux1", "linux2", "darwin"]:
        CLEAR_FUNCTION = "clear"
    else:
        CLEAR_FUNCTION = "cls"
else:
    print(f"Your operating system ({sys.platform}) is not supported.")
    exit()

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

print(DIR_PATH)

# the default language is Spanish
lang = "es" # language code
lang_name = "Spanish" # language name


header_color = ""
engword_color = ""
lword_color = ""
lword_nochange_color = ""
formal_color = ""
article_color = ""
input_color = ""
error_color = ""
correct_color = ""
incorrect_color = ""
hint_color = ""

with open(DIR_PATH + "/gamefiles/settings.json", "r", encoding="utf-8") as f:
        config = json.load(f)

        header_color = config["colors"]["header_color"]
        engword_color = config["colors"]["engword_color"]
        lword_color = config["colors"]["lword_color"]
        formal_color = config["colors"]["formal_color"]
        article_color = config["colors"]["article_color"]
        input_color = config["colors"]["input_color"]
        error_color = config["colors"]["error_color"]
        correct_color = config["colors"]["correct_color"]
        incorrect_color = config["colors"]["incorrect_color"]
        lword_nochange_color = config["colors"]["lword_nochange_color"]
        hint_color = config["colors"]["hint_color"]


def clear():
    subprocess.run(CLEAR_FUNCTION, shell=True)


def settings(tp="load", set_dict=[]):
    if tp == "save":
        with open(DIR_PATH + "/gamefiles/settings.json", "w", encoding="utf-8") as f:
            json.dump(set_dict, f, indent=4) # wrting to json with indentation 4
    elif tp == "load":
        with open(DIR_PATH + "/gamefiles/settings.json", "r", encoding="utf-8") as f:
            return json.load(f) # returning the loaded settings file


def load_words(lang=lang, name="all"):
    with open(DIR_PATH + f"/languages/{lang}/{name}.csv", "r", encoding="utf-8") as f:
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
    elif settings_file["def_lang"] == "ar":
        lang = "ar"
        lang_name = "Arabic"

        if settings_file["mode"] != 2:
            print("It seems that you are learning Arabic.")
            print("Would you like to the second mode (entering the English word as an answer)?")
            print("You can permanently turn this on in the settings.")
            print("This way you can learn if you don't have an Arabic keyboard.\n [Y/n] ", end="")
            usrinput = input(colored("==> ", "cyan")).lower()

            if usrinput == "" or usrinput == "y" or usrinput == "yes":
                settings_file["mode"] = 2
                settings("save", settings_file)
                print("Mode successfully changed to 2.")
    else:
        print("Select language:")
        print("1. Turkish")
        print("2. German")
        print("3. Spanish")
        print("4. Arabic")

        while True:
            usrinput = input(colored(" ==> ", input_color)).lower()

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

            elif usrinput == "4" or usrinput == "arabic":
                lang = "ar"
                lang_name = "Arabic"

                if settings_file["mode"] != 2:
                    print("It seems that you are learning Arabic.")
                    print("Would you like to set your mode to 2 (entering the English word as an answer)?")
                    print("You can permanently turn this on in the settings.")
                    print("This way you can learn if you don't have an Arabic keyboard.\n [Y/n] ", end="")
                    usrinput = input(colored("==> ", "cyan")).lower()

                    if usrinput == "" or usrinput == "y" or usrinput == "yes":
                        settings_file["mode"] = 2
                        settings("save", settings_file)
                        print("Mode successfully changed to 2.")

                break

            elif usrinput == "clear":
                clear()
                print("Select language:")
                print("1. Turkish")
                print("2. German")
                print("3. Spanish")
                print("4. Arabic")

            elif usrinput == "exit":
                q = 1
                break

            else:
                print(colored("error", error_color) + f": {usrinput}: invalid option.")

        if q == 1:
            return

    if lang in ["tr", "de", "es", "ar"]: # Technically this should always be executed
        print("Choose a category: ")
        print("1. All words")
        print("2. Colours")
        print("3. Days")
        print("4. Food")
        print("5. Months")
        print("6. Numbers")
        print("7. Numbers (extended)")
        if lang in ["de", "es", "ar"]:
            print("8. Countries")
        if lang == "de":
            print("9. Outside")
        print("10. Custom words")

        # This asks for user's input and based on what they enter
        # the "name" variable will be changed. It is used for
        # opennig .csv files with all the words.
        while True:
            usrinput = input(colored(" ==> ", input_color)).lower()

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
            elif usrinput == "8" and lang in ["de", "es", "ar"]:
                name = "countries"
                break
            elif usrinput == "9":
                name = "outside"
                break
            elif usrinput == "10":
                name = "custom"
                break
            elif usrinput == "exit":
                q = 1
                break
            else:
                print(colored("error", error_color) + f": {usrinput}: invalid option.")

        if q == 1:
            return

        words = load_words(lang, name)

    if q == 1:
        return

    rows, fields = load_words(lang, name)
    mode = settings_file["mode"]

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
        lword_nochange = ""

        if formal == "0":
            formality = "no"
        elif formal == "1":
            formality = "yes"
        elif formal == "2":
            formality = "no"

        while True:
            if formal != "2":
                if articles == True:
                    if mode == 1:
                        print(f"Enter the {lang_name} word for " + colored(word, engword_color) + " with the proper grammatical article. Formal?: " + colored(formality, formal_color))
                    else:
                        print(f"Enter the English word for " + colored(lword, lword_color) + " with the proper grammatical article. Formal?: " + colored(formality, formal_color))
                else:
                    if mode == 1:
                        print(f"Enter the {lang_name} word for " + colored(word, engword_color) + ". Formal?: " + colored(formality, formal_color))
                    else:
                        print(f"Enter the English word for " + colored(lword, lword_color) + ". Formal?: " + colored(formality, formal_color))
            else:
                if articles == True:
                    if mode == 1:
                        print(f"Enter the {lang_name} word for " + colored(word, engword_color) + " with the proper grammatical article.")
                    else:
                        print(f"Enter the English word for " + colored(lword, lword_color) + " with the proper grammatical article.")
                else:
                    if mode == 1:
                        print(f"Enter the {lang_name} word for " + colored(word, engword_color) + ".")
                    else:
                        print(f"Enter the English word for " + colored(lword, lword_color) + ".")

            print(colored(" ╰─> ", input_color), end="")

            usrinput = input().lower()

            if article not in ARTICLES_LIST:
                articles = False

            # If articles are enabled and the user hasn't tried to use a hint/exit
            if articles == True and usrinput != "hint" and usrinput != "exit":
                if usrinput == lword.lower() and mode == 1:
                    print(colored("Correct", correct_color) + "!")
                    break
                elif usrinput == word.lower() and mode == 2:
                    print(colored("Correct", correct_color) + "!")
                    break
                else:
                    lword_change = ""
                    list(lword_change)

                    for i in range(0, len(lword_change)):
                        if lword_change[i] in ["í", "ì", "ï", "ó", "ò", "ö",
                                        "é", "è", "ë", "á", "à", "ä",
                                        "ú", "ù", "ü", "ß", "ı", "ç", "ş",
                                        "Í", "Ì", "Ï", "Ó", "Ò", "Ö",
                                        "É", "È", "Ë", "Á", "À", "Ä",
                                        "Ú", "Ù", "Ü", "ẞ", "İ", "Ç", "Ş"]:
                            if lword_change[i] in ["Í", "Ì", "Ï"]:
                                lword_change[i] = "I"
                            elif lword_change[i] in ["Ó", "Ò", "Ö"]:
                                lword_change[i] = "O"
                            elif lword_change[i] in ["É", "È", "Ë"]:
                                lword_change[i] = "E"
                            elif lword_change[i] in ["Á", "À", "Ä"]:
                                lword_change[i] = "A"
                            elif lword_change[i] in ["Ú", "Ù", "Ü"]:
                                lword_change[i] = "U"
                            elif lword_change[i] == "ẞ":
                                lword_change[i] = "SS"
                            elif lword_change[i] == "İ":
                                lword_change[i] = "I"
                            elif lword_change[i] == "Ç":
                                lword_change[i] = "C"
                            elif lword_change[i] == "Ş":
                                lword_change[i] = "S"
                            elif lword_change[i] in ["ó", "ò", "ö"]:
                                lword_change[i] = "o"
                            elif lword_change[i] in ["é", "è", "ë"]:
                                lword_change[i] = "e"
                            elif lword_change[i] in ["á", "à", "ä"]:
                                lword_change[i] = "a"
                            elif lword_change[i] in ["ú", "ù", "ü"]:
                                lword_change[i] = "u"
                            elif lword_change[i] == "ß":
                                lword_change[i] = "ss"
                            elif lword_change[i] == "ı":
                                lword_change[i] = "i"
                            elif lword_change[i] == "ç":
                                lword_change[i] = "c"
                            elif lword_change[i] == "ş":
                                lword[i] = "s"
                    lword_change = ''.join(lword_change)

                    if usrinput.lower() == article.lower() + lword_change.lower():
                        print(colored("Correct", correct_color) + "!" + " The correct word was " + colored(lword_change, lword_nochange_color) + ".")
                        break
                    else:
                        try_number += 1 # Increment try_number by 1

                        if try_number <= 2: # If try_number hasn't reached 3
                            print(colored("Incorrect", error_color) + ". Try again.")
                        else: # Else, tell the user the word
                            print(colored("Incorrect", error_color) + ". The right answer was: " + colored(article, article_color), colored(lword, lword_color))
                            break
            # If articles are disabled AND the user hasn't tried to use a hint/exit
            elif articles == False and usrinput != "hint" and usrinput != "exit":
                if usrinput == lword.lower() and mode == 1:
                    print(colored("Correct", correct_color) + "!")
                    break
                elif usrinput == word.lower() and mode == 2:
                    print(colored("Correct", correct_color) + "!")
                    break
                else:
                    lword_change = lword
                    list(lword_change)

                    for i in range(0, len(lword)):
                        if lword[i] in ["í", "ì", "ï", "ó", "ò", "ö",
                                        "é", "è", "ë", "á", "à", "ä",
                                        "ú", "ù", "ü", "ß", "ı", "ç", "ş",
                                        "Í", "Ì", "Ï", "Ó", "Ò", "Ö",
                                        "É", "È", "Ë", "Á", "À", "Ä",
                                        "Ú", "Ù", "Ü", "ẞ", "İ", "Ç", "Ş"]:
                            if lword_change[i] in ["Í", "Ì", "Ï"]:
                                lword_change[i] = "I"
                            elif lword_change[i] in ["Ó", "Ò", "Ö"]:
                                lword_change[i] = "O"
                            elif lword_change[i] in ["É", "È", "Ë"]:
                                lword_change[i] = "E"
                            elif lword_change[i] in ["Á", "À", "Ä"]:
                                lword_change[i] = "A"
                            elif lword_change[i] in ["Ú", "Ù", "Ü"]:
                                lword_change[i] = "U"
                            elif lword_change[i] == "ẞ":
                                lword_change[i] = "SS"
                            elif lword_change[i] == "İ":
                                lword_change[i] = "I"
                            elif lword_change[i] == "Ç":
                                lword_change[i] = "C"
                            elif lword_change[i] == "Ş":
                                lword_change[i] = "S"
                            elif lword_change[i] in ["ó", "ò", "ö"]:
                                lword_change[i] = "o"
                            elif lword_change[i] in ["é", "è", "ë"]:
                                lword_change[i] = "e"
                            elif lword_change[i] in ["á", "à", "ä"]:
                                lword_change[i] = "a"
                            elif lword_change[i] in ["ú", "ù", "ü"]:
                                lword_change[i] = "u"
                            elif lword_change[i] == "ß":
                                lword_change[i] = "ss"
                            elif lword_change[i] == "ı":
                                lword_change[i] = "i"
                            elif lword_change[i] == "ç":
                                lword_change[i] = "c"
                            elif lword_change[i] == "ş":
                                lword_change[i] = "s"
                    lword_change = ''.join(lword_change)

                    if usrinput.lower() == lword_change.lower():
                        print(colored("Correct", correct_color) + "!" + " The correct word was " + colored(lword_change, lword_nochange_color) + ".")
                        break
                    else:
                        try_number += 1 # Increment try_number by 1

                        if try_number <= 2: # If try_number hasn't reached 3
                            print(colored("Incorrect", error_color) + ". Try again.")
                        else: # Else, tell the user the word
                            print(colored("Incorrect", error_color) + ". The right answer was: " + colored(lword, lword_color))
                            break
            elif usrinput == "hint":
                hints = 3
                # I honestly don't even understand what this does
                if len(lword) <= hints:
                    hints = len(lword) - 1
                else:
                    pass

                if hint_number < hints:
                    print(colored("Hint", hint_color) + f": {lword[hint_number]}")
                    hint_number += 1
                else:
                    print("No hints left")
            elif usrinput == "exit":
                q = 1
                break
            elif usrinput == "":
                try_number += 1 # Increment try_number by 1

                if try_number <= 2: # If try_number hasn't reached 3
                    print(colored("Incorrect", error_color) + ". Try again.")
                else: # Else, tell the user the word
                    print(colored("Incorrect", error_color) + ". The right answer was: " + colored(article, article_color), colored(lword, lword_color))
                    break
            else:
                print(usrinput, lword, word, hint_number, try_number, article, articles, formal, formality)


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
    elif settings_file["def_lang"] == "ar":
        lang = "ar"
        lang_name = "Arabic"
    else:
        print("Select language:")
        print("1. Turkish")
        print("2. German")
        print("3. Spanish")
        print("4. Arabic")

        while True:
            usrinput = input(colored(" ==> ", input_color)).lower()

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
            elif usrinput == "4" or usrinput == "arabic":
                lang = "ar"
                lang_name = "Arabic"
                break
            elif usrinput == "clear":
                clear()
                print("Select language:")
                print("1. Turkish")
                print("2. German")
                print("3. Spanish")
                print("4. Arabic")
            elif usrinput == "exit":
                q = 1
                break
            else:
                print(colored("error", error_color) + f": {usrinput}: invalid option.")

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
        if lang in ["de", "es", "ar"]:
            print("8. Countries")
        if lang == "de":
            print("9. Outside")
        print("10. Custom words")

        while True:
            usrinput = input(colored(" ==> ", input_color)).lower()

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
            elif usrinput == "8" and lang in ["de", "es", "ar"]:
                name = "countries"
                break
            elif usrinput == "9":
                name = "outside"
                break
            elif usrinput == "10":
                name = "custom"
                break
            elif usrinput == "clear":
                clear()
                print("Select language:")
                print("1. Turkish")
                print("2. German")
                print("3. Spanish")
                print("4. Arabic")
            elif usrinput == "exit":
                q = 1
                break
            else:
                print(colored("error", error_color) + f": {usrinput}: invalid option.")


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
                print(colored(i + 1, "green") + ".", colored(row[0], engword_color), "-", colored(row[3], article_color), colored(row[1], lword_color))
            else:
                print(colored(i + 1, "green") + ".", colored(row[0], engword_color), "-", colored(row[1], lword_color))
        else:
            print(colored(i + 1, "green") + ".", colored(row[0], engword_color), "-", colored(row[1], lword_color))

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
    elif settings_file["def_lang"] == "ar":
        lang = "ar"
        lang_name = "Arabic"

    print("Select language:")
    print("1. Turkish")
    print("2. German")
    print("3. Spanish")
    print("4. Arabic")

    while True:
        usrinput = input(colored(" ==> ", input_color)).lower()

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
        elif usrinput == "4" or usrinput == "arabic":
            lang = "ar"
            lang_name = "Arabic"
            break
        elif usrinput == "clear":
            clear()
            print("Select language:")
            print("1. Turkish")
            print("2. German")
            print("3. Spanish")
            print("4. Arabic")
        elif usrinput == "exit":
            q = 1
            break
        else:
            print(colored("error", error_color) + f": {usrinput}: invalid option.")

    if q == 1:
        return


    enword = "" # The English word
    lword = "" # The word in the language the user has selected
    formality = 0 # Formality. 0 = no, 1 = yes, 2 = doesn't matter. Set to 0 by default
    article = ""

    if lang in ["tr", "de", "es", "ar"]:
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
                article = "none"
                print("Grammatical article: none")
            else:
                print(f"Grammatical article: {article}")

            print("Is this correct? [Y/n] ", end='')
            usrinput = input().lower()
            if usrinput == "" or usrinput == "yes" or usrinput == "y":
                print("add the word") # WORK IN PROGRESS
            else:
                return

            with open(DIR_PATH + f"/languages/{lang}/custom.csv", 'a') as f:
                f.write(f"\n{enword},{lword},{formality},{article}")

            print("Word successfully added!")

            return


def settings_change():
    settings_file = settings("load")

    print(colored("Settings", header_color))
    print("1. Change default language")
    print("2. Toggle formality on/off (showing if the word is formal or not)")
    print("3. Toggle articles on/off")
    print("4. Change mode")
    print("5. Reset settings")


    while True:
        usrinput = input(colored(" settings ==> ", input_color))

        if usrinput == "1":
            print("Enter your preferred language")
            usrinput = input(" [ES/de/ar/tr] " + colored("==> ", input_color)).lower()

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

            elif usrinput == "ar" or usrinput == "arabic":
                if usrinput == settings_file["def_lang"]:
                    print("Your language is already set to Arabic (ar).")
                    input("Press ENTER to go back...")
                else:
                    settings_file["def_lang"] = "ar"
                    print("Successfully changed default language to Arabic (ar).")
                    settings("save", settings_file)
                    time.sleep(1.5)
                break

            elif usrinput == "exit":
                pass

            else:
                print(colored("error", error_color) + f": {usrinput}: ivalid language number/name/code.")

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
                        print("Successfully changed to " + colored(settings_file["formality"], formal_color) + ".")
                    else:
                        print(colored("Cancelled", error_color) + ".")
                else:
                    if settings_file["formality"] == False:
                        settings_file["formality"] = True
                        print("Successfully changed to " + colored(settings_file["formality"], formal_color) + ".")
                    else:
                        print(colored("Cancelled", error_color) + ".")
            else:
                print(colored("Cancelled", error_color) + ".")

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
                        print("Successfully changed to " + colored(settings_file["grammatical_articles"], formal_color) + ".")
                    else:
                        print(colored("Cancelled", error_color) + ".")
                else:
                    if settings_file["grammatical_articles"] == False:
                        settings_file["grammatical_articles"] = True
                        print("Successfully changed to " + colored(settings_file["grammatical_articles"], formal_color) + ".")
                    else:
                        print(colored("Cancelled", error_color) + ".")
            else:
                print(colored("Cancelled", error_color) + ".")

        elif usrinput == "4":
            print(f"Your current mode is {settings_file['mode']}.")
            print(" Mode 1 --> typing words in the target language (i.e. German)")
            print(" Mode 2 --> typing words in English")
            print("Would you like to change the mode? [Y/n] ", end="")
            usrinput = input().lower()

            if usrinput == "" or usrinput == "y" or usrinput == "yes":
                previousmode = settings_file["mode"]

                if settings_file["mode"] == 1:
                    settings_file["mode"] = 2
                else:
                    settings_file["mode"] = 1
                settings("save", settings_file)

                print(f"Mode successfully changed from {previousmode} ==> {settings_file['mode']}.")

        elif usrinput == "5":
            print("Are you sure you want to reset settings? This " + colored("cannot", error_color) + " be undone.")
            confirm = input(" [y/N] " + colored("==> ", input_color)).lower()

            if confirm == "y" or confirm == "yes":
                settings_file["def_lang"] = ""
                settings_file["formality"] = True
                settings_file["grammatical_articles"] = False
                settings_file["mode"] = 1
                settings_file["colors"]["header_color"] = "magenta"
                settings_file["colors"]["engword_color"] = "magenta"
                settings_file["colors"]["lword_color"] = "cyan"
                settings_file["colors"]["lword_nochange_color"] = "yellow"
                settings_file["colors"]["formal_color"] = "cyan"
                settings_file["colors"]["article_color"] = "cyan"
                settings_file["colors"]["input_color"] = "cyan"
                settings_file["colors"]["error_color"] = "red"
                settings_file["colors"]["correct_color"] = "green"
                settings_file["colors"]["incorrect_color"] = "red"
                settings_file["colors"]["hint_color"] = "magenta"

                settings("save", settings_file)

        elif usrinput == "exit":
            break

        else:
            print(colored("error", error_color) + f": {usrinput}: ivalid choice.")

def help():
    while True:
        clear()
        print("\t === Help manual ===")
        print("Type '6' or 'exit' to go back.", end="\n\n")
        print(" 1. How does the program work?")
        print(" 2. How do I add custom words?")
        print(" 3. What if I am learning a language with a non-Roman")
        print("    alphabet and don't have a specific keyboard?")
        print(" 4. More about the programs functionality/commands")
        print(" 5. Info about other languages/future features")
        print(" 6. Go back")
        usrinput = input(colored(" ==> ", input_color))
        
        if usrinput in ["1", "2", "3", "4", "5", "6", "exit"]:
            if usrinput == "1":
                clear()
                print("This program is written in Python and uses CSV tables for words.")
                print("Every row in CSV has a word in English and in the foreign language you want to study.")
                print("Then there is the formality of the word (whether you use it with friends/colleagues")
                print("or in situations such as meetings/people who are older) and the grammatical article")
                print("(i.e. der, die, das; equivalent of the English 'the'). For example, in German all nouns")
                print("have a gender and the article depends on it. It is very important to learn it as there")
                print("is no 100% way to guess the gender of a word in German.")
                input("Press ENTER to continue...")
            elif usrinput == "2":
                clear()
                print("You can add your own words in the main menu.")
                print("Navigate to the main menu, then choose the 'Add custom words' option.")
                print("You will need to choose the language where you want to add the word.")
                print("Then, the program will ask you for the English word and then the word")
                print("in the language you chose.")
                print("You will then be asked whether the word is formal/informal/doesn't matter")
                print("and the correct article (i.e. der, die, das).")
                print("Additional info: if you want to cancel the process, type '!back'.")
                input("Press ENTER to continue...")
            elif usrinput == "3":
                clear()
                print("If you are learning a language that uses a writing system other than the Roman alphabet,")
                print("you can go to settings and choose 'Change mode'.")
                print("There are two modes. The first one is when you enter the word in the language you are")
                print("learning. The second one is when you are entering the word in English.")
                print("This is extremely useful when you don't have a proper keyboard installed.")
                input("Press ENTER to continue...")
            elif usrinput == "4":
                clear()
                print("There are some commands you can enter while learning words.")
                print(" 'clear' - clear the screen,")
                print(" 'hint' - get a hint. There are 3 available hints for each word,")
                print(" 'exit' - exit to the main menu")
                input("Press ENTER to continue...")
            elif usrinput == "5":
                clear()
                print("This program currently has 4 languages:")
                print("  - Arabic")
                print("  - German")
                print("  - Spanish")
                print("  - Turkish", end="\n\n")
                print("In the future, these languages will be added:")
                print("  - French")
                print("  - Ukrainian", end="\n\n")
                print("However, languages that are already available will still be worked on.")
                print("Primarily German, but I will try adding more words to others.")
                input("Press ENTER to continue...")
            elif usrinput == "6" or usrinput == "exit":
                break
        else:
            print("Invalid input")
