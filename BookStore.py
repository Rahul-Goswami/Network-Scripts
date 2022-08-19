books_in_library = [{'name': 'Harry potter', 'author': 'J.K.Rowling', 'category': 'Fiction'},
{'name': 'A Song of Ice and Fire', 'author': 'George R. R. Martin', 'category': 'Fantasy'},
{'name': 'A Brief History of Time', 'author': 'Stephen Hawking', 'category': 'Cosmology'},
{'name': 'Revolution 2020', 'author': 'Chetan Bhagat', 'category': 'Fiction'}]


def receive_books(list_of_books):
    # Retrive the book from 3rd position. Tag the book and store to a variable so that you can retrive next time.
    third_book = None
    for itr in books_in_library:
        if list_of_books[2] == itr['name']:
            third_book = itr
    print("\nThird Book details: ", third_book)
    print("\n")

    # Start displaying the message saying `Hey!! welcome to cerner library` until it reaches the end of list index
    for itr in list_of_books:
        print("Hey! Welcome to Cerner Library")

    # while iterating the list of books, when it reaches the 4th position call the function Book_to_move() and store the book from a 4th position to a variable
    count = 1
    fourth_book = None
    for itr in list_of_books:
        if count == 4:
            print("\nFourth Book Details: ", book_to_move(itr))
            break
        count += 1


    # List of books
    print("\nList of books: ")
    for itr in books_in_library:
        print(itr)

def book_to_move(bookname):
    fourth_book = None
    for itr in books_in_library:
        if bookname == itr['name']:
            fourth_book = itr
    return fourth_book


list_of_books = ['Revolution 2020', 'A Song of Ice and Fire', 'Harry potter', 'A Brief History of Time', 'Game of Thrones']
print("\nList of Books as input: ", list_of_books)
receive_books(list_of_books)
