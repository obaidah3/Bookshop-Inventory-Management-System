#Programming Project 
from abc import ABC , abstractmethod

#Items in the store
class Item(ABC):
    def __init__(self , title , author , price = None ):
        self.title = title
        self.author = author
        self.__price = price #private atribute so that it cannot be changable 
        
        
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def BasicDetails(self):
        print(f"Title : {self.get_title()} ")
        print(f"Author : {self.get_author()} ")
        print(f"Price : {self.get_price()} ")

    @abstractmethod
    def Update(self): 
        pass

    @abstractmethod
    def Display(self):
        pass

class Book(Item):

    def __init__(self , title , author , price , genre , isbn , pages):
        super().__init__(title , author , price )
        self.genre = genre
        self.isbn = isbn 
        self.pages = pages
        self.__discount = 0.1

    def Display(self):
        self.BasicDetails()
        print(f"Genre : {self.genre} ")
        print(f"ISBN : {self.isbn} ")
        print(f"Pages : {self.pages} ")

    def Update(self , title = None , author = None , price = None  ,genre = None ,isbn = None , pages = None   ):
        if title :
            self.title = title
        elif author :
            self.author = author 
        elif price :
            self.set_price(price)
        elif genre :
            self.genre = genre 
        elif isbn :
            self.isbn = isbn 
        print("Updated Succesfully !!") 

class Magazine(Item):
    def __init__(self, title, author, price, issue_number, publication_date, editor):
        super().__init__(title, author, price)
        self.issue_number = issue_number
        self.publication_date = publication_date
        self.editor = editor

    def get_title(self):
        return super().get_title()

    def Display(self):
        self.BasicDetails()
        print(f"issue Number : {self.issue_number} ")
        print(f"Publication Date : {self.publication_date} ")
        print(f"Editor : {self.editor} ")

    def Update(self , title = None, author = None, price = None, issue_number= None, publication_date= None, editor= None):
        if title:
            self.title = title
        elif author :
            self.author = author
        elif price :
            self.set_price(price)
        elif issue_number :
            self.issue_number = issue_number
        elif publication_date :
            self.publication_date = publication_date
        elif editor :
            self.editor = editor
        print("Updated Succesfully !!")
        
class DVD(Item):
    def __init__(self, title, author, price , director, duration, genre):
        super().__init__(title, author, price)
        self.director = director
        self.duration = duration
        self.genre = genre

    def Display(self):
        self.BasicDetails()
         print(f"Director : {self.director} ")
        print(f"Duration : {self.duration} mins ")
        print(f"Genre : {self.genre} ")

    def Update(self,title  = None, author = None, price = None, director =None, duration = None, genre = None):
        if title:
            self.title = title
        elif author :
            self.author = author
        elif price :
            self.set_price(price)
        elif director :
            self.director =director
        elif duration :
            self.duration = duration
        elif genre : 
            self.genre = genre
        print("Updated Succesfully !!")

#People in the system
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def add_book_to_inventory(self, bookstore, book):
        if isinstance(book, Book):
            bookstore.add_item(book)
            print(f"{self.name} added {book.title} to the inventory.")
        else:
            print("Only books can be added to the inventory by employees.")

class Client:
    def __init__(self, name):
        self.name = name

    def search_item(self, bookstore, title):
        items = bookstore.search_by_title(title)
        if items:
            print(f"Items found with title '{title}':")
            for item in items:
                print(f"- {item.title} by {item.author}")
        else:
            print(f"No items found with title '{title}'.")

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def get_cutomer_name(self):
        return self.customer_name
    
    def add_item(self, item):
        self.items.append(item)
        print(f"{item.title} is add to the cart successfully !")

    def calculate_total(self):
        return sum(item.get_price() for item in self.items)  
    
    def displayItems(self):
        return f"Items : {', '.join(item.title for item in self.items)}"

