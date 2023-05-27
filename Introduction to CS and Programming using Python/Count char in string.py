def count(string):
    Dict = {}
    for char in string:
        if char in Dict:
            Dict[char] += 1
        else:
            Dict[char] = 1
    return Dict
print(count('abfhjdfsjkhfkdajflfjashfjdshf'))