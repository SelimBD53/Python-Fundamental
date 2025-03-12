import hashlib
from brta import BRTA
from vehicales import Car, Bike, Cng
from ride_manager import uber
from random import random, randint, choice
from threading import Thread
license_autherity = BRTA()


class UserAlreadyExist(Exception):  # ai ta akta coustom user Exceptationn handeling class 
    def __init__(self, email, *args):
        print(f"User: {email} already exists.")
        super().__init__(*args)

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        pwd_encrypted = hashlib.md5(password.encode()).hexdigest()
        already_exists = False 
        with open("user.txt", 'r') as file:
            if email in file.read():
                already_exists = True
                # raise UserAlreadyExist(email)
        file.close()
        
        if already_exists == False:
            with open("user.txt", 'a') as file:
                file.write(f"{email} => {pwd_encrypted}\n")
            file.close()
        # print(self.name, 'user created')
        
    @staticmethod
    def log_in(email, password):
        stored_password = ''
        with open('user.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stored_password = line.split(" ")[2]
        file.close()
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == stored_password:
            print("Valid User")
            return True
        else:
            print("Invalid User")
            return False
        # print("Password Found", stored_password)

class Rider(User):
    def __init__(self, name, email, password, location, balance):
        self.location = location
        self.__trip_history = []
        self.balance = balance
        super().__init__(name, email, password)
        
    def set_location(self, location):
        self.location = location
    
    def get_location(self):
        return self.location
    
    def request_a_trip(self):
        pass
    
    def get_trip_history(self):
        return self.__trip_history
    
    def start_a_trip(self, fare, trip_info):
        print(f"A trip started for {self.name}")
        self.balance -= fare
        self.__trip_history.append(trip_info)


class Driver(User):
    def __init__(self, name, email, password, location, licence):
        super().__init__(name, email, password)
        self.location = location
        self.__trip_history = []
        self.licence = licence
        self.valid_driver = license_autherity.validate_license(email, licence)
        self.earning = 0
        self.vehicle = None
        
    def take_driving_test(self):
        result = license_autherity.take_driving_test(self.email)
        if result == False:
            # print("You are faild. try again!!!!!")
            self.licence = None
        else:
            self.licence = result
            self.valid_driver = True
      
    def register_a_vehicles(self, vehicles_type, license_plate, rate):
        if self.valid_driver is True:
            if vehicles_type == 'car':
                self.vehicles = Car(vehicles_type, license_plate, rate, self)
                uber.add_a_vehicles(vehicles_type, self.vehicles)
            elif vehicles_type == 'bike':
                self.vehicles = Bike(vehicles_type, license_plate, rate, self)
                uber.add_a_vehicles(vehicles_type, self.vehicles)
            else:
                self.vehicles = Cng(vehicles_type, license_plate, rate, self)
                uber.add_a_vehicles(vehicles_type, self.vehicles)
        else:
            pass
            # print("You are not a valid driver.")
            
    def start_a_trip(self, start, destination, fare, trip_info):
        self.earning += fare
        self.location = destination
        trip_thread = Thread(target=self.vehicles.start_driving, args=(start, destination, ))
        trip_thread.start()
        # self.vehicles.start_driving(start, destination)
        self.__trip_history.append(trip_info)
        

rider_1 = Rider('rider1', 'rider1@gmail.com', "rider1", randint(0, 30), 1000)
rider_2 = Rider('rider2', 'rider2@gmail.com', "rider2", randint(0, 30), 5000)
rider_3 = Rider('rider3', 'rider3@gmail.com', "rider3", randint(0, 30), 5000)
rider_4 = Rider('rider4', 'rider4@gmail.com', "rider4", randint(0, 30), 5000)
rider_5 = Rider('rider5', 'rider5@gmail.com', "rider5", randint(0, 30), 5000)

for i in range(1, 100):
    driver_1 = Driver(f'driver_{i}', f'driver{i}@gmail.com', f'driver{i}', randint(0, 100), randint(1000, 9999))
    driver_1.take_driving_test()
    driver_1.register_a_vehicles(choice(['car', 'bike', 'cng']), randint(10000, 99999), 10)

print(uber.get_available_cars())
uber.find_a_vehicles(rider_1, choice(['car', 'bike', 'cng']), randint(1, 100))
uber.find_a_vehicles(rider_2, choice(['car', 'bike', 'cng']), randint(1, 100))
uber.find_a_vehicles(rider_3, choice(['car', 'bike', 'cng']), randint(1, 100))
uber.find_a_vehicles(rider_4, choice(['car', 'bike', 'cng']), randint(1, 100))
uber.find_a_vehicles(rider_5, choice(['car', 'bike', 'cng']), randint(1, 100))

print(rider_1.get_trip_history())
print(uber.total_income())
# hero = User("Hero Alom", "hero@alom.com", "heroOhalom")
# User.log_in("hero@alom.com", 'abc')
 
# selim = Driver("Selim Reza", 'selim@gamil.com', "Selimreza53", "Dhaka_Mirpur", "45652") 
# result = license_autherity.validate_license(selim.email, selim.licence)
# print(result)
# selim.take_driving_test()
# result = license_autherity.validate_license(selim.email, selim.licence)
# print(result)
