import json
import random


def load_data():
    with open("vocabulary.json", "r") as file:
        # json.dump(data, file)
        data = json.load(file)
        return data
    
def view_all_word(data):
    for key,value in data.items():
        print("\n")
        print(f"Word: {key}")
        for kyes, val in value.items():
            if kyes=="Meaning":
                print(f"Meaning: {val}")
            elif kyes=="Example":
                print(f"Example: {val}")
        print("\n=======================")

def add_new_word(data):
    input_num = input("Enter The Add Word Number: ")
    for i in input_num:
        word = input("Enter The Word: ")
        F = True
        for key, value in data.items():
            if key == word:
                F = False
                print("The Word is Exist.Another Word Input This.")
                break

        if F == True:
            meaning = input("Enter The Meaning: ")   
            example = input("Enter The Example: ")   
            data[word] = {
                "Meaning": meaning,
                "Example": example,
            }
            with open("vocabulary.json", "w") as file:
                json.dump(data, file)
            print("New Word Added Successfully.")
                 
def Search_Word_Details(data):
    word_input = input("Enter The Searchs Word: ").strip()
    
    f= False
    for key, value in data.items():
        if key.strip() == word_input:
            print("\n")
            print(f"Word: {word_input}")
            f=True
            for i, j in value.items():
                print(f"{i}: {j}")
    if f == False:
        print("\n")
        print("Word Not Found")  
                
def Update_Word(data):
    user_input = input("Enter The Updated Word Name: ").strip()
    input_User_choise = input("What is the Update (Meaning/Example): ").strip()
    for key, value in data.items():
        if key.strip() == user_input:
            for i,j in value.items():
                if i == input_User_choise and i == "Meaning":
                    meaning = input("Enter The Updated Meaning: ") 
                    data[user_input] = {
                        "Meaning": meaning,
                        "Example": value["Example"]
                        }
                    with open("vocabulary.json", "w") as file:
                        json.dump(data, file)
                    print("\n")
                    print(f"{input_User_choise} Update Successfully")
                        
                        
                elif i == input_User_choise and i == "Example":
                    example = input("Enter The Updated Example: ") 
                    data[user_input] = {
                        "Meaning": value["Meaning"],
                        "Example": example,
                        } 
                    with open("vocabulary.json", "w") as file:
                        json.dump(data, file)
                    print("\n")
                    print(f"{input_User_choise} Update Successfully")

def Delete_word(data):
    user_input = input("Enter The Deleted Word Name: ")
    for key, value in data.items():
        if key == user_input:
            del data[user_input]
            with open("vocabulary.json", "w") as file:
                json.dump(data, file)
            print(f"The Word {user_input} Delete Successfully.")
    
def Quiz_Competation(data):

    if not data:
        print("\n")
        print(" Vocabulary Not Exist. Please Some Word Added Them.")
        return

    words = list(data.keys())
    random.shuffle(words)
    Score = 0
    for word in words:
        question_type = random.choice(["Meaning", "Example"])
        question = data[word][question_type]
        
        print(f"{question_type}: {question}")
        user_input = input("What's The Word? ").strip()
        if word == user_input:
            Score += 1
            print(f"Correct! Your Score: {Score}/{len(words)}")
        else:
            print(f"Wrong Answer! Correct Answer was: {word}")
        
    
    






def Export_File(data):
    with open("vocabulary.txt", "w") as file:
        for key, value in data.items():
            file.write(f"Word: {key} \n")
            file.write(f"Meaning: {value['Meaning']}\n")
            file.write(f"Example: {value['Example']}\n")
            file.write("\n")
    print("File Export Successfully.")
        
data = load_data()
 
while True:
    print("Choose an option:\n1. View all words\n2. Add a new word\n3. Search for a word \n4. Update word details\n5. Delete a word\n6. Quiz mode\n7. Export to text file\n8. Quit")
    choise = input("Enter your choice: ")
    print("\n")
    if choise == "1":
        view_all_word(data)
        print("\n")
    elif choise == "2":
        add_new_word(data)
        print("\n")
    elif choise == "3":
        Search_Word_Details(data)
        print("\n")      
    elif choise == "4":
        Update_Word(data)
        print("\n")
    elif choise == "5":
        Delete_word(data)
        print("\n")
    elif choise == "6":
        Quiz_Competation(data)
        print("\n")
    elif choise == "7":
        Export_File(data)
        print("\n")
    elif choise == "8":
        print("\n")
        print("User Choise The System is off.")
        break
    else:
        print("Invalid Choise. Please Correct Choise Input Here.")
        print("\n")
