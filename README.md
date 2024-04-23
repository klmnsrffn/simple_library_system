## Overview
This project is a simple library management system. Both administrators and regular users can sign in through the same sign-in page, but they will be directed to different features based on their account type (admin or regular user).

## Administrator Features :
-Create accounts for administrators and regular users
-Delete existing accounts
-Add new books to the library
-Utilize the borrow and return book features

## Regular User Features:
-Borrow books from the library
-Return borrowed books

## How it Works?
-Upon accessing the system, users will be prompted to sign in.
-After successful sign-in, administrators will have access to the administrative features mentioned above, while regular users will only have access to the borrow and return book features.
-Administrators can manage accounts, add new books to the library, and handle book borrowing and returning operations.
-Regular users can browse the available books and borrow or return them as needed.

## Admin Features
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

* Validation and Error Handling
-Appropriate validation checks are in place to ensure that required fields are not left blank or filled with invalid data.
-Error messages will be displayed to guide users in case of any invalid input or operations.

* Database Integration
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

## Flowchart

### Welcome Page
![main_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/aa9effec-d927-45d6-ab3b-365270e60091)


### Database
![database_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/8d57d2c3-3f2b-4041-9d2e-e8a6fa6d5566)


### Sign in
![login_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/4316c991-e66b-4764-bd32-69b99342207d)


### Homepage Admin
![homepage_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/98e820c1-1bb2-4896-9c90-94a8d5a9f61f)


### Manage Accounts
![account_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/1773722f-4839-4e40-9bcb-0e0c045c5498)


### Manage Books
![book_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/944391b3-43c0-4647-95f8-8d1c7ad5497e)


### User
![user_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/db156d94-5748-48ed-bb9f-19bfe490c3c2)

### Users Features
![user_book_eng](https://github.com/klmnsrffn/simple_library_system/assets/165617982/f838fea7-cbd6-480b-ad9c-a3824475a34b)
