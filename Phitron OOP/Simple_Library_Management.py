class User:
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_books = []
        self.returned_books = []
        

class Library:
    def __init__(self, book_list):
        self.book_list = book_list
    
    def borrow_book(self, bookName, user):
        for book in self.book_list:
            if book == bookName:
                if bookName in user.borrow_books:     # Logic One
                    print("Please Return The Book First")
                    return
                if self.book_list[book] == 0:   # Logic two
                    print("Sorry, The book is out of print at the library.")
                    return 
                self.book_list[book] -= 1        # Logic three
                print("You have Successfully Borrow This Book.")
                user.borrow_books.append(bookName)
                return
        print("Book Not Available.")
     
    def return_book(self, bookName, user):
        for book in self.book_list:
            if book == bookName:
                if book in user.borrow_books:
                    self.book_list[book] += 1
                    user.borrow_books.remove(bookName)
                    user.returned_books.append(bookName)
                    print("Book Return Successfully")
                    return
                else: 
                    print("Do not Another Person Book Return.")
                    return
        print("Whose book have you come to return?")

    def availability(self):
        for book in self.book_list:
            if self.book_list[book] > 0 :
                print(book, self.book_list[book])

    def donate(self, bookName, amount):
        for book in self.book_list:
            if book == bookName:
                self.book_list[book] += amount
                print("Thanks For Book Donating.")
                return
        self.book_list[bookName] = amount
        print("Thanks For Book Donating.")

                 
  
library = Library({"English": 3, "Bangla": 5, "Math": 3})

allUsers = []          # User Info thakba=== userName, roll, password
currentUser = None
print(allUsers)                

# At first user login korta hoba. login na thakla msage debo.
while True:
    if currentUser == None:         # correntuser none mana logine kora koue nai.
        print("Not logged in\nPlease Login or Create Account(L/C)")
        option = input()
        if option == "L":
            roll = int(input("Enter The Roll: "))
            password = input("Enter The password: ")
            match = False
            for user in allUsers:
                if user.roll == roll and user.password == password:
                    currentUser = user                            # Match hola current user ka debo. na hola user k kuja poua jaccha na.
                    match = True
            if match == False:
                print("No User Found")
        else:                         # New User Created. 
            name = input("Name: ")    
            roll = int(input("Roll: "))  
            password = input("Password: ")
            found = False
            for user in allUsers:
                if user.roll == roll:
                    found = True
            if found:
                print("Already You are Loggined in.")
                continue     
            user = User(name, roll, password) 
            currentUser = user
            allUsers.append(user)
                     
    else:
        print("OPTIONS")
        print("_______________")
        print("1. Borrow a Book")
        print("2. Return a book")
        print("3. Borrowed book List")
        print("4. Returned book List")
        print("5. Check Availability")
        print("6. Donate")             # Book Add Kora
        print("7. Logout")
        print("8. Quit")
        x = int(input("Give Option: "))
        if x == 1:
            bookName = input("Enter The Book Name: ")
            library.borrow_book(bookName, currentUser)
        elif x == 2:
            bookName = input("Enter The Book Name: ")
            library.return_book(bookName, currentUser)
        elif x == 3:
            print(currentUser.borrow_books)
        elif x == 4:
            print(currentUser.returned_books)
        elif x == 5:
            library.availability()
        elif x == 6:
            bookName = input("Book Name: ")
            amount = int(input("Enter The Amount: "))
            library.donate(bookName, amount)
        elif x == 7: 
            currentUser = None    
        elif x == 8:
            break

        print("\n\n") 
print(allUsers)                
