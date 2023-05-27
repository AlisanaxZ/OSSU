file = open('Example.txt')
content = file.read()
file.close()
count = 0
for line in content:
    count = count + 1
print(count)
