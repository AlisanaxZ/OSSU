#functions:

def caesar_encrypt(text, k):
    trials = []
    plaintext = ""
    index = 0


    for char in text:
        trials.append(char)

        if int(ord(char)) >= 65 and int(ord(char)) <= 90:
            number = int(ord(char)) + k
            if number > 90:
                number = (number - 90) + 65 - 1
            plaintext = plaintext + chr(number)
            index = index + 1

        elif int(ord(char)) >= 97 and int(ord(char)) <= 122:
            number = int(ord(char)) + k
            if number > 122:
                number = (number - 122) + 97 - 1
            plaintext = plaintext + chr(number)
            index = index + 1

        else:
            number = int(ord(char))
            plaintext = plaintext + chr(number)

    return plaintext

def caesar_decrypt(text, k):
    trials = []
    plaintext = ""
    index = 0


    for char in text:
        trials.append(char)

        if int(ord(char)) >= 65 and int(ord(char)) <= 90:
            number = int(ord(char)) - k
            if number < 65:
                number = (number + 90) - 65 + 1
            plaintext = plaintext + chr(number)
            index = index + 1

        elif int(ord(char)) >= 97 and int(ord(char)) <= 122:
            number = int(ord(char)) - k
            if number < 97:
                number = (number + 122) - 97 + 1
            plaintext = plaintext + chr(number)
            index = index + 1

        else:
            number = int(ord(char))
            plaintext = plaintext + chr(number)

    return plaintext


# Main program:

a = input("Encrypt or Decrypt? ")
b = input("Type in your text: ")
c = input("Type in the numbers of characters you want to move: ")
try:
    if a == "Encrypt":
        print(caesar_encrypt(b, int(c)))
    elif a == "Decrypt":
        print(caesar_decrypt(b, int(c)))
    else:
        print("Incorrect input")
except:
    print("Incorrect input")
