# Website pynative.com

s = input("Enter a text of number : ")

list = s.split()
sum = 0

for num in list:
    sum = sum + int(num)
    
print(sum)


numberofwords = 0
numberofletter = 0
numberofdigits = 0

s = input("Enter a text of number : ")

for x in s:
    x = x.lower()
    if x >= 'a' and x <= 'z' :
        numberofletter = numberofletter + 1
    
    elif x >= '0' and x <= '9' :
        numberofdigits = numberofdigits + 1
        
    elif x == ' ':
        numberofwords = numberofwords + 1
        
print(numberofletter)
print(numberofdigits)
print(numberofwords + 1)