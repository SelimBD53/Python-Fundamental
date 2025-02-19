from abc import ABC, abstractmethod

class Vechile(ABC):
    @abstractmethod
    def start(self):
        # print("selim")
        pass
        
class Car(Vechile):
    print("Selim")
    
    def start(self):
        print("Start the Car")
    
    def stop(self):
        print("Stop The Car")
    
car = Car()
car.start()
car.stop()