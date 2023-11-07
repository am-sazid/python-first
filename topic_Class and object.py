class Student :
    roll = ""
    cgpa = ""
    
# rahim = Student()
# print(isinstance(rahim,Student))

rahim = Student()
rahim.roll = 101
rahim.cgpa = 3.70
print(f"Rool = {rahim.roll}, Cgpa = {rahim.cgpa}")

karim = Student()
karim.roll = 102
karim.cgpa = 3.75
print(f"Rool = {karim.roll}, Cgpa = {karim.cgpa}")


# introducing method
class Student :
    roll = ""
    cgpa = ""
    
    def set_value(self,roll,cgpa):
        self.roll = roll
        self.cgpa = cgpa
    def display(self):
        print(f"Rool = {self.roll}, Cgpa = {self.cgpa}")
        
karim = Student()
karim.set_value(102,3.75)
karim.display()


    