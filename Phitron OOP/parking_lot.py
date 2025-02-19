class Car:
    def __init__(self, license, model, color):
        self.license = license
        self.model = model
        self.color = color
    
    def __repr__(self):                                # representational string = jokon akta string ka organize way ta akta formal way ta rakta chai tokon ai dunder method used kori.
        return f"{self.license},{self.model},{self.color}"
       

# __repr__ = formal string, not readable thaka amra access kora kothin but python access korta para esay.
# str(__repr__) = readable formate string deya dai easy.


class Garage:
    def __init__(self):
        self.car_added = []                             # ka ka kon kon user car gula rakcha tader info gula alada kora store kora hoba. = [['123', 'VHMY89', 'Red'], ['12345', 'ABDS89', 'Blue']]        
        self.spot = 10
        self.car_infos = {}                             # jai user aslo tar [licence, model, color, ticket aigulo] takba . Ai tai identify korta easy hoba. ai ta user dakba na.
        # self.bill = 0
        # self.ticket = []                                # akta string takba. ai tar shata joge kora hoba license number ta.
 
    def spots_available(self):
        return f"Total Spots Avalilable {self.spot}"
    
    def add_car_to_garage(self, car):
        self.spot_name = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1']
        if self.spot > 0:
            user_data = str(car).split(",")            # self.car_added ar moddha nested list takba saita ai khana create hoccha.
            self.spot -=1
            self.car_added.append(user_data)
            self.car_infos = {'Tickets' : [], 'License' : [], 'Model' : [], 'Color' : []}
            ticket = ""
            
            for i, val in enumerate(self.car_added):      # [[index = 0], [index = 1], [index = 2], [index = 3], [index = 4]]   Nested List akara index ways value takba.
                ticket = self.spot_name[i] + val[0]
                self.car_infos['Tickets'].append(ticket)
                self.car_infos['License'].append(val[0])
                self.car_infos['Model'].append(val[1])
                self.car_infos['Color'].append(val[2])
            print(f"Successfully Parked!!!!! YOUR TICKET {ticket}")
        else:
            print("NO SPOTS AVAILABLE!!!!!!!!!")
            
    def unpark(self, ticket, hours):
        if ticket not in self.car_infos['Tickets']:      #Security check purpose O(N)
            print("NO CAR FOUND!!!!!!")
            return
        else:
            for i, val in enumerate(self.car_infos['Tickets']):    #O(N)
                if val == ticket:
                    print(f"YOUR LICENSE IS {self.car_infos['License'][i]}")
                    print(f"YOUR MODEL IS {self.car_infos['Model'][i]}")
                    print(f"YOUR COLOR IS {self.car_infos['Color'][i]}")
                    
                    removed_car_index = i
                    self.car_infos['License'].pop(i)
                    self.car_infos['Model'].pop(i)
                    self.car_infos['Color'].pop(i)
                    self.car_infos['Tickets'].pop(i)
                    self.spot += 1
        if hours > 30:
            print(f"Total Bill =${hours*5 + 100}")
        else:
            print(f"Total Bill =${hours*5}")        
    
    def total_cars_in_garage(self):
        for i in self.car_infos.items():
            print(i)    
                
                
my_garage = Garage()
print("***************WELCOME TO OUR PARKING SYSTEM*********************")

while True:
    print("What do you want ? ")
    print("1. Park you car \n2. Check Available Space \n3. Unpark Your Car \n4. Total Cars in Garage")
    user_choice = int(input("Enter your Choice : ")) 
    if user_choice == 1:
        car_license = input("Enter your car license: ")
        car_model = input("Enter your car model: ")
        car_color = input("Enter your car color: ")
        user_car = Car(car_license, car_model, car_color)          # Car class object
        my_garage.add_car_to_garage(user_car)
        print()
    elif user_choice == 2:
        print(my_garage.spots_available())
        print()
    elif user_choice == 3:
        ticket = input("Enter your ticket number : ")
        hours = int(input("Enter hours :  "))
        if my_garage.spot == 10:
            continue
        else:
            my_garage.unpark(ticket, hours)
        print()
    elif user_choice == 4:
        my_garage.total_cars_in_garage()
    else:
        break







# my_car1 = Car("123MM", "Land Crouger", "Red")
# my_car2 = Car("156Tyd", "TOYOTA", "BLUE")
# my_garage.add_car_to_garage(my_car1)
# my_garage.add_car_to_garage(my_car2)
# my_garage.total_cars_in_garage()      
# my_garage.unpark("A1123MM", 12)
# my_garage.total_cars_in_garage()
# my_garage.unpark("B1156Tyd", 70)
# my_garage.total_cars_in_garage()      
 
 