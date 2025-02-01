
questions =  ("1. What has the most Eye Color? " 
             ,"2. How many days in a week? " 
             ,"3. How many days in a year? " 
             ,"4. Who is the president of the Philippines? " 
             ,"5. What is the next big thing? ")

options = (("A. Red" , "B. Blue" , "C. Green" , "D. Brown") 
          ,("A. 5" , "B. 10" , "C. 12" , "D. 7") 
          ,("A. 340" , "B. 1200" , "C. 365" , "D. 563") 
          ,("A. Duterte" , "B. Joe Biden" , "C. Marcos" , "D. Joe Mama")
          ,("A. Your Hat" , "B. Gaming" , "C. AI" , "D. Rockets"))

answers = ("B" , "D" , "C" , "C" , "C")
guesses = []
score = 0


#Quiz App

question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answers")
    
    question_num += 1

if score < 3:
    print("----------------------------")
    print("----------RESULTS-----------")
    print(f"Your score is {score} out of 5! You need to study more")
else:
    print("----------------------------")
    print("----------RESULTS-----------")
    print(f"Your score is {score} out of 5! Well played")