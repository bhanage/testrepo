#Q.2
list = [] #list data structure to store array elements
for i in range(11):
    number = int(input("Enter the number: "))
    list.append(number)
tuple_of_numbers = tuple(list)
print(tuple_of_numbers) #we can use tuple data structure because it is immutable.