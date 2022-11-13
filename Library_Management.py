
""" 
Project: Library Management System (Using OOP)
Author : Jubayer Ahmed

"""


class User:

    allUsers = [] 
    currentUser = None #class Attribute
    def __init__(self,name,roll,password):

        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_books = []
        self.return_books = []
        self.allUsers.append(self) # object's reference passing here

    def __repr__(self) -> str:
        return f'Name:{self.name}' 



class Library(User):
    
    def __init__(self,book_list) -> None:
        self.book_list = book_list 


    def borrow_book(self,book_name):

        for book in self.book_list:
            if book == book_name and self.book_list[book] > 0:
                hasBook = False

                if book_name in User.currentUser.borrow_books:
                    hasBook = True
                    print("You Already taken this book!\nOne Book Multiple Times is not allowed!!")
                    return

                if hasBook == False:
                    print(f'Here is your Book: {book_name}')
                    self.book_list[book]-=1
                    User.currentUser.borrow_books.append(book_name)
                    return
  
        print(f'The book named: {book_name} is currently not available!!')
            


    def return_book(self,book_name):

        if book_name in User.currentUser.borrow_books:
            User.currentUser.borrow_books.remove(book_name)
            User.currentUser.return_books.append(book_name)
            for book in self.book_list:
                if book == book_name:
                    self.book_list[book]+=1
                    print('Thank you! The book returned successfully!')
                    return

        print(f"The book named: {book_name} is not Our Library's Book!")



    def donate_book(self,book_name,quantity):
        for book in self.book_list:
            if book == book_name:
                self.book_list[book]+=quantity
                print('Thank you! Donation Done successfully!')
                return
        
        self.book_list[book_name] = quantity
        print('Thank you! Donation Done successfully!')



    def book_availability(self):
        isEmpty = True
        for book in self.book_list:
            if self.book_list[book] > 0:
                print(book, self.book_list[book])
                isEmpty = False

        if isEmpty == True:
            print('Sorry! Currently No Book is Available.')








popy_library = Library({'English':1,'Bangla':5,'Math':3})



while True:

    if User.currentUser == None:
        print("Please Login or Create An account(L/C): ")
        option = input('')
        if option == 'L':
            roll = int(input('Enter Roll: '))
            password = input('Enter Password: ')
            userMatch = False
            for user in User.allUsers:
                if user.roll == roll and user.password == password:
                    User.currentUser = user
                    userMatch = True

            if userMatch == False:
                print('No User Found!')

        else:
            userFound = False
            name = input('Enter your Name: ')
            roll = int(input('Enter your Roll: '))
            for user in User.allUsers:
                if user.roll == roll:
                    print('An Account Already Exist')
                    userFound = True
                    break

            if userFound == False:
                password = input('Give a password: ')
                user = User(name,roll,password)
                User.currentUser = user
                User.allUsers.append(user)

    else:
        print()
        print('--------------------')
        print('OPTIONS')
        print("1.Borrow a Book")
        print("2.Return a Book")
        print("3.Brroowed Books List")
        print("4.Return Books List")
        print("5.Check Book Availablity")
        print("6.Donate Book")
        print("7.Log Out")
        print()

        user_option = int(input('Enter an Option: '))
        if user_option == 1:
            book_name = input('Book Name: ')
            popy_library.borrow_book(book_name)

        elif user_option == 2:
            book_name = input('Book Name: ')
            popy_library.return_book(book_name)

        elif user_option == 3:
            print(User.currentUser.borrow_books)

        elif user_option == 4:
            print(User.currentUser.return_books)

        elif user_option == 5:
            popy_library.book_availability()

        elif user_option == 6:
            book_name = input('The Name of Book For Donaate: ')
            book_quantity = int(input('Quantity of the Book: '))
            popy_library.donate_book(book_name,book_quantity)

        else:
            User.currentUser = None





