questions = [
    [
        "Which symbol is used to start a comment in Python?", "Slash", "Hash", "Semicolon", "Colon", 2
    ],

    [
        "Which programming language is known for its use in web development along with HTML and CSS?", "Java", "C#", "JavaScript", "Swift", 3
    ],

    [
        "Who is known as the father of the computer?", "Turing", "Jobs", "Babbage", "Gates", 3
    ],

    [
        "What does HTML stand for?", "Hypertext", "Hyperloop", "Hyperlink", "Hyperspace", 1
    ],
    [
        "What is the term for a loop that never ends?", "Finite", "Recursive", "Infinite", "Conditional", 3
    ],

    [
        "What does JSON stand for?", "JavaScript", "Jumbled", "Java", "Jumbo", 1
    ],
    [
        "What does SQL stand for?", "Simple Query Language", "Structured Query Language", "Sequential Query Language", "Syntax Query Language", 2
    ],
    [
        "Which company developed the Java programming language?", "Microsoft", "Apple", "Google", "Sun", 4
    ],
    [
        "Which programming language was developed by Guido van Rossum?", "Java", "Ruby", "Python", "PHP", 3
    ],
    [
        "What was the first personal computer introduced by IBM?", "PC", "Mac", "Altair", "Commodore", 1
    ],
    [
        "What is the name of the process of finding and fixing errors in software code?", "Compiling", "Debugging", "Encrypting", "Parsing", 2
    ],
    [
        "What is the name of the first high-level programming language?", "COBOL", "BASIC", "Fortran", "Pascal", 3
    ],
    [
        "Who is known as the creator of Linux?", "Gates", "Torvalds", "Zuckerberg", "Ellison", 2
    ],
    [
        "What is an API?", "Application", "Program", "Protocol", "Interface", 4
    ],
    [
        "Who is the author of 'The C Programming Language?'", "Knuth", "Stroustrup", "Kernighan", "Gosling", 3
    ]
]

level = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print("*** WELCOME TO GoChampionz QUIZ ***")

score = 0
for i in range(len(questions)):
    question = questions[i]

    print()
    print(f"-- QUESTION NUMBER {level[i]} ON YOUR SCREEN --\n")
    print(question[0])
    print()
    print("1.", question[1])
    print("2.", question[2])
    print("3.", question[3])
    print("4.", question[4])

    answer = int(input("Enter your answer (1/2/3/4) or 0 to Quit : "))

    if(answer == 0):
        score = level[i-1]
        break
    elif(answer == question[-1]):
        print("Correct Answer !")
        score = level[i]
    else:
        print("Wrong Answer !")
        print("Exit")
        break

if(answer == 0 or answer == question[-1]):
    print(f"YOU SCORED {score} POINTS")

    if(score>=5 and score<10):    
        print("Congrats, You won BRONZE Star")
    elif(score>=10 and score<15):
        print("Congrats, You won BRONZE and SILVER Stars")
    elif(score == 15):
        print("Congrats, You won BRONZE , SILVER and GOLD Stars")

print("Well Done for your participation\nBEST OF LUCK !!")



