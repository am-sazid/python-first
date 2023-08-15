'''
# Python List Data Type
     # int type list
li = [12,13,23,43,54,65,76]

print(li)

li[1]=0

print(li)

    # string type list
    
lis = ["sazid " "khalid " "sifat " "arafat"]


print(lis)

    # boolean type list
    
list= [False, True, False, True]

print (type(list))


# Access List Item

sazid = ["facebook", "group", "website", "page" ]

print(sazid[2])

# change list Item

hablu = ["facebook", "group", "website", "page" ]

hablu[2]= "massenger"

print(hablu)


# ADD List Item
    #Append 
    
hablu = ["facebook", "group", "website", "page" ]

hablu.append("my page")
print(hablu)


    # Insert

hablu = ["facebook", "group", "website", "page" ]

hablu.insert(4, " page")

print(hablu)

# The remove() method removes the specified item.

Mylist = ["sazid", "saju", "rifat", "shikto"]

Mylist.remove("sazid")

print(Mylist)


# The pop() method removes the specified index.

Mylist = ["sazid", "saju", "rifat", "shikto"]

Mylist.pop(2)

print(Mylist)


# The del keyword also removes the specified index:

Mylist = ["sazid", "saju", "rifat", "shikto", 420]

Mylist.pop()

print(Mylist)

# The del keyword also removes the specified index:

Mylist = ["sazid", "saju", "rifat", "shikto", 420]

del Mylist[4]

print(Mylist)

# Clear the List

Mylist = ["sazid", "saju", "rifat", "shikto", 420]

Mylist.clear()

print(Mylist)

# You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Use the range() and len() functions to create a suitable iterable
# index number output
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(i)
  
# Use the range() and len() functions to create a suitable iterable
# output string

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  

# Print all items, using a while loop to go through all the index numbers
# trying
Mylist = ["sazid", "saju", "rifat", "shikto", 420]

y= 0

while y < len(Mylist):
    print(Mylist[y])
    y = y + 1
''' 
# w3 school

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1