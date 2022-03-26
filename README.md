# Swim_Bot
### CSH Major Project 2021 - 2022
### Made By Garrett Maury
### All Research / Labs Made For This Project:
https://github.com/GarrettMaury7921/OpenAI_Tutorials

## Main Directories / Scripts

### main.py
The main driver code of the project. The debug flag is the most important aspect of this class as it controls if you will get output in the console while the program is running. Having debug on will make the program slightly slower due to window capture screens opening.

### menus.py
This class is created from the start and gets the resolution of your main screen (Only supports 1440 currently). This uses pyautogui to find the main menu screen of the game. It will ask what type of game you would want to play. The selection "1" for AI Game, is the only selectable one right now. If the user selects one, it goes to deck detection in the screen_capturing directory. This class also uses the handmade libraries made from the libraries folder.

### bot directory
Contains the card_assets folder with all of the card data in the game. Also contains the card finder classes that find all the card data from the card_assets folder and returns them to the swim_bot.py class (Formatted data). The initializer is the most important class here as it starts the port listener and the window capture class for getting more data while in game. This class is only used while in game.

### image_assets directory
Contains screenshots to compare the main screen to them to realize that the bot is in the main menu of the game. Also contains pictures of certain buttons in that main menu.

### libraries directory
Contains constants of x and y coordinates of where buttons are on the screen. Only supports 1440p screens currently.

### port_listening directory
Probably the best designed class in this project. The game spits data out of a local port and this class uses an https GET to grab the data out of the port every second. This contains card data (with x and y coordinates) and various other info about the game that will be used for the bot. You can get the code of your active deck, the positions of all the cards on the screen, and if you're game is over or not (And if you won).

### screen_capturing directory
This directory is used when in the main menu and when you're in game. The window_capture class is used multiple times and basically uses window's commands to take screenshots quickly and put them together to make kind of a video recording. It does not save the pictures anywhere on your computer but other classes such as the word_detector will look at these screenshots very quickly and find letters and numbers to collect data to return (Such as Health in game or the name of the deck you want to play). The number detector and the word detector are very similar. One finds numbers on screen in various places depending on your monitor while the word detector finds words while you're selecting a deck.

### All Used External Libraries In This Project
import random
import time
import pyautogui
import cv2 as cv (OpenCV)
from threading import Thread, Lock
from pytesseract import pytesseract, Output (For word/number detection)
import numpy as np
import win32con
import win32gui
import win32ui
import sleep
import requests
import ctypes
import win32api
import sys

