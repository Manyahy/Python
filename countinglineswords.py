data = open('C:\\Users\\Admin\\OneDrive\\Desktop\\demo.txt','r')
countlines,countwords,countchar = 0,0,0
for i in data.readlines():
    countlines+=1
    lst=i.split()
    countwords+=len(lst)
    countchar+=len(i.strip('\n'))
print("The no of lines in demo.txt are : ",countlines)
print("The no of words in demo.txt are : ",countwords)
print("The no of characters in demo.txt are : ",countchar)
