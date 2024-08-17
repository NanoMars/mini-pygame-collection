#game_opener.py
import os
import time
import subprocess

print("game opener opened!!!!")

def open_game(path):
    print("open game ",path)

    


    if path.endswith(".py") and path is not None:
        print("entering the if statement")

        if os.path.exists(path):
            print(f"File {path} exists.")
        else:
            print(f"File {path} does NOT exist.")

        print("Absolute path:", os.path.abspath(path))

        time.sleep(1) 
        print("after 1 second")
        result = subprocess.run(['python', path], capture_output=True, text=True)
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)
        if result.returncode != 0:
            print(f"Error running the game script: {result.stderr}")
        time.sleep(3) 
