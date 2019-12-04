# --- Day 4: Secure Container ---
# --- Part One ---
#
# You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the
# password on a sticky note, but someone threw it out.
#
# However, they do remember a few key facts about the password:
#
# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:
#
# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
# How many different passwords within the range given in your puzzle input meet these criteria?
#
# Your puzzle input is 357253-892942.


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
    if is_password_valid:
        two_adjacent = False
        for i in range(len(mapped_pwd)):
            if i < len(mapped_pwd) - 1:
                if mapped_pwd[i] == mapped_pwd[i+1]:
                    two_adjacent = True
            if two_adjacent:
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
