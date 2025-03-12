import random

class BRTA:
    def __init__(self):
        self.__licence = {}
    def take_driving_test(self, email):
        score = random.randint(0, 100)
        licence_number = random.randint(5000, 9999)
        if score >=33:
            # print("Congrass, You Have Pass", score)
            self.__licence[email] = licence_number
            return licence_number
        else:
            # print("sorry you failed", score)
            return False
    def validate_license(self, email, license):
        for key, value in self.__licence.items():
            if key == email and value == license:
                print("You are authenticate Driver")
                return True
        return False