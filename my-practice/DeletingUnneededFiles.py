#! /user/bin/env python3
# large_file_search.py - Walks through a directory and finds large files.

import os
import send2trash

while True:
    try:
        dir_search = input('Please type in the path to a directory to search.\n')
        os.chdir(dir_search)
        dir_search = os.path.abspath('.')
        print('Searching ' + dir_search + '...')
        break
    except FileNotFoundError:
        print('Path not found. Please enter a complete path.')
        
big_files = 0

global filename

for folder_name, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        filename = os.path.join(folder_name, filename)
        size = os.path.getsize(filename)
        if size > 104857600:
            big_files += 1
            print(os.path.abspath(filename) + ' - ' + str(round((size/1000000), 2)) + ' MB')

print('\nTotal: %s files\n' % big_files)

while big_files >= 1:
    try:
        userChoice = str(input('Do you want to delete all? (Y/N)')).upper()
        
        if userChoice == "Y":
            for folder_name, subfolders, filenames in os.walk('.'):
                for filename in filenames:
                    filename = os.path.join(folder_name, filename)
                    send2trash.send2trash(filename)
            break
        
        elif userChoice == "N":
            break
        print("Done")
    except:
        print("Try Again!")

# /Users/kzsmacbook/Downloads/1
