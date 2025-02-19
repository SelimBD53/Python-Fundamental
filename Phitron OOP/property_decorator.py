class User:
    def __init__(self, f_name, l_name):
        self.first = f_name
        self.last  = l_name
        self.email = f"{self.first}.{self.last}@user.com"
    

    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter
    def full_name(self, value):       # value set korar jonno ai ta used kora hoyacha
        # first, last = value.split(" ")
        self.first = value.split(" ")[0]  #first
        self.last = value.split(" ")[2]     # last
        self.email = f"{self.first}.{self.last}@user.com"
   
    # @full_name.deleter
    # def full_name(self):
    #     del self.first
    #     del self.last
        
    def get_email(self):
        return self.email

mark = User("Selim", "Reza")
print(mark.first)
print(mark.email)
print(mark.get_email())
print(mark.full_name)
mark.full_name = "Tom And Jerry"
# del mark.full_name
print(mark.first)
print(mark.last)
print(mark.email)
