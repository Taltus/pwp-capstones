
class User(object):
            def __init__(self, name, email):
                        self.name = name
                        self.email = email
                        self.books = {}
# A method get_email that returns the email associated with this user
            def get_email(self):
                        return self.email
# A method change_email that takes in a new email and changes the email associated with this user. 
# It should also print a message saying that this user’s email has been updated.      
            def change_email(self, address):
                        self.email = address
                        print('{} email changed to {}'.format(self.name, self.email))        

# A __repr__ method that returns a string to print out this user object in a meaningful way. 
# Printing a user named Stephen Hawking, with an email hawking@universe.edu, with 7 books read, might produce a string like:
            def __repr__(self):
                        return ''' Username: {} email: {} Books you have read: {} '''.format(self.name, self.email, len(self.books))
        
# An __eq__ method to define comparison between users. 
# A User object should be equal to another User object if they both have the same name and email.   
            def __eq__(self, other_user):
                        if self.name == other_user.name and self.email == other_user.email:
                                    return True
                        return False
   
# Give Books and Users Methods
# Now that we have both Book classes and User classes, we can create more methods than just ones that get and set instance variables.

# read_book, which takes in book and an optional parameter rating, which defaults to None. 
# It should add a key:value pair to self.books where the key is book and the value is rating.
            def read_book(self, book, rating=None):
                        self.books[book] = rating

# get_average_rating, which iterates through all of the values in self.books, which are the ratings, and calculates the average rating. 
# It should return this average.
            def get_average_rating(self):
                        average = 0
                        rated_books = 0
                        for value in self.books.values():
                                    if value:
                                                average += value
                                                rated_books += 1
                                                average = average / rated_books
                                    return average
      

#Define a Book object that has:
class Book(object):
# A constructor method, which takes in self, title, and isbn. 
# It should set instance variables self.title and self.isbn. 
# It Should also set an instance variable self.ratings, which will Start as an empty list.
# - title will be a string
# - isbn will be a number        
        
            def __init__(self, title, isbn):
                        self.title = title
                        self.isbn = isbn
                        self.ratings = []

# A method get_title that returns the title of the book.
            def get_title(self):
                        return self.title
        
# A method get_isbn that returns the ISBN of the book.
            def get_isbn(self):
                        return self.isbn

# A method set_isbn that takes in a new ISBN and sets the book’s isbn to be this new number. 
# It should also print a message saying that this book’s ISBN has been updated.
            def set_isbn(self, new_isbn):
                        self.isbn = new_isbn
                        print('Book {} set to {}'.format(self.title, self.isbn))

# A method called add_rating that takes in a rating and adds it to the list self.ratings. 
# It should only do this if rating is a valid rating (at least 0 and at most 4 ). 
# Otherwise, it should print "Invalid Rating".
            def add_rating(self, rating):
                        if rating and 0 < rating <= 4:
                                    Self.ratings.append(rating)
                        else:
                                    print('Invalid rating')

# An __eq__ method to define comparison between books. 
# A Book object should be equal to another Book object if they both have the same title and isbn.
            def __eq__(self, other_book):
                        if self.title == other_book.title and self.isbn == other_book.idbn:
                                    return True
                        return False
        
# get_average_rating, which iterates through all of the values in self.ratings and calculates the average rating. 
# It should return this average.

            def get_average_rating(self):
                        average = 0
                        for rating in self.ratings:
                                    average += rating
                        try:
                                    average = average / len(self.ratings)  
                        except ZeroDivisionError:
                                    print('ratings list is empty')    
                        return average

# There is one more method we have to add to Book to make this work! 
# Do you remember how we get the error TypeError: unhashable type: 'list', when we try to create a dictionary with lists as keys? 
# This is because lists are mutable, and thus do not have a consistent hash that a dictionary can use to look up the associated value. 
# We are trying to make a dictionary in the User class called self.books that has Book objects askeys. 
# In order to use a class that we construct ourselves, we must make sure that our object is hashable, and not unhashable, like a list!
# To make our Book hashable, we will add a method __hash__ which will return a consistent hash for an instance of a book object:
# Copy this method into your Book class so that Book becomes hashable! 
# If you’re curious, look at the documentation to see what the built-in method hash() is doing: https://docs.python.org/3/library/functions.html#hash
            def __hash__(self):
                        return hash((self.title, self.isbn))
        
        
# Make a Fiction Subclass of Book
# Assume we have two kinds of books, fiction and non-fiction.
class Fiction(Book):

# A constructor, which takes in self, title, author, and isbn. 
# It should first call the __init__ of its parent class, with title and isbn. 
# Then, it should set the instance variable self.author         
            def __init__(self, title, author, isbn):
                        Book.__init__(self, title, isbn)
                        self.author = author

# get_author, which returns the author       
            def get_author(self):
                        return self.author
        
# Define a reprr which will return a meaningful string. {title} by {author}       
            def __repr__(self):
                        return '{} by {}'.format(self.title, self.author)


# Make a Non-Fiction Subclass of Book
# The Non_Fiction class should inherit from Book
class Non_Fiction(Book):
        
