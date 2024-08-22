# questions = [
#     ["Who is the main antagonist in The Avengers(2012)?", "Loki", "Thanos", "Ultron", "Red Skull", 1],
#     ["What is the name of Tony Stark's AI assistant?", "J.A.R.V.I.S.", "F.R.I.D.A.Y.", "H.O.M.E.R.", "A.L.F.R.E.D.", 1],
#     ["Which Infinity Stone is embedded in Vision's forehead?", "Space Stone", "Reality Stone", "Mind Stone", "Time Stone", 3],
#     ["Who directs Avengers: Infinity War 2018 and Avengers: Endgame 2019?", "Joss Whedon", "James Gunn", "Russo Brothers", "Taika Waititi", 3]
# ]

# rslevel = [1000, 2000, 3000, 4000]
# money = 0

# for i in range(len(questions)):
#     Q = questions[i]
#     print(f"\n\nQuestion for Rs. {rslevel[i]}")
#     print(questions[i][0])
#     print(f"a. {Q[1]}          b. {Q[2]} ")
#     print(f"c. {Q[3]}          d. {Q[4]} ")
#     reply = input("Enter/type your answer or 0 to quit:\n")
#     if reply == '0':
#         money = rslevel[i-1]
#         print(f"you won rs {money}")
#         break
#     if reply == str(Q[5]) :
#         print(f"Correct answer! You have won Rs. {rslevel[i]}")
#     else:
#         print("Wrong answer!")
#         break
# else:
#     print("Congratulations! You've answered all the questions correctly!")



# STONE PAPER SCISSORS 

import random

player = int(input("1 for stone 2 for paper and 3 for scissors:"))

comp = random.randint(1 , 3)

def game(comp , player):
    if (comp==player):
        return 0
    if(comp==1 and player==2):
        return 1
    if(comp==2 and player==3):
        return 1
    if(comp==3 and player==1):
        return 1
    
    return -1

score = game(comp ,player)

print("you:" , player)
print("computer:" , comp)

if (score==0):
    print("darw")
elif score == 1 :
    print("you won")
else:
    print("you lose") 

print("play again")   


# "LIBRARY MANAgement

    
# class Library:
#   def __init__(self):
#     self.noBooks = 0
#     self.books = []
    
#   def addBook(self, book):
#     self.books.append(book)
#     self.noBooks = len(self.books)

#   def showInfo(self):
#     print(f"The library has {self.noBooks} books. The books are")
#     for book in self.books:
#       print(book)


# l1 = Library()
# l1.addBook("Harry Potter1")
# l1.addBook("naruto")
# l1.addBook("onepiece")
# l1.showInfo()
    
  