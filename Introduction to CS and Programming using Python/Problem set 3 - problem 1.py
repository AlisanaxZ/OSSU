# Neu nhung chu da doan co trong secretWord thi tra ve True, nguoc lai tra ve False
# secretWord: Tu can doan
# lettersGuessed: Nhung chu cai da doan
def isWordGuessed(secretWord, lettersGuessed):
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    return True

Word = 'apple' 
letters = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(Word, letters))