# A constructor, which takes in self, title, subject, level and isbn. 
# It should first call the __init__ of its parent class, with title and isbn. 
# Then, it should set the instance variables self.subject and self.level. 
# - subject will be a string, like "Geology"
# - level will be a string, like "advanced        
            def __init__(self, title, subject, level, isbn):
                        Book.__init__(self, title, isbn)
                        self.subject = subject
                        self.level = level

# get_subject, which returns the subject
            def get_subject(self):
                        return self.subject
    
 # get_level, which returns the level
            def get_level(self):
                        return self.level
        
# get_level, which returns the level {title}, a {level} manual on {subject}
# For example, the book with title “Society of Mind” about beginner Artificial Intelligence would print out:
            def __repr__(self):
                        return '{}, a {} manual on {}'.format(self.title, self.level, self.subject)



# CREATE TOMERATER
class TomeRater:
        
# A constructor that only takes in self. 
# It should create:
# - self.users, an empty dictionary that will map email to the corresponding User object
# - self.books, an empty dictionary that will map object to the number of Users that have read it
            def __init__(self):
                        self.users = {}
                        self.books = {}
               
# create_book, which takes in title and isbn and creates a new book with that title and ISBN. 
# Returns this Book object.


            def create_book(self, title, isbn):
                        new_book = Book(title, isbn)
                        return new_book

# create_novel, which takes in title, author, and isbn, and creates a new Fiction with that title, author and ISBN. 
# Returns this Fiction object.    
            def create_novel(self, title, author, isbn):
                        new_novel = Fiction(title, author, isbn)
                        return new_novel

# create_non_fiction, which takes in title, subject, level, and isbn, and creates a new Non_Fiction with that title, author and ISBN.
# Returns this Non_Fiction object.
            def create_non_fiction(self, title, subject, level, isbn):
                        non_fiction = Non_Fiction(title, subject, level, isbn)
                        return non_fiction

# add_book_to_user, which takes in book, email, and an optional parameter rating, which defaults to None. 
# It should get the user in self.users with the key email. 
# If this user doesn’t exist, it should print out `“No user with email {email}!”. 
# If the user exists, it should: 
# - Call read_book on this user, with book and rating
# - Call add_rating on book, with rating Check if the book is in TomeRater’s self.books already. 
# If it is not, add the key book to self.books with a value of 1 (because one user has read it)
# If book was already in the catalog, increase the value of it in self.books by 1, because one more user has read it.
            def add_book_to_user(self, book, email, rating=None):
                        user = self.users.get(email, None)
                        if user:
                                    user.read_book(book, rating)
                                    if book not in self.books:
                                                self.books[book] = 0
                                                self.books[book] += 1
                                                book.add_rating(rating)
                        else:
                                    print("No user with email " + email)

# add_user, which takes in name, email, and an optional list of Books user_books that defaults to None. 
# It should create a new User object from name and email. 
# Then, if user_books is provided, it should loop through the list, and add each Book to the user (using the TomeRater method add_book_to_user )
            def add_user(self, name, email, user_books=None):
                        new_user = User(name, email)
                        self.users[email] = new_user
                        if user_books:
                                    for book in user_books:
                                                self.add_book_to_user(book, email)

#print_catalog, which iterates through all of the keys i self.books (which are Book objects), and prints them    
            def print_catalog(self):
                        for keys in self.books:
                                    print(keys)

#print_users, which iterates through all of the values of self.users (which are the User objects), and prints them
            def print_users(self):
                        for user in self.users.values():
                                    print(user)
                        
# most_read_book, which should iterate through all of the books in self.books and return the book that has been read the most.
# Remember that the keys of self.books are Books, and the values are how many times they’ve been read.
            def most_read_book(self):
                        most_read = float("-inf")
                        most_read = None

                        for book in self.books:
                                    num_reads = self.books[book]
                        if num_reads > most_read:
                                    most_read = num_reads
                                    most_read = book
                        return most_read
# highest_rated_book , which should iterate through all of the books in self.books and return the book that has the highest average rating. 
# Remember that the keys of self.books are Books, and you can call book.get_average_rating() on a Book object book.
            def highest_rated_book(self):
                        highest_rating = float("-inf")
                        best_book = None
                        for book in self.books:
                                    average = book.get_average_rating()
                        if average > highest_rating:
                                    highest_rating = average
                                    best_book = book
                                    return best_book

# most_positive_user, which should iterate through all of the users in self.users and return the user that has the highestaverage rating. 
# Remember that the values of self.users are Users, and you can call user.get_average_rating() on a User object user .
            def most_positive_user(self):
                        highest_rating = float("-inf")
                        nicest_user = None

                        for user in self.users.values():
                                    average = user.get_average_rating()
                        if average > highest_rating:
                                    highest_rating = average
                                    nicest_user = user
                        return nicest_user

            def lookup_user_average_rating(self, email):
                        user = self.users.get(email, None)
                        if user:
                                    return user.get_average_rating()
                        return "No such user"