#Store
class Bookstore:
    def __init__(self):
        self.inventory = []
        self.employees = []
        self.orders = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} has been added to the list of employees.")
    
    def add_item(self, item , item2 = None , item3 = None ,item4 = None):
        self.inventory.append(item )
        self.inventory.append(item2)
        self.inventory.append(item3)
        self.inventory.append(item4)
        #print(f"{item.title} has been added to the inventory.")

    def search_by_title(self, title):
        for item in self.inventory:
            if item.title.lower() == title.lower():
                print("Item exists !")
                x= input("Do you want the Details ? (y / n) ")
                if x.lower() == "y" :
                    print("------- Details --------- ")
                    item.Display()
                    return item
                else:
                    print("Item does not exist !")
                    return item
                    
    def search_by_Author(self, author):
        for item in self.inventory:
            if item.author.lower() == author.lower():
                print("Item exists !")
                x= input("Do you want the Details ? (y / n) ")
                if x.lower() == "y" :
                    print("------- Details --------- ")
                    item.Display()
                    return item
                else:
                    print("Item does not exist !")
                    return item
                
    def search_by_genre(self, genre):
        for item in self.inventory:
            if item.genre.lower() == genre.lower():
                print("Item exists !")
                x= input("Do you want the Details ? (y / n) ")
                if x.lower() == "y" :
                    print("------- Details --------- ")
                    item.Display()
                    return item
                else:
                    print("Item does not exist !")
                    return item        


    def place_order(self, customer_name, order ):
        
        self.orders.append(order)
        print(f"Order placed successfully .")

    def display_orders(self):
        for order in self.orders:
            print(f"Customer: {order.customer_name}")
            print("Items:")
            for item in order.items:
                print(f"- {item.get_title()} (${item.get_price()})")
            print(f"Total: ${order.calculate_total()}")
            
# Initialization
bookstore = Bookstore()

# Updated book objects
book1 = Book("Artificial Intelligence Explained", "Nour Fathy", 89.99, "Educational", 1001001001, 350)
book2 = Book("Cybersecurity Essentials", "Omar Yassin", 99.50, "Technical", 1001001002, 400)
book3 = Book("Beyond Earth", "Alyaa Hamdy", 45.75, "Sci-Fi", 1001001003, 290)
book4 = Book("Quantum Computing 101", "Salma Hossam", 120.00, "Educational", 1001001004, 320)
book5 = Book("The AI Paradox", "Mahmoud El-Sharkawy", 75.99, "Philosophy", 1001001005, 275)
book6 = Book("Chronicles of Mars", "Mona Ehab", 64.50, "Science Fiction", 1001001006, 310)


# Updated magazine objects
mag1 = Magazine("Tech Pulse", "Layla Osama", 10.99, 44, "2025-04", "Hassan Salem")
mag2 = Magazine("Future Trends", "Adel Kamel", 12.50, 45, "2025-05", "Nada Elmasry")
mag3 = Magazine("AI Weekly", "Farida Samir", 8.99, 46, "2025-06", "Tarek Zidan")
mag4 = Magazine("Neural Nexus", "Mohamed Zakaria", 11.00, 47, "2025-07", "Rana Ismail")
mag5 = Magazine("The Innovator", "Youssef Gamil", 9.75, 48, "2025-08", "Leila Nader")


# Updated DVD objects
dvd1 = DVD("The Singularity", "Sara Kamal", 18.99, "Khaled Tawfik", 122, "Science Fiction")
dvd2 = DVD("Code Breakers", "Ahmed Fouad", 16.50, "Lina Ashraf", 98, "Thriller")
dvd3 = DVD("Digital Shadows", "Kareem Adel", 19.99, "Nada Amin", 110, "Cyber Thriller")
dvd4 = DVD("Rebooted Reality", "Zeinab Khalil", 17.49, "Omar Tarek", 95, "Tech Drama")
dvd5 = DVD("The Last Algorithm", "Habiba Mostafa", 20.00, "Ehab Yehia", 130, "Mystery")


