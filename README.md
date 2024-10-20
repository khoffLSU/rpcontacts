# Realpython Project: Build a Contact Book App With Python, Textual, and SQLite

In this Let's code following a realpython tutorial:

- Create the contact book app’s TUI using Textual
- Handle the database operations using SQLite
- Connect the app’s TUI with the database code and make it functional

At the end of this project a functional contact book application will created allowing storage, retrival and management of contact information.

[Url for the tutorial](https://realpython.com/contact-book-python-textual/)

# Step 1: Create the Contact Book’s App With Textual

In this first step, you’ll create a minimal TUI application to provide the foundation on which you’ll start to build the contact book. You’ll also create the required project structure.

# Step 2: Build the Contact Book’s TUI

Now that the skeleton of the contact book app is built, start coding the main TUI. In this TUI, you have two main components. On the left side, you have the contacts list, which includes the contact’s name, phone number, and email address. On the right side, you have a panel with three buttons:

1. Add to add a new contact to the list
2. Delete to remove the selected contact from the list
3. Clear All to remove all contacts from the list

# Step 3: Set Up the Contact Book’s Database

At this point the Textual app has an appropriate TUI to build a contact book. In this section, code with be written to operate an SQLite database where the app will store the contact information persistently.  

The database operations will be directly related to the features of the contact book app. The app will need to do the following actions on the database:

- Retrieve all the contacts
- Get the last contact
- Add a new contact
- Delete an existing contact
- Clear all contacts

# Step 4: Display Existing Contacts on the App’s TUI

To display the contacts’ data in the application’s main TUI, we first load that information from the database. Then we will display the retrieved data in the contacts list of the TUI. Get the contacts’ data from the database using the Database class and its .get_all_contacts() method. For this we only need to pass an instance of this class to ContactsApp.

# Step 5: Add New Contacts to the Database and TUI

The contact book application has an appealing TUI that can load and display the information about your existing contacts. In this section the code required to add new contacts to the database will be added. The first step in accomplishing this is to create the Add Contact dialog.