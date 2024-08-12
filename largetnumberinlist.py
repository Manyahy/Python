length =int(input("Enter the length of the list :"))
list1 = []
for i in range(length):
    num = int(input("Enter the number "))
    list1.append(num)
print(list1)
sorted_list = sorted(list1)
print(sorted_list)
print("THe largest number is",sorted_list[-1])
print("THe second largest number is",sorted_list[-2])
print("THe smallest number is",sorted_list[0])
