# *lang*
lang is a language learning program to learn and view words. All languages are divided into categories, i.e. food, colors, months, etc.

Version: 0.0.2de

## Features
- Word learning
- Word viewing
- Adding words (not yet implemented)
- Turning grammatical articles on/off
- Turning formality display on/off

## Currently supported operating systems
- GNU/Linux (tested on Arch Linux, should work on all Linux distributions)
- macOS (never tested, installation script will most likely not work, but the program itself should)

## Available languages:
- Spanish 🇪🇸 🇲🇽
- German 🇩🇪
- Turkish 🇹🇷

## Running the program
The program can be run as a Python script. Type `python3 main.py` and you can start using it.
## Installation
_**Warning**_: *this is for Linux only!*  
If you want to install it on your system, you can type `sudo ./install.sh install $USER` inside lang's folder. This should be ran _only_ through user shell so that the `$USER` variable is set to your username. Alternatively, instead of typing `$USER` you can type your username.  
**If you try installing it this way after running `su` it will install it for root.**  <br><br>
After installing lang, type `lang` and you can start using the program.  
## Uninstall
In order to uninstall lang, type `sudo ./install.sh uninstall $USER` the same way you did when installing it.  
## Other
Locations of files when installing lang with the `install.sh` script:
- `/home/$USER/.lang`     <-- game directory
- `/usr/bin/lang`         <-- executable<br><br>

#### Some more information about me and this project
I came up with the idea of this project in December 2021. I originally wanted to create this in C/C++ but due to the lack of knowledge of these languages at that time I started developing this in Python.<br><br>
At the start this was created as a personal project to learn words for school but then I thought about making it available for others; so I continued working on it, adding some more languages and minor features such as articles/formality and perhaps adding custom words in the future.<br><br><br>
*This project is licensed under the MIT license*.
