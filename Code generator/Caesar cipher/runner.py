import main

original = input("Please enter your message here: ")
code = main.code_generator(original)

uncoded = main.code_cracker(code)

print("coded message = ", code, "\nuncoded message = ", uncoded)