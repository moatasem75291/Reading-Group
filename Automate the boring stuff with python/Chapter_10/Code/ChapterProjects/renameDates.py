#! python3
# renameDAtes.py - Renames filenames with American MM-DD-YYYY date formate
# to European DD-MM-YYYY format.

import re
import os
import shutil
from pathlib import Path

# Step 1: Create regex for Amirecan-Style dates.
dataPattern = re.compile(
    """
^(.*?)          # all text before the date
((0|1)?\d)-     # one or two digits for the month
((0|1|2|3)?\d)- # one or two digits for the day
((19|20)\d\d)   # 4 digits for the year
(.*?)$          # all text after the date
""",
    re.VERBOSE,
)

# Step 2: Identify the Date Parts from the FileNames.
for amerFilename in os.listdir("."):
    mo = dataPattern.search(amerFilename)
    if mo == None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Step 3: Form the New Filename and rename the File.
    euroFilename = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart
    absWorkingDir = os.path.abspath(".")
    amerFilename = Path(os.path.join(absWorkingDir, amerFilename))
    euroFilename = Path(os.path.join(absWorkingDir, euroFilename))
    print(f"Renaming {amerFilename.name} to {euroFilename.name}")
    shutil.move(amerFilename, euroFilename)
