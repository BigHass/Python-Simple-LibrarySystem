import pickle
class Book:
    def __init__(self, title, author_name, price):
        self.__title = title
        self.__author=author_name
        self.__price=price
    
    def set_title(self, title):
        self.__title=title
    
    def get_title(self):
        return self.__title
    
    def set_author(self, author_name):
        self.__author=author_name
    
    def get_author(self):
        return self.__author
    
    def set_price(self, price):
        self.__price=price

    def get_price(self):
        return self.__price
    
    def display(self):
        print("%-20s %-20s %s" %(self.__title, self.__author, self.__price))
########################################################################################
def Add_Book():
    var_flie=open('book.dat','ab')
    var_flie.close()
    title_name=input("Enter the title:")
    author_name=input("Enter the author name:")
    price=float(input("Enter the price:"))
    book_obj=Book(title_name, author_name, price)
    var_file=open('book.dat', 'ab')
    pickle.dump(book_obj,var_file)
    var_file.close()
########################################################################################
def Search_Book():
    notfound=True
    flag_title=input("Enter the title of the book to search about:")
    flag=False
    var_file=open('book.dat', 'rb')
    while not flag:
        try:
            book_obj=pickle.load(var_file)
            if book_obj.get_title()==flag_title:
                print("The Author name is :",book_obj.get_author())
                print("The Price is :",book_obj.get_price(),"JD")
                notfound=False
        except EOFError:
            flag=True
    var_file.close()
    if notfound:
        print("The book doesn't found")
########################################################################################
def Delete_Book():
    notfound=True
    flag_title=input("Enter the title of the book to be deleted:")
    flag=False
    list_flag=[]
    var_file=open('book.dat', 'rb')
    while not flag:
        try:
            book_obj=pickle.load(var_file)
            list_flag.append(book_obj)
        except EOFError:
            flag=True
    var_file.close()
    for item in list_flag:
        if item.get_title()==flag_title:
            list_flag.remove(item)
            notfound=False
    var_file1=open('book.dat', 'wb')
    for obj in list_flag:
        pickle.dump(obj,var_file1)
    var_file1.close()
    if notfound:
        print("The book doesn't found")
########################################################################################
def Update_Book():
    flag_title=input("Enter the title of the book to be updated:")
    flag=False
    list_flag=[]
    var_file=open('book.dat', 'rb')
    while not flag:
        try:
            book_obj=pickle.load(var_file)
            list_flag.append(book_obj)
        except EOFError:
            flag=True
    var_file.close()
    for book_object in list_flag:
        if book_object.get_title()==flag_title:
                choice=input("Enter the field to update (a for author. p for price):")
                if choice.lower()=='p':
                    new_price=float(input("Enter the new price:"))
                    book_object.set_price(new_price)
                elif choice.lower()=='a':
                    new_author_name=input("Enter the new name of author:")
                    book_object.set_author(new_author_name)
                else:
                    print("Wrong choice, please try again...")
    var_file1=open('book.dat', 'wb')
    for obj in list_flag:
        pickle.dump(obj,var_file1)
    var_file1.close()
########################################################################################
def View_Book():
    print()
    print("%-20s %-20s %s" %("Title","Author","Price"))
    print("************************************************************")
    flag=False
    var_file=open('book.dat', 'rb')
    while not flag:
        try:
            book_obj=pickle.load(var_file)
            book_obj.display()
        except EOFError:
            flag=True
    var_file.close()
    print("************************************************************")
    print()
########################################################################################
def main():
    flag = True 
    while flag :
        print("****************************MENU****************************")
        print("1- Add book.")
        print("2- Search about book.")
        print("3- Delete book.")
        print("4- Update book.")
        print("5- View books.")
        print("6- Exit.")
        choice = int(input("Enter your choice:"))
        print("************************************************************")
        if choice == 1 :
            Add_Book()
        elif choice == 2:
            Search_Book()
        elif choice ==3:
            Delete_Book()
        elif choice == 4:
            Update_Book()
        elif choice ==5:
            View_Book()
        elif choice ==6:
            flag=False
            print("Good Bye.")
        else :
            print("Wrong choice, please try again....")
main()