# Add items to the bookstore
bookstore.add_item(book1, book2, book3)
bookstore.add_item(mag1, mag2, dvd1, dvd2)
bookstore.add_item(book4, book5, book6)
bookstore.add_item(mag3, mag4, mag5)
bookstore.add_item(dvd3, dvd4, dvd5)



# Create Employee objects (updated names and roles)
emp1 = Employee("Amira Hassan", "Inventory Supervisor")
emp2 = Employee("Omar Khaled", "Customer Relations")
emp3 = Employee("Salma Tarek", "Operations Head")
emp4 = Employee("Tamer Ibrahim", "Sales Manager")
emp5 = Employee("Laila Hossam", "Marketing Director")
emp6 = Employee("Mohamed Samir", "Customer Support Specialist")


# Create Client objects (updated names)
client1 = Client("Farida Ahmed")
client2 = Client("Hassan Fathi")
client3 = Client("Rana Gamil")
client4 = Client("Maya Youssef")
client5 = Client("Nour El-Deen")
client6 = Client("Karim Mohamed")


# Create Employee
def CreateStaffMember():
    try:
        full_name = input("Enter Full Name: ")
        position = input("Enter Position: ")
        security_code = int(input("Enter the intended security code: "))
        if security_code == 1234:
                staff = Employee(full_name, position)
                return staff 
        else:
            print("Incorrect security code: Program is terminating...")
            return 0 
    except ValueError: 
        print("Invalid input.")
        return 
    except Exception as e: 
        print("An unexpected error occurred:", e)
        return

# Create Client
def CreateCustomer():
    full_name = input("Enter Full Name: ")
    customer = Client(full_name)
    return customer



# Create Book
def CreatePublicationBook():
    try:
        book_title = input("Title of the Book: ")
        author_name = input("Author's Name: ")
        category = input("Genre: ")
        isbn_code = input("ISBN: ")
        page_count = int(input("Enter the number of Pages: "))
        price_value = float(input("Enter Price: "))
        
        publication_book = Book(book_title, author_name, price_value, category, isbn_code, page_count)
        publication_book.set_price(price_value)
        return publication_book

    except ValueError: 
        print("Invalid Value")
        return 
    except Exception as e: 
        print("Unexpected error occurred:", e)
        return

# Create Magazine
def CreatePublicationMagazine():
    try:
        mag_title = input("Title of the Magazine: ")
        mag_author = str(input("Author's Name: "))
        issue_no = input("Issue Number: ")
        publish_date = input("Publication Date: ")
        editor_name = input("Editor: ")
        price_value = float(input("Enter Price: "))
        
        magazine = Magazine(mag_title, mag_author, price_value, issue_no, publish_date, editor_name)
        magazine.set_price(price_value)
        return magazine

    except ValueError: 
        print("Invalid Value")
        return 
    except TypeError:
        print("Type Error")
    except Exception as e: 
        print("Unexpected error occurred:", e)

# Create DVD
def CreateMediaDVD():
    try:
        dvd_title = input("Title of the DVD: ")
        dvd_author = str(input("Author/Director: "))
        movie_director = input("Director: ")
        movie_duration = input("Duration (in mins): ")
        movie_genre = input("Genre: ")
        price_value = float(input("Enter Price: "))
        
        dvd_media = DVD(dvd_title, dvd_author, price_value, movie_director, movie_duration, movie_genre)
        dvd_media.set_price(price_value)
        return dvd_media

    except ValueError: 
        print("Invalid Value")
        return 
    except TypeError:
        print("Type Error") 
    except Exception as e: 
        print("Unexpected error occurred:", e)

    

