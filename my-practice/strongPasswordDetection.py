#! /usr/bin/env python3
# strong_password_detection.py

"""
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that
is at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string
against multiple regex patterns to validate its strength.
"""
import re, pyperclip

def strong_password(password):
    regex_count = 0
    for regex in regex_list:
        if regex.search(password) is None:
            print('Sorry, your password is not strong enough')
            break
        else:
            regex_count += 1
            continue
    if regex_count is 4:
        print('Congrats. Your password is strong enough!')

length_regex = re.compile('.{8,}')
lower_case_regex = re.compile('[a-z]+')
upper_case_regex = re.compile('[A-Z]+')
digit_regex = re.compile('[\d]+')

regex_list = [length_regex,
              lower_case_regex,
              upper_case_regex,
              digit_regex]

pw = input('Please type in a password:\n')
strong_password(pw)
pyperclip.copy(pw)

