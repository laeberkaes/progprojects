import os
import platform
import sys
import time

# Static Variables
screen_width = os.get_terminal_size().columns

# Static Functions
def clear():
    if platform.system() in ["Linux", "Darwin"]:
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        raise ValueError ("No known operating system.")

def speech_manipulation(text, speed):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)