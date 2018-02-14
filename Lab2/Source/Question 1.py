#This code displays the book names of any book that fits the range the customer wants to spend
# Create a dictionary with the book names as the key and the cost as the value.
books = {'python' : 50, 'web': 30, 'c': 20, 'java': 40}
# Initialize a list
cost = []

# Ask the user to enter a minimum and maximum amount they would like to spend.
minimum = int(input("Please enter a minimum value:"))
maximum = int(input("Please enter a maximum value:"))

# Execute the loop for the number of items in the dictionary
for x in books:
    # Extract the values one at a time and place them in a list
    cost = books.get(x)
    # Determine if there is a value in the range the customer wants
    if minimum <= cost <= maximum:
        # Execute the loop for the values in the dictionary
        for bookname, value in books.items():
            # If the value is equal to the cost then print the book name
            if value == cost:
                print(bookname)