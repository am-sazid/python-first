class Student :
    roll = ""
    cgpa = ""
    
    def __init__(self,roll,cgpa):
        self.roll = roll
        self.cgpa = cgpa
    def display(self):
        print(f"Rool = {self.roll}, Cgpa = {self.cgpa}")
        
karim = Student(101,3.75)
karim.display()

