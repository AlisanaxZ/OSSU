s = "abcdefgabcefcccccc"
l = []
tempo = ""
index = 0

def check(char, string, index):
    tempo = char
    try:
        if int(ord(char[-1])) <= int(ord(s[index + 1])):
            tempo += str(s[index+1])
            check(tempo, string, index+1)
            l.append(tempo)
        else:
            return tempo
    except:
        return tempo
    
for char in s:
    check(char, s , index)
    index += 1

longest = l[0]
for e in l:
    if int(len(e))> int(len(longest)):
        longest = e
print('Longest substring in alphabetical order is:', longest)