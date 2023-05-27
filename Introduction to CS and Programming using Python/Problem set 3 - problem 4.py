# Kiem tra xem chu cai da doan co trong tu can doan khong
# secretWord: tu can doan
# lettersGuessed: chu da doan
def isWordGuessed(secretWord, lettersGuessed):
    for l in secretWord:
        if l not in lettersGuessed:
            return False
    return True

# Tra ve tu da doan voi cac chu cai da doan dung
# secretWord: tu can doan
# lettersGuessed: chu da doan
def getGuessedWord(secretWord, lettersGuessed):
    result = ''
    for l in secretWord:
        if l in lettersGuessed:
            result += l
        else:
            result += '_'
    return result

# Cho biet cac chu cai chua doan
# lettersGuessed: chu da doan
def getAvailableLetters(lettersGuessed):
    result = ''
    for l in 'abcdefghijklmnopqrstuvwxyz':
        if l not in lettersGuessed:
            result += l
    return result

# Tro choi hangman
# secretWord: tu can doan
def hangman(secretWord):
    # Cho nguoi choi goi y ve tu can doan va khoi tao cac gia tri 
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []
    # Chay tro choi neu nhu so lan sai it hon 8
    while mistakesMade < 8:
        # Neu doan dung thong bao cho nguoi choi da thang
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('Congratulations, you won!')
            break
        else:
            # Neu chua doan xong thong bao cho nguoi choi cac thong tin
            print('------------')
            print('You have', 8 - mistakesMade, 'guesses left.')
            print('Available letters:', getAvailableLetters(lettersGuessed))
            guess = str(input('Please guess a letter: ')).lower()
            # Neu doan dung thi thong bao cho nguoi choi
            if guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            # Neu da doan tu do thi thong bao cho nguoi choi
            elif guess in lettersGuessed:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            # Neu doan sai thi thong bao cho nguoi choi va thay doi gia tri mistakesMade
            elif guess not in secretWord:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(guess)
                mistakesMade += 1
        # Neu so lan sai bang 8 thi thong bao cho nguoi choi va cho biet tu can doan       
        if 8 - mistakesMade == 0:
            print('------------')
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break
        else:
            continue
#chay tro choi
hangman('apple')