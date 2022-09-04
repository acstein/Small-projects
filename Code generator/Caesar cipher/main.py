# Cipher based on code used by Julius Caesar
# Each letter is 3 letters back

import numpy as np

def code_generator(message):
    """
    Creates a coded message based on caesar cipher
    :param message: Input code (varchar)
    :return: Coded message (varchar)
    """
    split = np.array([*message]) # split input message into seperate characters
    numerical = split.view(np.int32) # convert each character into ASCII value
    numerical_code = []

    for i in numerical:
        if i>99 and i<123: # lowercase d-z
            numerical_code.append(i - 3)
            continue
        if i<100 and i>96: # lowercase a-c
            numerical_code.append(i + 23)
            continue
        if i<91 and i>67: # uppercase d-z
            numerical_code.append(i - 3)
            continue
        if i<68 and i>64: # uppercase a-c
            numerical_code.append(i + 23)
            continue
        else:
            numerical_code.append(i) # if not a letter

    code = []
    for i in range(len(numerical_code)):
        code.append(chr(numerical_code[i])) # change numerical back to corresponding characters

    return ''.join(code)

def code_cracker(message):
    """
        Uncodes a message based on caesar cipher
    :param message: Input codeed message (varchar)
    :return: Uncoded message (varchar)
    """
    split = np.array([*message]) # split input message into seperate characters
    numerical = split.view(np.int32) # convert each character into ASCII value
    numerical_uncoded = []

    for i in numerical:
        if i>96 and i<120: # lowercase a-w
            numerical_uncoded.append(i + 3)
            continue
        if i<123 and i>119: # lowercase x-z
            numerical_uncoded.append(i - 23)
            continue
        if i<88 and i>64: # uppercase a-w
            numerical_uncoded.append(i + 3)
            continue
        if i<91 and i>87: # uppercase x-z
            numerical_uncoded.append(i - 23)
            continue
        else:
            numerical_uncoded.append(i) # ignore if not a letter

    uncoded = []
    for i in range(len(numerical_uncoded)):
        uncoded.append(chr(numerical_uncoded[i])) # change numerical back to corresponding character

    return ''.join(uncoded)
