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

with open("gamefiles/settings.json", "r", encoding="utf-8") as f:
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
        print("9. Custom words")

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
                        print(f"Enter the {lang_name} word for " + colored(word, engword_color) + " with the proper grammatical article.")
                    else:
                        print(f"Enter the English word for " + colored(lword, lword_color) + " with the proper grammatical article.")

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
                    lword_nochange = lword
                    lword = list(lword)

                    for i in range(0, len(lword)):
                        if lword[i] in ["í", "ì", "ï", "ó", "ò", "ö",
                                        "é", "è", "ë", "á", "à", "ä",
                                        "ú", "ù", "ü", "ß", "ı", "ç", "ş",
                                        "Í", "Ì", "Ï", "Ó", "Ò", "Ö",
                                        "É", "È", "Ë", "Á", "À", "Ä",
                                        "Ú", "Ù", "Ü", "ẞ", "İ", "Ç", "Ş"]:
                            if lword[i] in ["Í", "Ì", "Ï"]:
                                lword[i] = "I"
                            elif lword[i] in ["Ó", "Ò", "Ö"]:
                                lword[i] = "O"
                            elif lword[i] in ["É", "È", "Ë"]:
                                lword[i] = "E"
                            elif lword[i] in ["Á", "À", "Ä"]:
                                lword[i] = "A"
                            elif lword[i] in ["Ú", "Ù", "Ü"]:
                                lword[i] = "U"
                            elif lword[i] == "ẞ":
                                lword[i] = "SS"
                            elif lword[i] == "İ":
                                lword[i] = "I"
                            elif lword[i] == "Ç":
                                lword[i] = "C"
                            elif lword[i] == "Ş":
                                lword[i] = "S"
                            elif lword[i] in ["ó", "ò", "ö"]:
                                lword[i] = "o"
                            elif lword[i] in ["é", "è", "ë"]:
                                lword[i] = "e"
                            elif lword[i] in ["á", "à", "ä"]:
                                lword[i] = "a"
                            elif lword[i] in ["ú", "ù", "ü"]:
                                lword[i] = "u"
                            elif lword[i] == "ß":
                                lword[i] = "ss"
                            elif lword[i] == "ı":
                                lword[i] = "i"
                            elif lword[i] == "ç":
                                lword[i] = "c"
                            elif lword[i] == "ş":
                                lword[i] = "s"
                    lword = ''.join(lword)

                    if usrinput.lower() == article.lower() + lword.lower():
                        print(colored("Correct", correct_color) + "!" + " The correct word was " + colored(lword_nochange, lword_nochange_color) + ".")
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
                    lword_nochange = lword
                    lword = list(lword)

                    for i in range(0, len(lword)):
                        if lword[i] in ["í", "ì", "ï", "ó", "ò", "ö",
                                        "é", "è", "ë", "á", "à", "ä",
                                        "ú", "ù", "ü", "ß", "ı", "ç", "ş",
                                        "Í", "Ì", "Ï", "Ó", "Ò", "Ö",
                                        "É", "È", "Ë", "Á", "À", "Ä",
                                        "Ú", "Ù", "Ü", "ẞ", "İ", "Ç", "Ş"]:
                            if lword[i] in ["Í", "Ì", "Ï"]:
                                lword[i] = "I"
                            elif lword[i] in ["Ó", "Ò", "Ö"]:
                                lword[i] = "O"
                            elif lword[i] in ["É", "È", "Ë"]:
                                lword[i] = "E"
                            elif lword[i] in ["Á", "À", "Ä"]:
                                lword[i] = "A"
                            elif lword[i] in ["Ú", "Ù", "Ü"]:
                                lword[i] = "U"
                            elif lword[i] == "ẞ":
                                lword[i] = "SS"
                            elif lword[i] == "İ":
                                lword[i] = "I"
                            elif lword[i] == "Ç":
                                lword[i] = "C"
                            elif lword[i] == "Ş":
                                lword[i] = "S"
                            elif lword[i] in ["ó", "ò", "ö"]:
                                lword[i] = "o"
                            elif lword[i] in ["é", "è", "ë"]:
                                lword[i] = "e"
                            elif lword[i] in ["á", "à", "ä"]:
                                lword[i] = "a"
                            elif lword[i] in ["ú", "ù", "ü"]:
                                lword[i] = "u"
                            elif lword[i] == "ß":
                                lword[i] = "ss"
                            elif lword[i] == "ı":
                                lword[i] = "i"
                            elif lword[i] == "ç":
                                lword[i] = "c"
                            elif lword[i] == "ş":
                                lword[i] = "s"
                    lword = ''.join(lword)

                    if usrinput.lower() == lword.lower():
                        print(colored("Correct", correct_color) + "!" + " The correct word was " + colored(lword_nochange, lword_nochange_color) + ".")
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
        print("9. Custom words")

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

            with open(f"languages/{lang}/custom.csv", 'a') as f:
                f.write(f"\n{enword},{lword},{formality},{article}")

            print("Word successfully added!")

            return


def settings_change():
    settings_file = settings("load")

    print(colored("Settings", header_color))
    print("1. Change default language")
    print("2. Toggle formality on/off (showing if the word is formal or not)")
    print("3. Toggle articles on/off")
    print("4. Reset settings")


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
            print("Are you sure you want to reset settings? This " + colored("cannot", error_color) + " be undone.")
            confirm = input(" [y/N] " + colored("==> ", input_color)).lower()

            if confirm == "y" or confirm == "yes":
                settings_file["def_lang"] = ""
                settings_file["formality"] = True
                settings_file["grammatical_articles"] = False
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
