
num1 = {1,2,3,4,5}
num2 = set([4,5,6])
num2.add(7)
num2.remove(7)
print(num2)

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)


Empty_set = set()
print(type(Empty_set))

num1 = {1,2,3,4,5}

print(1 in num1)
print(9 in num1)