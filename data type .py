
# string type data 

name = "sazid"

print ("my name is " +name)

# number type data 
  #int type 
num1 = 490

print(type(num1))

  #float type

num2= 4.90 
print(type(num2))

  # complex type 
  
num3 = 490j

print (type(num3))

#Python Boolean Type Data

sazidbool = False

print (type(sazidbool))

x = 10
y = 8
print(x==y)


#  Binary Type Data

  # bytes type

sazidlist= [1,2,3,4,23,124,145,245]
b = bytes(sazidlist)

print(type(b))

  # bytearray
  
sazidli= [1,21,13,144,231,123,133,132,255]

c=bytearray(sazidli)

c[2]= 22

print(c[2])

# None type data

name= None

print(type(name))


# Sequence Type Data
  # list type
li = ["grameen" ,"airtel" , "robi" ,"banglalink"]
li[1]= "btcl"
print(li)
print(type(li))

  # tuple type
  
tup = (5,10,15,20,25)

print(type(tup))

   # range type

ran = range(8)

for i in ran:
  print(i)
  
