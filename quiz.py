questions = [



   ["Who is the main antagonist in The Avengers(2012)?", "Loki", "Thanos", "Ultron", "Red Skull", 1],
    ["What is the name of Tony Stark's AI assistant?", "J.A.R.V.I.S.", "F.R.I.D.A.Y.", "H.O.M.E.R.", "A.L.F.R.E.D.", 1],
    ["Which Infinity Stone is embedded in Vision's forehead?", "Space Stone", "Reality Stone", "Mind Stone", "Time Stone", 3],
    ["Who directs Avengers: Infinity War 2018 and Avengers: Endgame 2019?", "Joss Whedon", "James Gunn", "Russo Brothers", "Taika Waititi", 3]
]

rslevel = [1000, 2000, 3000, 4000]
money = 0

for i in range(len(questions)):
    Q = questions[i]
    print(f"\n\nQuestion for Rs. {rslevel[i]}")
    print(questions[i][0])
    print(f"a. {Q[1]}          b. {Q[2]} ")
    print(f"c. {Q[3]}          d. {Q[4]} ")
    reply = input("Enter/type your answer or 0 to quit:\n")
    if reply == '0':
        money = rslevel[i-1]
        print(f"you won rs {money}")
        break
    if reply == str(Q[5]) :
        print(f"Correct answer! You have won Rs. {rslevel[i]}")
    else:
        print("Wrong answer!")
        break
else:
    print("Congratulations! You've answered all the questions correctly!")


