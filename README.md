##Overview
This project is a simple library management system. Both administrators and regular users can sign in through the same sign-in page, but they will be directed to different features based on their account type (admin or regular user).

##Administrator Features :
-Create accounts for administrators and regular users
-Delete existing accounts
-Add new books to the library
-Utilize the borrow and return book features

##Regular User Features:
-Borrow books from the library
-Return borrowed books

##How it Works?
-Upon accessing the system, users will be prompted to sign in.
-After successful sign-in, administrators will have access to the administrative features mentioned above, while regular users will only have access to the borrow and return book features.
-Administrators can manage accounts, add new books to the library, and handle book borrowing and returning operations.
-Regular users can browse the available books and borrow or return them as needed.

##Admin Features
After signing in, administrators will be prompted to choose between managing accounts or managing books in the library.
Manage Accounts
1. Create Account
-Administrators can create accounts for other administrators or regular users.
-The username and password fields cannot be left blank or contain only spaces.
2. Delete Account
Administrators have the ability to delete existing accounts.
3. Display All Accounts
Administrators can display a list of all registered accounts in the database.

Manage Books in Library
1. Add New Book
-Administrators can add new books to the library.
-The book title and author fields cannot be left blank.
-The quantity of the book must be filled with a positive integer.
2. Borrow and Return Books
Administrators can borrow and return books, just like regular users.
3. Display Book List
Administrators can display a list of all books available in the library.

*Validation and Error Handling
-Appropriate validation checks are in place to ensure that required fields are not left blank or filled with invalid data.
-Error messages will be displayed to guide users in case of any invalid input or operations.

*Database Integration
All account and book data is securely stored and retrieved from a database, ensuring data persistence and integrity.


*Regular User Features
After signing in, regular users will have access to the following features:

1. Display Book List
-Regular users can view a list of all available books in the library.
-The book list will provide information about the availability of each book, indicating whether it's currently in stock or borrowed.
2. Borrow Book
-Regular users can borrow books from the library.
-The system will ensure that a book is available before allowing it to be borrowed.
-Appropriate validation checks will be in place to prevent users from borrowing a book that is already checked out by another user.
3. Return Book
-Regular users can return books that they have previously borrowed.
-Upon returning a book, the system will update the book's availability status, making it accessible for other users to borrow.

*Limitations
Regular users will not have access to administrative features, such as creating or deleting accounts, adding new books, or managing other user accounts. These features are reserved for administrators to maintain the integrity and security of the library management system.

##Flowchart
Welcome Page
![welcomepage](flowchart.main_eng.png)

Database
![database](flowchart,database_eng.png)

Sign in
![signin](flowchart.login_eng.png)

Homepage Admin
![homepageadmin](flowchart.homepage_eng.png)

Manage Accounts
![manageaccounts](flowchart.account_eng.png)

Manage Books
![managebooks](flowchart.book_eng.png)

User
![user](flowchart.user_eng.png)

Users Features
![usersfeatures](flowchart.user_book_eng.png)

