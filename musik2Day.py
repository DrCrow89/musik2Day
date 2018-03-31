import os, subprocess, random
from glob import glob
from collections import deque

MUSICPATH_FAVORITES = 'musik/list'
SAFE_FILE = 'titel.txt'
NUMBER_OF_SINGLE_TITLES = 3

playlist = glob(os.path.join(MUSICPATH_FAVORITES, '*.mp3'))
last_three_title = deque(maxlen=NUMBER_OF_SINGLE_TITLES)
random_title = random.choice(playlist)

try:
    while True:
        while random_title in last_three_title:
            random_title = random.choice(playlist)
        last_three_title.append(random_title)
        musicplayer = subprocess.Popen(['mpg123', '-q', random_title])
        path, datei = os.path.split(random_title)
        filename, extension = os.path.splitext(datei)
        with open(SAFE_FILE, 'w') as datei:
            datei.write(filename)
        musicplayer.wait()
except KeyboardInterrupt:
        musicplayer.terminate()
