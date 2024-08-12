str = "New Horizon College Of Engineering @#$%^&*"
lower = 0
upper = 0
others = 0
spaces = 0
for i in str:
    if(i.isupper()):
        upper+=1
    elif(i.islower()):
        lower+=1
    elif(i.isspace()):
        spaces+=1
    else:
        others+=1
print("The number of uppercase characters: ",upper)
print("The number of lowercase characters: ",lower)
print("The number of  spaces: ",spaces)
print("The number of other characters: ",others)
print("The toggled case sentence is ",str.swapcase())
print("The toggled case sentence is ",str.lower())
print("The toggled case sentence is ",str.upper())
print("The toggled case sentence is ",str.title())
print("The toggled case sentence is ",str.capitalize())
