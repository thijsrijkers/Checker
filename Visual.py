import time
import subprocess
import os

def read_file():
    with open("D:\!!!!!Checker\Storage\data.json", "r") as f:
        SMRF1 = f.readlines()
    return SMRF1

initial = read_file()

while True:
    current = read_file()
    if initial != current:
        subprocess.Popen("Filter.py 1", shell=True)
        initial = current

    time.sleep(3)

