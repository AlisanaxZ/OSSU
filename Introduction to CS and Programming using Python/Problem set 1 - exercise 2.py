s = 'azcbobobegghakl'
count = 0
for x in range(len(s)):
    if(s[x:x+3] == "bob"):
        count += 1
print("Number of times bob occurs is:", str(count))