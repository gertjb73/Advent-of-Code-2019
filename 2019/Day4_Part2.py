# --- Day 4: Secure Container ---
# --- Part Two ---
#
# An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group
# of matching digits.
#
# Given this additional criterion, but still ignoring the range rule, the following are now true:
#
# 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
# 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
# 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
# How many different passwords within the range given in your puzzle input meet all of the criteria?
#
# Your puzzle input is still 357253-892942.

from collections import Counter


# Function to check a password
def check_password(password):
    is_password_valid = True
    mapped_pwd = str(password)

    # Password rules:
    # 1) It is a six-digit number
    if is_password_valid:
        if len(mapped_pwd) != 6 or type(password) is not int:
            is_password_valid = False
    # 2) The value is within the range given in your puzzle input.
    if is_password_valid:
        if password not in range(password_range_begin, password_range_end):
            is_password_valid = False
    # 3) Two adjacent digits are the same (like 22 in 122345).
    # 5) The two adjacent matching digits are not part of a larger group of matching digits.
    if is_password_valid:
        two_adjacent = False
        how_many_adjacent = Counter(mapped_pwd)
        for k in how_many_adjacent:
            if how_many_adjacent[k] == 2:
                two_adjacent = True
                break
        is_password_valid = two_adjacent
    # 4) Going from left to right, the digits never decrease;
    #    they only ever increase or stay the same (like 111123 or 135679).
    if is_password_valid:
        still_increasing = True
        for i in range(len(mapped_pwd)):
            if i < len(mapped_pwd) - 1:
                if mapped_pwd[i] > mapped_pwd[i + 1]:
                    still_increasing = False
            if not still_increasing:
                break
        is_password_valid = still_increasing

    return is_password_valid


# Main - Go through range of passwords
password_range_begin = 357253
password_range_end = 892942 + 1
valid_passwords = []

for pwd in range(password_range_begin, password_range_end):
    pwdvalid = check_password(pwd)
    if pwdvalid:
        valid_passwords.append(pwd)
print('Number of valid passwords:', len(valid_passwords))

# /usr/local/bin/python3.7 "/Users/rx05sx/Documents/Advent of Code/2019/Day4_Part2.py"
# Number of valid passwords: 324

