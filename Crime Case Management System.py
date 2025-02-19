import json

def cases_data():
    with open('cases.json', 'r') as file:
        # json.dump(cases_info, file)
        data = json.load(file)
        return data

def view_all_cases(data):
    for key, value in data.items():
        print(f"Case ID: {key}")
        for i, j in value.items():
            if i == "Title":
                print(f"Title: {j}")
            elif i == "Suspects":
                suspet = ", ".join(j)
                print(f"Suspects: {suspet}")
            elif i == "Status":
                print(f"Status: {j}")
        print("\n========================\n")
            
        

def add_new_case(data):
    num = int(input("Enter The add how many cases: "))
    for i in range(num):
        case_id = input("Enter The Case ID: ")
        title = input("Enter The Case Title: ") 
        suspect = input("Enter The Suspect Name(comma-separated): ").split(",")
        status = input("Enter The Case Status: ") 
        
        data[case_id]= {
            "Title": title,
            "Suspects": suspect,
            "Status": status
            }
        with open('cases.json', 'w') as file:
            json.dump(data, file)
    print("New Cases Added Successfully.")

def Updat_status_cases(data):
    case_id = input("Enter The Update Case ID: ")
    for key, value in data.items():
        if case_id ==key:
            value["Status"] = input("Enter The Case Updated Status: ")
    
    with open('cases.json', 'w') as file:
        json.dump(data, file)


def add_suspect_cases(data):
    case_id = input("Enter The Case ID For Add Suspect: ")
    
    for key, value in data.items():
        if case_id == key:
            for sus_key, sus_val in value.items():
                if sus_key == "Suspects":
                    user_input = input("Enter The suspect Name: ").split(",")
                    for val in user_input:
                        if val.strip() not in sus_val:
                            data[case_id]["Suspects"].append(val)
                            with open('cases.json', 'w') as file:
                                json.dump(data, file)
                            print("Suspect Successfully Inserted The Case.")
                        else:
                            print(f"{val} is Already Exist Here in This Case.")


def Search_Open_Cases(data):
    for key, value in data.items():
        # print(value)
        for i,j in value.items():
            if j=="Open":
                print([key, value])
    
def Delete_Case(data):
    case_id = input("Enter The Deleted Case ID: ")
    for key, value in data.items():
        if key == case_id:
            del data[case_id]
            with open("cases.json", "w") as file:
                json.dump(data, file)
            print(f"The Case Number {case_id} is Deleted.")


def Find_specific_suspect(data):
    user_Suspect_Name = input("Enter suspect name: ")
    c=1
    print(f"Cases involving {user_Suspect_Name}:")
    for key, value in data.items():
        for i, j in value.items():
            if i == "Suspects":
                for val in j:
                    if val == user_Suspect_Name:
                        print(f"{c}. {value['Title']} ({key})")
                        c += 1


data = cases_data()

while True:
    print("Choose an option:\n1. View all cases\n2. Add a new case\n3. Update case status\n4. Add suspects to a case\n5. Search open cases\n6. Delete a case\n7. Find cases by suspect\n8. Quit")
    choise = input("Enter your choice: ")
    print("\n")
    if choise == "1":
        print(view_all_cases(data))
        print("\n")
    elif choise == "2":
        add_new_case(data)
        print("\n")
    elif choise == "3":
        Updat_status_cases(data) 
        print("\n")      
    elif choise == "4":
        add_suspect_cases(data)
        print("\n")
    elif choise == "5":
        Search_Open_Cases(data)
        print("\n")
    elif choise == "6":
        Delete_Case(data)
        print("\n")
    elif choise == "7":
        Find_specific_suspect(data)
        print("\n")
    elif choise == "8":
        print("\n")
        print("User Choise the System is of")
        break
    else:
        print("Invalid Choise. Please Correct Choise Input Here.")
        print("\n")
