import time
import subprocess

while True:
    print("List Of Topics Has Been Adjusted")
    subprocess.Popen("Filter.py 1", shell=True)
    time.sleep(3)

