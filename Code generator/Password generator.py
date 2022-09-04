# Code to generate a random password
# Based on an article on 101computing.net, full credit to them

import random

# shuffles all the characters of a string
def shuffle(string):
    temp = list(string)
    random.shuffle(temp)
    return ''.join(temp) # join all the characters in temp string with no spaces

# main program
# Generate random letters based on ASCII code
UppercaseLetter1 = chr(random.randint(65,90))
UppercaseLetter2 = chr(random.randint(65,90))
LowercaseLetter1 = chr(random.randint(97, 122))
LowercaseLetter2 = chr(random.randint(97, 122))
digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))
puncSign1 = chr(random.randint(32, 47))
puncSign2 = chr(random.randint(32, 47))

# Generate password using all characters in randomised order
password = UppercaseLetter1 + UppercaseLetter2 + LowercaseLetter1 + LowercaseLetter2 + digit1 + digit2 + puncSign1 + puncSign2
password = shuffle(password)

print(password)