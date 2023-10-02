# xargs

def student(*details):
    print(details)
    
student(102,"sazid",4.85)

def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)
        
add(20,50,30)
add(10,20,30,40)

# xxargs

def student(**details):
    print(details["id"])
    
student(id=101,name="Sazid")