# _lang_
lang is a language learning program to learn and view words. All languages are divided into categories, i.e. food, colors, months, etc.

Version: 0.0.2


## Features
- Word learning
- Word viewing
- Adding words (not yet implemented)

Currently supported operating systems: GNU/Linux (Arch)


## Available languages:
- Spanish 🇪🇸 🇲🇽
- German 🇩🇪
- Turkish 🇹🇷

## Installation
The program can be run as a Python script. Type `python3 main.py` and you can start using it. However, if you want to install it on your system, you can type `sudo ./install.sh install $USER` inside lang's folder. This should be ran _only_ through user shell so that the `$USER` variable is set to your username.  
If you try installing in this way after running `su` it will probably install it for `root` (I never tested).  
After installing lang, type `lang` and you can start using the program.  
## Uninstall
In order to uninstall lang, type `sudo ./install.sh uninstall $USER` the same way you did when installing it.  
## Other
Locations of files when installing lang with the `install.sh` script:
- `/home/$USER/.lang`     <-- game directory
- `/usr/bin/lang`         <-- executable
_This project was originally hosted on GitLab_
