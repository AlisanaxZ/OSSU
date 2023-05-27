# Tra ve nhung tu chua doan
# lettersGuessed: nhung tu da doan
def getAvailableLetters(lettersGuessed):
    result = ''
    for l in 'abcdefghijklmnopqrstuvwxyz':
        if l not in lettersGuessed:
            result += l
    return result

letters = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(letters))