# In ra tu da doan voi nhung chu cai da doan dung
def getGuessedWord(secretWord, lettersGuessed):
    result = ''
    for l in secretWord:
        # Neu chu cai co trong tu da doan thi xuat hien trong kq
        if l in lettersGuessed:
            result += l
        # Neu khong thi duoc thay bang dau "_"
        else:
            result += '_'
    return result

Word = 'apple'
letters = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(Word, letters))