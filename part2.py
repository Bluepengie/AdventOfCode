import sys
import datetime
import shutil
from pathlib import Path

SRC = "Day{}Part1.py"
DEST = "Day{}Part2.py"


d = int(datetime.datetime.now().strftime("%d"))

wd = Path(sys.argv[0]).parent / "Day{}".format(d)
src = wd / SRC.format(d)

dest = wd / DEST.format(d)

dest.write_text(src.read_text())
