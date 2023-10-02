from random import *

for A in range(1,6):
    guessnumber = int(input("Enter guessnumber (1,5): "))
    randomnumber = random.randint(1,5)
    
    if guessnumber==randomnumber:
        print("You have won ")
        
    else :
        print("You have lost")
        print("Random number : ",randomnumber)