## Search for an Item
def SearchForItem():
    print("---Search for an Item ---\n")
    print("1. Book")
    print("2. Magazine")
    print("3. DVD")
    search_choice = int(input("Enter your Choice -> "))
    
    if search_choice == 1:
        print("*" * 50)
        print("Search for an Item by Title: \n")
        search_title = input("Enter the title -> ")
        search_result = bookstore.search_by_title(search_title)
        if search_result:
            for item in search_result:
                print(f"Found: {item.title} by {item.author}")
        else:
            print("No matching items found.")
    elif search_choice == 2:
        print("*" * 50)
        print("Search for an Item by Title: \n")
        search_title = input("Enter the title -> ")
        search_result = bookstore.search_by_title(search_title)
        if search_result:
            for item in search_result:
                print(f"Found: {item.title} by {item.author}")
        else:
            print("No matching items found.")
    elif search_choice == 3:
        print("*" * 50)
        print("Search for an Item by Title: \n")
        search_title = input("Enter the title -> ")
        search_result = bookstore.search_by_title(search_title)
        if search_result:
            for item in search_result:
                print(f"Found: {item.title} by {item.author}")
        else:
            print("No matching items found.")
    else:
        print("Invalid Input.")

# Search and Price
def SearchAndPrice():  
    print("---Search for an Item ---\n")
    print("1. Book")
    print("2. Magazine")
    print("3. DVD")
    search_choice = int(input("Enter your Choice -> "))
    
    if search_choice == 1:
        print("*" * 50)
        print("Search for an Item by Title: \n")
        search_title = input("Enter the title of the book -> ")
        search_result = bookstore.search_by_title(search_title)
        if search_result:
            for item in search_result:
                print(f"Found: {item.title} by {item.author}")
                print(f"The Price is: {item.get_price()} EGP.")
        else:
            print("No matching items found.")
    elif search_choice == 2:
        print("*" * 50)
        print("Search for an Item by Title: \n")
        search_title = input("Enter the title -> ")
        search_result = bookstore.search_by_title(search_title)
        if search_result:
            for item in search_result:
                print(f"Found: {item.title} by {item.author}")
                print(f"The Price is: {item.get_price()} EGP.")
        else:
            print("No matching items found.")
    elif search_choice == 3:
        print("*" * 50)
        print("Search for an Item by Title: \n")
        search_title = input("Enter the title -> ")
        search_result = bookstore.search_by_title(search_title)
        if search_result:
            for item in search_result:
                print(f"Found: {item.title} by {item.author}")
                print(f"The Price is: {item.get_price()} EGP.")
        else:
            print("No matching items found.")
    else:
        print("Invalid Input.")



#Return Menus
def Returnifemp():
    print("---- Return ----")
    print("1 . Main Menu")
    print("2 . Employee Menu")
    print("3 . Terminate Program")
    choice = int(input("Enter an Option -> "))
    if choice == 1 :
        clientOrEmployee()
    elif choice == 2 :
        Employee()
    else :
        print("The Program is Terminating .......")
        return

def Returnifclient(client):
    print("---- Return ----")
    print("1 . Main Menu")
    print("2 . Client Menu")
    print("3 . Terminate Program")
    choice = int(input("Enter an Option -> "))
    if choice == 1 :
        clientOrEmployee()
    elif choice == 2 :
        Client(client)
    else :
        print("The Program is Terminating .......")
        return

def ReturnToMenu():
    option4 = str(input("Do you want to return to the main menu ? (y/n)"))  
    if option4.lower() == "y":
        clientOrEmployee()
    else :
        print("The Program is Terminating .......")

