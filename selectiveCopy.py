#! /usr/bin/env python3
# selectiveCopy.py

import os
import shutil


def selective_copy(folder, destination):
    for folder_name, sub_folders, filenames in os.walk(folder):
        print('in os.walk() for ' + folder)
        for filename in filenames:
            if filename.endswith('.' + filename_extension):
                print("Copying '%s' from '%s' to %s..." % (filename, folder_name, destination))
                shutil.copy(os.path.join(folder_name, filename), destination)


print("Please enter Pathname of files wanted to copy and destination")
folder_input = input('From:\n')
folder_output = input('To:\n')
filename_extension = input('Filename extension:\n')
selective_copy(folder_input, folder_output)