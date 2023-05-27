# Cac chu cai va diem so tuong duong
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Cho biet diem so cua chu cai
#letter: chu cai can tim diem so
def SCRABBLE_LETTER_VALUES(letter):
    index = letters.index(letter)
    return points[index]

# Tim diem so cua tu
# word: tu da cho
# n: so chu
def getWordScore(word, n):
    # Neu tu khong co chu nao thi tra ve 0
    if len(word) == 0:
        return 0
    # Gia tri khoi diem
    wordScore = 0
    lettersUsed = 0
    # Tim va cong diem cua cac chu cai trong tu
    for letter in word:
        wordScore += SCRABBLE_LETTER_VALUES(letter.capitalize())
        lettersUsed += 1
    # Tinh so diem
    wordScore *= lettersUsed
    if lettersUsed == n:
        wordScore += 50
    return wordScore

print(getWordScore('apple', 7))
