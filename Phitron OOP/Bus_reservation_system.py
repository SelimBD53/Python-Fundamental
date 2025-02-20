class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class Bus:
    def __init__(self, Coach, driver, arrival, departure, from_des, to):
        self.Coach = Coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(20)]

class PhitronCompany:         # Bus install kora hoba for admin.
    total_bus = 5
    total_bus_lst = []  #Dummy Database     // ai ta Static variable.
    
    def install(self):
        bus_no = int(input("Enter Bus No: "))
        flag = 1
        
        for bus in self.total_bus_lst:     # Checking korchi already kono bus install acha ki na.
            if bus_no == bus['Coach']:       # bus["Coach"]= 12, 10
                print("Bus already Installed")
                flag = 0
                break
        
        if flag:
            bus_driver = input("Enter Bus Driver Name : ")
            bus_arrival = input("Enter Bus Arrival Time : " )
            bus_departure = input("Enter Bus Departure Time : ")
            bus_from = input("Enter Bus Start From : ")
            bus_to = input("Enter Bus Destination To : ")
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival, bus_departure, bus_from, bus_to)
            self.total_bus_lst.append(vars(self.new_bus))
            print("\n Bus Installed Successfully.\n")
            
class BusCounter(PhitronCompany):         # user or countre officer tar jonno ai ta
    user_lst = []  # user database
    bus_seat = 20
    def reservation(self):
        bus_no = int(input("Enter Bus Number : "))
        flag = 1 
        for bus in self.total_bus_lst:
            if bus_no == bus["Coach"]:
                passenger = input("Enter Your Name : ")
                seat_no = int(input("Enter Your Seat Number : "))
                if seat_no-1 > BusCounter.bus_seat:         # maximum seat checking
                    print("Only 20 seats are Available.")
                elif bus["seat"][seat_no-1] != "Empty":         # not empty ki na
                    print("Seat Already Booked.")
                else:
                    bus["seat"][seat_no-1] = passenger     # oi seat a oi passanger ka bosaiya decchi.
            else:
                flag = 0
                break
        if flag == 0:
            print("No Bus Available.")    
        
    def showBusInfo(self):                    # Akta bus ar information.
        bus_no = int(input("Enter Bus No : "))
        for bus in self.total_bus_lst:
            if bus["Coach"] == bus_no:
                print("*"*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                print(f"Bus Number : {bus_no} \t\t Driver : {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t\t\t Departure : {bus['departure']}")
                print(f"From : {bus['from_des']} \t\t\t To : {bus['to']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print("\t", end="")
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()
    def get_users(self):
        return self.user_lst  
    
    def create_account(self):
        name = input("Enter your name : ")
        flag = 0
        for user in self.get_users():
            if user.username == name:
                print("Username already exists")
                flag = 1
                break
        if flag == 0:
            password = input("Enter your password : ")
            self.new_user = User(name, password)
            self.user_lst.append(vars(self.new_user)) 
            print("Account created successfully")     
    
    def available_buses(self):          # All bus information
        if len(self.total_bus_lst) == 0:
            print("No Bus Available")
        else:                          # Bus Available Acha.
            for bus in self.total_bus_lst:
                print("*"*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {bus['Coach']} {'#'*10}")
                print(f"Bus Number : {bus['Coach']} \t\t Driver : {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t\t\t Departure : {bus['departure']}")
                print(f"From : {bus['from_des']} \t\t\t To : {bus['to']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print("\t", end="")
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end="\t")
                        a += 1
                    print()
     
while True:
    counter = BusCounter()
    print("1. Create An Account \n2. Login To Your Account \n3. EXIT")
    user_input = int(input("Enter Your Choice : "))
    if user_input == 3:
        break
    elif user_input == 1:
        counter.create_account()
    elif user_input == 2:
        name = input("Enter your name : ")
        password = input("Enter your password : ")
        isAdmin = False
        flag = 0
        if name == "admin" and password == "123":
            isAdmin = True
            
        if isAdmin == False:                        # Normal user/ customer 
            for user in counter.get_users():        # username, password == database a ache kina.
                if user['username'] == name and user['password'] == password:
                    flag = 1            # authentic user.
                    break         
            if flag:
                while True:
                    print("1. Available Buses \n2. Show Bus Infp \n3. Reservation \n4. EXIT")
                    user_choice = int(input("Enter Your Choice : "))
                    if user_choice == 4:
                        break
                    elif user_choice == 1:
                        counter.available_buses()
                    elif user_choice == 2:
                        counter.showBusInfo()
                    elif user_choice == 3:
                        counter.reservation()
            else:
                print("Ara vai ka tumi??? ki choue.") 
        else:
            while True:
                print("Hello Admin, Welcome back")
                print("1. Install Bus \n2. Available Buses \n3. Show Bus \n4. Show User list \n5. EXIT")            
                a = int(input("Enter Your Choice : "))
                if a == 5:
                    break
                elif a == 1:
                    counter.install()
                elif a == 2:
                    counter.available_buses()
                elif a == 3:
                    counter.showBusInfo()
                elif a == 4:
                    counter.get_users()

# 1. create an account -> create_new_account()  []
# 2. login to your account -> authentic User
#                          -> 1. Available buses
#                          -> 2. Reservation
#                          -> 3. Show bus info
                         
#                          -> Administrator
#                          -> 1. Install Buses
#                          -> 2. See available buses
#                          -> 3. See total userList
# 3. exit    

                  
# {"Coach": 12, "driver": "Naim", "arrival": "12PM", "departure": "12:30PM", "form":"Dhaka", "to": "Khulna"}

# [10, "Naim", "12Pm", "12:30PM", "Dhaka", "Khulna"]

# [{"Coach": 12, "driver": "Naim", "arrival": "12PM", "departure": "12:30PM", "form": "Dhaka", "to": "Khulna"}, 
# {"Coach": 10, "driver": "Naim", "arrival": "12PM", "departure": "12:30PM", "form": "Dhaka", "to": "Khulna"}]

# a = Bus(10, "Naim", "12Pm", "12:30PM", "Dhaka", "Khulna")
# print(vars(a))

