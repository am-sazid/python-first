# 1 + 2 + 3 + .....+ n

n = int(input("Enter n number : "))
sum = 0

for x in range(1,n+1,2):
    sum = sum + x*x
    
print(sum)

# 1 x 2 x 3 x ......+n
n = int(input("Enter n number : "))
sum = 2

for x in range(1,n+1,2):
    sum = sum * x
    
print(sum)