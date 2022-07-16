# Question 1 solution:
s = "dabaxyddab"
dict = {}
for ch in s:
    if ch not in dict.keys():
        dict[ch] = 1
    else:
        dict[ch] += 1
print(dict)


# Section '1.a' solution:
for key, value in sorted(dict.items()):
    print(key, "-", value)


# Section '1.b' solution:
reverseDict = {}
for value in dict.values():
    reverseDict[value] = []
    for key in dict.keys():
        if dict[key] == value:
            if key not in reverseDict[value]:
                reverseDict[value].append(key)
print(reverseDict)
