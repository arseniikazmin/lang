# *lang*
lang is a language learning program to learn, repeat and view words. All words are divided into categories, i.e. food, colors, months, etc.

## Features
- Word learning
- Word viewing
- Adding words
- Turning grammatical articles on/off
- Turning formality display on/off

## Operating systems
- Windows (installation script doesn't work)
- GNU/Linux (Arch Linux, should work on all Linux distributions)
- macOS (never tested, installation script won't work, but the program itself might)

## Available languages:
- Arabic 🇪🇬
- German 🇩🇪
- Spanish 🇪🇸🇲🇽
- Ukrainian 🇺🇦
- Turkish 🇹🇷

## Running the program
First, install dependencies: `pip3 install -r requirements.txt`.  
Type `python3 main.py` and you can start using it.
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
- `/usr/bin/lang`         <-- executable

The installation script doesn't install files in any other directories.

#### Some more information about me and this project
I came up with the idea of this project in December 2021. I originally wanted to create this in C/C++ but due to the lack of knowledge of these languages at that time I started developing it in Python.<br><br>
At the start this was created as a personal project to learn words for school but then I thought about making it available for others; so I continued working on it, adding some more languages and more features such as articles, formality, adding custom words and different modes.<br><br><br>
*This project is licensed under the MIT license*.
