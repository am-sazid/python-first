# try:
#    list = [20,0,30]
#    sum = list[0] / list[3]
#    print(sum)
#    print("done")
    
# except ZeroDivisionError:
#     print("not possble")
    
    
# except IndexError:
#     print("index error")
    
# finally :
#     print("successful")   
# print("successful")

# # multiple excption
# try :
#     num1 = int(input("enter num1 : "))
#     num2 = int(input("Enter num2 : "))
#     sum = num1 / num2
#     print(sum)
#     print("done")
    
# except (ValueError,ZeroDivisionError) : 
#     print("You have enterd incorret input")
    
# finally:
#     print("thank you finally")
    
    
    
# use raise 

def voter (age):
    if age < 18:
        raise ValueError ("invalid voter")
    return "allowed"
try:
    print(voter(17))
except ValueError as e :
    print(e)