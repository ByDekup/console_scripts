from string import ascii_letters
import random as r, os, time, cursor

os.system("")
os.system("title partyy")

with cursor.HiddenCursor():
        while True:
                R = r.randint(0, 255) 
                G = r.randint(0, 255)
                B = r.randint(0, 255)
                print(f"\033[38;2;{R};{G};{B}m{r.choice(ascii_letters)}\033[0m", end="", flush=True)
                time.sleep(0.001)
