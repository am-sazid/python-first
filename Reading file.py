file = open ("student.txt","r+")

print(file.readable())
file.close()

file = open("student.txt","r")

text = file.read()
print(text)
size = len(text)
print(size)

file.close()

file = open ("student.txt","r+")

text = file.readlines()[0]

print(text)
file.close()

file = open ("student.txt","r+")

for line in file:
    print(line)
    
file.close()