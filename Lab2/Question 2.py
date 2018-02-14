"""This code allows the user to select four different choices: display the contact by entering the name, display the
contact by the number, edit the contact by entering the name and then what needs to be updated, and exit the contact
list."""

#What values should the user initially use.
AcceptableEntries = ['a','b','c','d']
#Initiate the while loop.
KeepSelecting = 'yes'
global ContactList
#What is the contact list.
ContactList=[{'name': 'Rashmi', 'number': '8797989821', 'email': 'rr@gmail.com'},
             {'name': 'Saria', 'number': '9897989821', 'email': 'ss@gmail.com'}]

#Function to accept the user input.
def UserSelection ():
    global UserInput
    #User can select either a, b, c, or d.
    UserInput = input("Select one of the following by entering a, b, c, or d:"'\n'
                      "a) Display contact by name"'\n'
                      "b) Display contact by number"'\n'
                      "c) Edit contact by name"'\n'
                      "d) Exit"'\n'
                      "Your Selection:"'\n')

#Function to print the contact list.
def DisplayContactList():
    print(ContactList)

#Function to check if what was entered after the initial selections can be found in the contact list.
def ValueInList(x):
    NameToEdit = x
    InContacts = 'no'
    select = 0
    #Iterate for the number of dictionaries in the Contact List
    for w in ContactList:
        #Look at each dictionary individually
        single = ContactList[select]
        #If the user input can be located in the contact list than initialize the while loops.
        if NameToEdit in single.values():
            InContacts = 'yes'
        select = select + 1
    #If user input cannot be found in the contact list. Then notify the user the value cannot be found.
    if InContacts == 'no':
        print("Input is not in contact list")
    return InContacts

#Display all contact information associated with a name or number
def DisplaySelectedContact(x):
    #User enters a name or number
    if x == 'a':
        NameorNumber = input("Please Enter Contact Name:")
    elif x == 'b':
        NameorNumber = input("Please Enter Contact Number:")
    index = 0
    #Determine if input is in contact list.
    InContacts = ValueInList(NameorNumber)
    while InContacts == 'yes':
        #Iterate for the number of dictionaries in contact list
        for x in ContactList:
            #Save the single dictionary into a temporary list
            singledictionary = ContactList[index]
            #If the user input is found. Print the contact
            if NameorNumber in singledictionary.values():
                print(singledictionary)
            index = index + 1
            #Stop while loop after all dictionaries are looked at.
            if index == len(ContactList):
                InContacts = 'no'

#Make changes to the value of the key that was selected.
def PossibleEdits(w,d,i):
    #If "a" was selected than an update to the name will occur.
    if w == 'a':
        update = input("What would you like to change the name to?:")
        key = 'name'
    # If "b" was selected than an update to the number will occur.
    elif w == 'b':
        update = input("What would you like to change the nnumber to?:")
        key = 'number'
    # If "c" was selected than an update to the email will occur.
    elif w == 'c':
        update = input("What would you like to change the email to?:")
        key = 'email'
    #Update the value in the dictionary
    d[key] = update
    #Update the contact list to have the correct value.
    ContactList[i] = d
    #Print the update
    print(ContactList[i])
    MakeSelection = 'no'
    return MakeSelection

#The user would like to edit a contact list. The user must enter the name of the contact that they would like to update
def EditContact():
    #User inputs the name
    NameToEdit = input("Please Enter the Name you Would Like to Edit:")
    index = 0
    CorrectSelection = ['a','b','c']
    MakeTheSelection = 'yes'
    #Check to see if the value is in the contact list.
    InContacts = ValueInList(NameToEdit)
    while InContacts == 'yes':
        #Interate for the number of dictionaries in the contact list.
        for x in ContactList:
            #Save the single dictionary into a temporary list
            singledictionary = ContactList[index]
            #See if the name is in the single dictionary
            if NameToEdit in singledictionary.values():
                while MakeTheSelection == 'yes':
                    #Ask the user what they would like to edit
                    WhatToEdit = input("Select one of the following to edit by entering a, b, or c:"'\n'
                                       "a) Name"'\n'
                                       "b) Number"'\n'
                                       "c) Email"'\n'
                                       "Your Selection:")
                    #Determine if the input was valid
                    if WhatToEdit in CorrectSelection:
                        #Update the dictionary and contact list accordingly
                        MakeTheSelection = PossibleEdits(WhatToEdit, singledictionary, index)
                    #If input was not valid. Let the user know and have them select again.
                    else:
                        print("Not the correct selection")
                        MakeTheSelection = 'yes'
            index = index + 1
            if index == len(ContactList):
                InContacts = 'no'

#The user has no more information that they need or does not need to edit a contact
def ExitContactList():
    KeepSelecting = 'no'
    return KeepSelecting

#main program. keep looping till the user is done
while KeepSelecting == 'yes':
    #display the contact list
    DisplayContactList()
    # Function to accept the user input.
    UserSelection()
    #Check that the input was valid
    if UserInput in AcceptableEntries:
        #User would like to display contact by entering the name
        if UserInput == 'a':
            DisplaySelectedContact(UserInput)
        #User would like to display contact by entering the number
        elif UserInput == 'b':
            DisplaySelectedContact(UserInput)
        #User would like to edit a contact.
        elif UserInput == 'c':
            EditContact()
        #User would like to exit the program
        elif UserInput == 'd':
            KeepSelecting = ExitContactList()
    #If selection is not valid let the user know.
    else:
        print("User Entry is Not Valid. Please Select either a, b, c, or d")
        UserSelection()