#Lists
def EmployeeMenu():
    print("_"*50)
    print("Accessibilities : ")
    print("1 . Add to Inventory ")
    print("2 . Check the Price for an Item ")
    print("3 . Search for an Item ")
    print("4 . View Customer Orders ")
    print("5 . Update an Item ")
    selected_option = int(input("Enter an Option -> "))
    
    if selected_option == 1 :
        print("\n") 
        print("_"*50)
        print("What do you want to add to the inventory ? : ")
        print("*"*50)
        print("1 . Book ")
        print("2 . Magazine ")
        print("3 . DVD ")
        
        item_choice = int(input("Enter a Number -> "))
        if item_choice == 1 :
            book_item = CreatePublicationBook()
            bookstore.add_item(book_item)
            print(f"{book_item.get_title()} by {book_item.get_author()} is added successfully")
            EmployeeMenu()
            
        elif item_choice == 2:
            magazine_item = CreatePublicationMagazine()
            bookstore.add_item(magazine_item)
            print(f"{magazine_item.get_title()} by {magazine_item.author} is added successfully")

        elif item_choice == 3:
            dvd_item = CreateMediaDVD()
            bookstore.add_item(dvd_item)
            print(f"{dvd_item.get_title()} by {dvd_item.get_author()} is added successfully")

        else :
            print("Invalid input: Program is terminating ....")
            return
    
    elif selected_option == 2 : 
        title = input("What is the title ? ")
        item_found = bookstore.search_by_title(title)
        print("-"*40)
        print("\nThe price is : ", item_found.get_price(), " EGP .\n")
        print("*"*50)
        Returnifemp()

    elif selected_option == 3:
        title = input("What is the title ? ")
        item_found = bookstore.search_by_title(title)
        print("-"*40)
        
    elif selected_option == 4 :
        if bookstore.display_orders() :
            bookstore.display_orders()
        else :
            print("." *50)
            print("No orders to display ... ")
            Returnifemp()

    elif selected_option == 5 :
        UpdateItem()

def ClientMenu(client_instance):
    print(f"----- Welcome {client_instance.name} -----\n")
    print("1. Place an Order ")
    print("2. Check Price ")
    print("3. Search for an Item\n")
    print("-"*40)

    client_choice = int(input("Enter your choice -> "))
    print("_" * 40)
    print("\n")
    if client_choice == 1:
        print("*" * 50)
        number_of_items = int(input("How many items do you want to order? "))
        client_order = Order(client_instance)
        while number_of_items >= 1:
            title = input("What is the title of the book ? ")
            item_found = bookstore.search_by_title(title)
            client_order.add_item(item_found)
            print("*" * 50)
            number_of_items -= 1
        while True:
            print("1 . Check Out \n2 . See Cart \n3 . Return to Main Menu")
            order_choice = int(input("Enter your choice -> "))
            if order_choice == 1:
                print("Total is : ", client_order.calculate_total(), " EGP.")
                bookstore.place_order(client_instance, client_order)
                Returnifclient(client_instance)
            elif order_choice == 2:
                print(client_order.displayItems())
                print("Total is : ", client_order.calculate_total())
                print("-" * 50)
            elif order_choice == 3:
                Returnifclient(client_instance)
            else:
                print("Invalid input: Program is terminating ....")
                return

    elif client_choice == 2 :
        title = input("What is the title ? ")
        item_found = bookstore.search_by_title(title)
        print("-"*40)
        print("\nThe price is : ", item_found.get_price(), " EGP .\n")
        print("*"*50)
        Returnifclient(client_instance)
    
    elif client_choice == 3 : 
        # Search for an Item
        SearchForItem()
        Returnifclient(client_instance)

    else:
        print("Invalid input: Program is terminating ....")
        return


#Updating Info

#For BOOKS , MAGAZINES & DVDs
def UpdateTitle(item):
    new_title = str(input("Enter the new title : "))
    item.Update(title = new_title)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
    else:
        Returnifemp()

def UpdateAuthor(item):
    new_author = str(input("Enter the new Author : "))
    item.Update(author = new_author)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

def UpdateGenre(item):
    new_genre = str(input("Enter the new Genre : "))
    item.Update(genre = new_genre)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
    else:
        Returnifemp()

def UpdatePrice(item):
    new_price = float(input("Enter the new Price : "))
    item.Update(price = new_price)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

#For Books
def UpdateISNB(item):
    new_isnb = eval(input("Enter the new ISNB : "))
    item.Update(isnb = new_isnb)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

def UpdatePages(item):
    new_pages = int(input("Enter the new Number of Pages : "))
    item.Update(pages = new_pages)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

#For Magazines
def UpdateEditor(item):
    new_editor = str(input("Enter the new Editor : "))
    item.Update(editor = new_editor)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

def UpdateIssueNumber(item):
    new_issue_number = int(input("Enter the new Issue Number : "))
    item.Update(issue_number = new_issue_number )
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

