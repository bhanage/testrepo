#Q.1 
string = input("Enter the string : ")
list = []
for i in string:
    if string.count(i) > 1: #check if occurence of the char is more than one 
        if i not in list: #check if element is already exists into list or not
            list.append(i)
print(list)