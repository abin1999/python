class Student:

    def __init__(self, name, branch, mark):
        self.name = name
        self.branch = branch
        self.mark = mark


    def displayStudent(self):
        print ("Name:" + self.name, "branch:"+ self.branch, "mark:" + self.mark)

    def __del__(self):
            print("destructer called student deleted")

stud1 = Student("abin", "mca", "70")
stud2 = Student("akhil", "mca", "65")

stud1.displayStudent()
stud2.displayStudent()