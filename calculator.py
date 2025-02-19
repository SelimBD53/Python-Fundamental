# while True:
#     choise = str(input("Enter Sum for addition,Sub for Subtraction,Mul for Multiplication, Div for divitation, E for exit:  "))
#     if choise in ["Sum", "Sub", "Mul", "Div"]:
#         num1 = int(input("Enter The First Number: "))
#         num2 = int(input("Enter The Second Number: "))
#         if choise == "Sum":
#             print(f"Sum of {num1} and {num2} is {num1+num2}")
#         elif choise == "Sub":
#             print(f"Sub of {num1} and {num2} is {num1-num2}")
#         elif choise == "Mul":
#             print(f"Mul of {num1} and {num2} is {num1*num2}")
#         elif choise == "Div":
#             print(f"Div of {num1} and {num2} is {num1/num2}")
#     elif choise == "E":
#         print("Exit From This Operation.")
#         break
#     else:
#         print("Invalid Operation.")

# nth=int(input("Enter The Position: "))
# if nth<=0:
#     print("Please Correct The Position.")
# elif nth==1:
#     print(0)
# else:
#     sum = 0
#     next_value = 1
#     for number in range(2, nth):
#         sum, next_value = next_value, sum+next_value 
        
#         print("sum=", sum)
#         print("next_value=", next_value)
#         print("=====================================")

#        0 1 1 2 3 5 8
#indx =  1 2 3 4 5 6 



















import json
import random

def quiz_mode():
    try:
        with open("vocabulary.json", "r") as file:
            vocabulary = json.load(file)
    except FileNotFoundError:
        print("Vocabulary file not found!")
        return

    if not vocabulary:
        print("The vocabulary is empty!")
        return

    words = list(vocabulary.keys())
    random.shuffle(words)
    score = 0

    for word in words:
        # Randomly choose whether to ask using Meaning or Example
        question_type = random.choice(["Meaning", "Example"])
        question_text = vocabulary[word][question_type]

        print(f"{question_type}: {question_text}")
        answer = input("What's the word? ").strip()

        if answer == word:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct word was: {word}")

    print(f"Your score: {score}/{len(words)}")

Call the quiz mode function
quiz_mode()
