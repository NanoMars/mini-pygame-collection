#game_opener.py

import os
import os
import time

def open_game(path):
    if path.endswith(".py") and path is not None:
        time.sleep(1) 
        os.system(f'python "{path}"')