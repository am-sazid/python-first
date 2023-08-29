# if else Statement

marks = 80

if marks >= 33:
    print("pass")
    
else:
    print("fail")
    
    
# largest number

num1 = 20
num2 = 10

if num1>num2 :
    print(num1)
    
else:
    print(num2)
    
# even condition

num = 4

if num %2 == 0:
    print("even")
    
else:
    print("odd")
    
    
# odd condition

num = 5

if num %2 == 0:
    print("even")
    
else:
    print("odd")
    
    
# elif Statement

marks =int(input("enter marks"))

if marks>= 80:
    print("A+")
    
elif marks>= 70:
    print("A")
    
elif marks>= 60:
    print("A-")
    
elif marks>= 50:
    print("B")
    
elif marks>= 40:
    print("C")
    
elif marks >= 33:
    print("D")
    
else :
    print("F")
    
# inner if 

num1 = 20
num2 = 50
num3 = 40

if num1 > num2 :
    if num1 > num3:
        print(num1)    
    else :
        print(num3)
        
if num2 > num1 :
    if num2 > num3:
        print(num2)
    else : 
        print(num3)