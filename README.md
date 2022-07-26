# _lang_
_lang_ is a language learning program to learn and view words. All languages are divided into categories, i.e. food, colors, months, etc.

Version: 0.0.2

## Features
- Word learning
- Word viewing
- Adding words (not yet implemented)


## Languages currently available:
- Spanish 🇪🇸 🇲🇽
- German 🇩🇪
- Turkish 🇹🇷

## Installation
The program can be run as a Python script. Type `python3 main.py` and you can start using it. However, if you want to install it on your system, you can type `sudo ./install.sh install $USER`. This should be ran _only_ through user shell so that the `$USER` variable is set to your username. After installing _lang_, type `lang` and you can start using the program.  
## Uninstall
In order to uninstall _lang_, type `sudo ./install.sh uninstall $USER` the same you did when installing it.  
## Other
Locations of files when installing _lang_ with a script:
- /home/$USER/.lang     <-- game directory
- /usr/bin/lang         <-- executable
