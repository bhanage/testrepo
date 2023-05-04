dictionary = {} #initialize pne dictionary

for i in range(5): #we have total 5 keys
     print(f"Enter the data for {i}:- ")  #for i'th index 
     key = input("Enter the key: ") #accept the key
     if key == "age": #if the key is age 
        value = int(input("Enter the value: ")) #accept it in integer format
     elif key == "salary": #if the key is salary
         value = float(input("Enter the value: ")) #accept it in float format
     else: 
        value = input("Enter the value: ") #accept for string format
    
     dictionary[key] = value #store the data in the form of key value in dictionary
     
print(dictionary) #display the dictionary