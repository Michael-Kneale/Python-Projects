from random import shuffle #imports shuffle from the random module, so that later on the order of values in an array can be randomised

score = 0 #sets the player's score to 0 (done outside as well as inside the run function so that the score resets whenever someone completes the quiz)
questionNumber = 1 #sets the question number to 0 (" ")


def run(): #the function that executes the quiz
    print('Please enter your name.') #prompts the user to enter their name
    name = input() #whatever the user inputs becomes their name, which they will be referred to as from now on
    print(f'Welcome to the software quiz, {name}!')
    global score #makes sure the score is consistent inside and outside functions
    score = 0 #sets the score to 0
    global questionNumber #makes sure the question number is consistent inside and outside functions
    questionNumber = 1 #sets the question number to 1

    def q1(): #the function for one of the questions (not necessarily the one that comes first)
        global questionNumber #grabs the questionNumber value from outside this function; may be anywhere from 1 to 20 depending on when this question comes up
        print(f'\n{questionNumber}. What is an example of a programming language?') #shows the user the question they need to answer
        print('A: Python') #answer option 1
        print('B: Chrome') #answer option 2
        print('C: Microsoft') #answer option 3
        print('D: Anaconda') #answer option 4
        questionNumber += 1 #the question number after this will be 1 higher
        answer = input() #sets the user's input to the value 'answer'; this is done because if we had 'input()' twice on the next line (instead of 'answer'), Python would try to accept two additional inputs from the user, messing up the program
        if answer == 'A' or answer == 'a': #only executes if the question is answered correctly, and allows for upper case and lower case responses
            print('Correct.') #provides immediate feedback to the user so that they know they answered correctly
            global score #grabs the score value from outside this function
            score += 1 #adds 1 to the player's overall score thus far
            print(f'Your score is {str(score)}.') #shows the player their current score
        else: #executes if the question was answered incorrectly, that is, if their input was anything other than 'A' or 'a'
            print('Incorrect; the correct answer was A.') #provides immediate feedback to the user so that they know they answered incorrectly

    def q2(): #this function, as well as those for questions 3 through 20, works the same as the one for question 1
        global questionNumber
        print(f"\n{questionNumber}. What is the study of people's efficiency in their working environment?")
        print('A: economics')
        print('B: Reaganomics')
        print('C: ergonomics')
        print('D: ecology')
        questionNumber += 1
        answer = input()
        if answer == 'C' or answer == 'c':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was C.')

    def q3():
        global questionNumber
        print(f'\n{questionNumber}. How long does copyright last for?')
        print('A: 50 years')
        print('B: the life of the author')
        print('C: the life of the author plus 70 years')
        print('D: the life of the author plus 50 years')
        questionNumber += 1
        answer = input()
        if answer == 'C' or answer == 'c':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was C.')

    def q4():
        global questionNumber
        print(f'\n{questionNumber}. What does CPU stand for?')
        print('A: central periphery unit')
        print('B: central processing unit')
        print('C: centred process unit')
        print('D: central printing unit')
        questionNumber += 1
        answer = input()
        if answer == 'B' or answer == 'b':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was B.')

    def q5():
        global questionNumber
        print(f'\n{questionNumber}. What is 39FE in binary form?')
        print('A: 1011 0111 1001 0110')
        print('B: 1101 1111 1010 1011')
        print('C: 0001 0011 0101 1010')
        print('D: 0011 1001 1111 1110')
        questionNumber += 1
        answer = input()
        if answer == 'D' or answer == 'd':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was D.')

    def q6():
        global questionNumber
        print(f'\n{questionNumber}. What is 1010 1101 in decimal form?')
        print('A: 173')
        print('B: 158')
        print('C: 125')
        print('D: 64')
        questionNumber += 1
        answer = input()
        if answer == 'A' or answer == 'a':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was A.')

    def q7():
        global questionNumber
        print(f'\n{questionNumber}. What is a while loop an example of?')
        print('A: a data type')
        print('B: a control structure')
        print('C: a script')
        print('D: a character')
        questionNumber += 1
        answer = input()
        if answer == 'B' or answer == 'b':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was B.')

    def q8():
        global questionNumber
        print(f'\n{questionNumber}. What can hardware be defined as?')
        print('A: the instructions controlling the actions of and directing the hardware')
        print('B: all the actions performed by the personnel to operate the system or support the operating system')
        print('C: the raw inputs that are transformed by the system into information')
        print('D: the physical elements of the computer system')
        questionNumber += 1
        answer = input()
        if answer == 'D' or answer == 'd':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was D.')

    def q9():
        global questionNumber
        print(f'\n{questionNumber}. Which of the following is an example of software?')
        print('A: graphics cards')
        print('B: video games')
        print('C: keyboards')
        print('D: news.com.au')
        questionNumber += 1
        answer = input()
        if answer == 'B' or answer == 'b':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was B.')

    def q10():
        global questionNumber
        print(f'\n{questionNumber}. Which of the following would cause a program to encounter a runtime error?')
        print('A: missing quotation mark')
        print('B: division by zero')
        print('C: misspelt keyword')
        print('D: missing parenthesis')
        questionNumber += 1
        answer = input()
        if answer == 'B' or answer == 'b':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was B.')

    def q11():
        global questionNumber
        print(f'\n{questionNumber}. What kind of operations does the arithmetic logic unit carry out?')
        print('A: qualitative and descriptive')
        print('B: imaginary')
        print('C: mathematical and logical')
        print('D: mechanical')
        questionNumber += 1
        answer = input()
        if answer == 'C' or answer == 'c':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was C.')

    def q12():
        global questionNumber
        print(f'\n{questionNumber}. What level of language is third-generation programming?')
        print('A: high-level')
        print('B: low-level')
        print('C: medium-level')
        print('D: none of the above')
        questionNumber += 1
        answer = input()
        if answer == 'A' or answer == 'a':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was A.')

    def q13():
        global questionNumber
        print(f'\n{questionNumber}. What are rectangles used for in data flow diagrams?')
        print('A: processes')
        print('B: flow of data')
        print('C: data storage')
        print('D: external entities')
        questionNumber += 1
        answer = input()
        if answer == 'D' or answer == 'd':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was D.')

    def q14():
        global questionNumber
        print(f'\n{questionNumber}. What is someone called who uses software and provides feedback to the developer on its usefulness?')
        print('A: tester')
        print('B: pilot')
        print('C: programmer')
        print('D: systems analyst')
        questionNumber += 1
        answer = input()
        if answer == 'A' or answer == 'a':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was A.')

    def q15():
        global questionNumber
        print(f'\n{questionNumber}. What is the first step in the structured approach to software development?')
        print('A: modifying the solution')
        print('B: checking the solution')
        print('C: defining the problem')
        print('D: building the solution')
        questionNumber += 1
        answer = input()
        if answer == 'C' or answer == 'c':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was C.')

    def q16():
        global questionNumber
        print(f'\n{questionNumber}. In which software development approach are the user and the developer one and the same?')
        print('A: structured')
        print('B: end-user')
        print('C: RAD')
        print('D: agile')
        questionNumber += 1
        answer = input()
        if answer == 'B' or answer == 'b':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was B.')

    def q17():
        global questionNumber
        print(f'\n{questionNumber}. In Python, what are the two Boolean values?')
        print('A: False and True')
        print('B: 1 and 2')
        print('C: 0 and 1')
        print('D: Off and On')
        questionNumber += 1
        answer = input()
        if answer == 'A' or answer == 'a':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was A.')

    def q18():
        global questionNumber
        print(f"\n{questionNumber}. What does 'IPO' stand for in IPO chart?")
        print('A: Io, Python, Oriel')
        print('B: Input, Process, Output')
        print('C: In, Prototype, Out')
        print('D: Integer, Program, On')
        questionNumber += 1
        answer = input()
        if answer == 'B' or answer == 'b':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was B.')

    def q19():
        global questionNumber
        print(f'\n{questionNumber}. What are some important things to take into consideration when designing a program to be inclusive?')
        print('A: age, disabilities, and sex')
        print('B: hobbies, likes, and dislikes')
        print('C: height, weight, and fitness')
        print('D: nothing should be taken into consideration')
        questionNumber += 1
        answer = input()
        if answer == 'A' or answer == 'a':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was A.')

    def q20():
        global questionNumber
        print(f'\n{questionNumber}. Which of the following statements is true?')
        print('A: = and == are both assignment operators')
        print('B: = is an equality operator and == is an assignment operator')
        print('C: = and == are both equality operators')
        print('D: = is an assignment operator and == is an equality operator')
        questionNumber += 1
        answer = input()
        if answer == 'D' or answer == 'd':
            print('Correct.')
            global score
            score += 1
            print(f'Your score is {str(score)}.')
        else:
            print('Incorrect; the correct answer was D.')

    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20] #puts all the question functions in an array
    shuffle(questions) #randomises the order of all of the question functions
    for func in questions: #the following line of code occurs for every function in the array above
        func() #the function runs (in this case, every function runs, due to the preceding line)

    score2 = f'{str(score / 20 * 100)}%' #calculates the score as a percentage

    print(f'\n{name}, your final score is {str(score)} out of 20, or {score2}.') #provides the user with their score out of 20 and as a percentage

    score3 = score / 20 * 100 #allows the calculation of the user's grade to be easily understood

    if score3 >= 90: #if the players score is equal to or above 90%...
        print('Your grade is an A.')#...they are told that their grade is an A
    elif score3 >= 80:
        print('Your grade is a B.')
    elif score3 >= 70:
        print('Your grade is a C.')
    elif score3 >= 60:
        print('Your grade is a D.')
    elif score3 >= 50:
        print('Your grade is an E.')
    else:
        print('Your grade is an F.')
    print('(F = 0-50%, E = 50-60%, D = 60-70%, C = 70-80%, B = 80-90%, A = 90-100%)') #shows the user the critera for all the different grades


    print("Press 'x' to exit the program, or press any other button to restart the quiz.")
    decision = input()
    if decision == 'x' or decision == 'X': #only executes if the user presses 'x'
        exit() #exit the program
    else: #if the user presses anything other than 'x'
        run() #run the program again

    print() #inserts a blank space between the end of a quiz and the beginning of a new one, for the sake of cleanliness and being user-friendly
    print() #same as the line above


run() #runs the quiz for the first time
