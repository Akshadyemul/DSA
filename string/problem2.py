'''
Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

Its length is at least 6.
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
'''


def minimum_number(password):
    n = len(password)
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    digit = False
    lower = False
    upper = False
    special = False

    for char in password:
        if char in numbers:
            digit = True
        if char in lower_case:
            lower = True
        if char in upper_case:
            upper = True
        if char in special_characters:
            special = True

    missing = 0
    if digit == False:
        missing += 1
    if lower == False:
        missing += 1
    if upper == False:
        missing += 1
    if special == False:
        missing += 1

    length_need = 6 - n
    if missing > length_need:
        return missing
    else:
        return length_need


print(minimum_number('Akshad@123'))