str_input = "Q2 sec Python Lab New Horizon College Of Engineering"
words = str_input.split()
dictionary = {}
for word in words:
    if(word[0] not in dictionary.keys()):
        dictionary[word[0]]=[]
        dictionary[word[0]].append(word)
    else:
        if(word not in dictionary[word[0]]):
            dictionary[word[0],append(word)]
print(dictionary)
