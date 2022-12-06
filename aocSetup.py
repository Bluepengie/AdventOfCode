import sys
import datetime
import argparse
import requests
from pathlib import Path

OPEN_FILE = "file = open('Day{}/Day{}Input.txt')\n"

ROOT_FOLDER = Path(sys.argv[0]).parent
COOKIE_PATH = ROOT_FOLDER / "COOKIE.txt"
FOLDER = "Day{}"
PY = "Day{}.py"
INPUT = "Day{}Input.txt"
URL = "https://adventofcode.com/2022/day/{}/input"

parser = argparse.ArgumentParser(
    description = 'Sets up the file template for today\'s Advent of Code'
)

d = datetime.datetime.now().strftime("%d")
parser.add_argument('day', nargs="?", type=int, default=d)
args = parser.parse_args()

day = args.day
if day > int(d):
    print("ERROR: Puzzle is not yet ready")
    exit()
tf = ROOT_FOLDER / FOLDER.format(day)
try:
    tf.mkdir(exist_ok=False)
except FileExistsError:
    print("ERROR: Folder '{}' already exists".format(FOLDER.format(day)))
    exit()

tp = tf / PY.format(day)
with tp.open('w', encoding="utf-8") as f:
    f.write(OPEN_FILE.format(day, day))

cookies = {"session": COOKIE_PATH.read_text().strip()}

ti = tf / INPUT.format(day)
ti.write_bytes(requests.get(URL.format(day), cookies=cookies).content)