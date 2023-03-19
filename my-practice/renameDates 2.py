#! /usr/bin/env python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import os
import re
import shutil

# create a regex that matches file with the American date format.
datePattern = re.compile(r"""^(.*?)     #all text before the date
    (([01])?\d)-                        #one or two digits for the month
    (([0123])?\d)-                      #one or two digits for the day
    ((19|20)\d\d)                       #four digits for the year
    (.*?)$                              #all text after the date
    """, re.VERBOSE)
# TODO: loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # TODO: skip files without a date.
    if mo is None:
        continue

    # TODO: get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # TODO: form the european-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # TODO: get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # TODO: rename the file.
    # noinspection PyStringFormat
    print('Renaming "%sS" to "s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)  # uncomment after testing