# stak example
books = []
books.append("learn python")
books.append("learn c")
books.append("learn java")
print(books)

books.pop()
print("top book is ",books[-1])

books.pop()
print("top book is ",books[-1])

books.pop()
if not books :
    print("No books left")


# queue example

from collections import deque

bank = deque(["sazid","khalid","saju"])
bank.popleft()
print(bank)


bank.popleft()
if not bank:
    print("no person left")


