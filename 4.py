import re
class hpc_2023_lab_exam:
    admitted_student = []
    def __init__(self,student_name) -> None: #calling init method for classs
        self.student_name = student_name
    
    def verify_cdac_student(self):
        
        pattern = "^[cdac].*.[pune]$"  #pattern start with cdac and end with pune
        result = re.search(pattern,self.student_name.lower()) #search for pattern in student name
        if result:
            try:
                with open("student_data.txt","a") as f: #open the file in append
                    f.write(self.student_name+"\n")
                             
            except:
                print("cannot write into the file!")
        else:
            print("Invalid student entry!") #if pattern not followed
    
    
    def read_student_details_from_file(self):
        try:
            print("Data from student_data.txt:- ")
            with open("student_data.txt") as fr: #open the file in read mode
                    hpc_2023_lab_exam.admitted_student = fr.readlines() #read the lines
                    for i in hpc_2023_lab_exam.admitted_student:  #store the student names in list admitted student and iterated
                        print(i.strip()) #display in output file is appended
        except FileNotFoundError:
            print("File not found!")
            
            
            
            
class hpc_2023(hpc_2023_lab_exam):
    
    def __init__(self, student_name) -> None:
        super().__init__(student_name)
        #print(hpc_2023_lab_exam.admitted_student) 
    
    def display_student_name_with_status(self): 
        for i in hpc_2023_lab_exam.admitted_student: #list of the admitted students from parent class
            print(i.strip()+"_active") #concatenate active with each student name 

def main():
    print("***************In parent class hpc_2023_lab_exam*************")    
    student_name = input("Enter the name for student: ")          
    hpc = hpc_2023_lab_exam(student_name) #create object for the class
    hpc.verify_cdac_student() #function to verify student name and append in file
    hpc.read_student_details_from_file()   #function to read the file and display
    
    print("********In child class hpc_2023***************")
    #creating object for child class
    hpc_child = hpc_2023(student_name) 
    hpc_child.display_student_name_with_status() #function to display student list and concatenate their status
    

main() #calling method main