def UpdatePublicationDate(item):
    new_publication_date = eval(input("Enter the new Publication Date : "))
    item.Update(publication_date = new_publication_date)
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

#For DVDs
def UpdateDirector(item):
    new_director = str(input("Enter the new Director : "))
    item.Update(director = new_director )
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

def UpdateDuration(item):
    new_duration = eval(input("Enter the new Duration : "))
    item.Update(duration = new_duration )
    option3 = str(input("Do you want to display the new Details ? (y/n)"))
    if option3.lower() == "y":
        item.Display()
        Returnifemp()
        
    else:
        Returnifemp()

#General Excution Function
def UpdateItem():
    print("\n") 
    print("_"*50)
    print("What do u want to Update ? : ")
    print("*"*50)
    print("1 . Book ")
    print("2 . Magazine ")
    print("3 . DVD ")
    option = int(input("Enter a Number -> "))
    

    if option == 1 :
        x = input("What is the title of the book ? ")
        book =  bookstore.search_by_title(x)
        if book : 
            #title , author , price , genre , isbn , pages
            print("What do u want to Update ? : ")
            print("1. Title")
            print("2. Author")
            print("3. Genre")
            print("4. ISBN ")
            print("5. Number of Pages ")
            print("6. Price")

            option2 = int(input("Enter a Number -> "))

            if option2 == 1 :
                UpdateTitle(book)
            elif option2 == 2 : 
                UpdateAuthor(book)
            elif option2 == 3 :
                UpdateGenre(book)
            elif option2 == 4 :
                UpdateISNB(book)
            elif option2 == 5 :
                UpdatePages(book)
            elif option2 == 6 :
                UpdatePrice(book)

    elif option == 2 :
        x = input("What is the title of the book ? ")
        mag =  bookstore.search_by_title(x)
        if mag : 
            #title, author, price, issue_number, publication_date, editor
            print("What do u want to Update ? : ")
            print("1. Title")
            print("2. Author")
            print("3. Editor")
            print("4. Issue Number ")
            print("5. Publication Date ")
            print("6. Price")
            option2 = int(input("Enter a Number -> "))
            if option2 == 1 :
                UpdateTitle(mag)
            elif option2 == 2 : 
                UpdateAuthor(mag)
            elif option2 == 3 :
                UpdateEditor(mag)
            elif option2 == 4 :
                UpdateIssueNumber(mag)
            elif option2 == 5 :
                UpdatePublicationDate(mag)
            elif option2 == 6 :
                UpdatePrice(mag)
            else : 
                print("Invalid Option")

    elif option == 3 :
        x = input("What is the title of the book ? ")
        dvd =  bookstore.search_by_title(x)
        if dvd : 
            #title, author, price , director, duration, genre
            print("What do u want to Update ? : ")
            print("1. Title")
            print("2. Author")
            print("3. Genre")
            print("4. Director ")
            print("5. Duration ")
            print("6. Price")
            option2 = int(input("Enter a Number -> "))
            if option2 == 1 :
                UpdateTitle(dvd)
            elif option2 == 2 : 
                UpdateAuthor(dvd)
            elif option2 == 3 :
                UpdateGenre(dvd)
            elif option2 == 4 :
                UpdateDirector(dvd)
            elif option2 == 5 :
                UpdateDuration(dvd)
            elif option2 == 6 :
                UpdatePrice(dvd)
    else :
        print("Invalid Option")
         



def clientOrEmployee ():
    print("---- Welcome to Bookshop ----")
    x = input("Are you an Employee or a Client ?: ")
    if x.lower() == "employee" :
        try:    
            emp = CreateStaffMember()
            if emp :
                bookstore.add_employee(emp)
            else:
                return
        except ValueError : 
            print("Value Error")
            return 
        except TypeError:
            print("Type Error") 
        except Exception as e : 
            print("Unexpected Error happened : " , e)

        Employee()

    elif x.lower() == "client" : 
        client = Client()
        Client(client)
                 
 


clientOrEmployee ()
