#Airline Booking Reservation System
#Creating the flight class
class Flight:
    #Constructor to initialize the flight number
    def __init__(self, number):
        #flight number
        self.number = number
#Creating the person class
class Person:
    # Constructor to initialize the first and last name of the person
    persontotal = 0
    def __init__(self, name, family):
        #Person's first name
        self.name = name
        #Person'ts last name
        self.lastname = family

        Person.persontotal = Person.persontotal + 1
    #Create a private variable that stores the number of people
    __privatetotal = persontotal
#Creating the employee class
class Employee:
    # Constructor to initialize the first and last name of the employee along with the employee number
    def __init__(self, name, family, number):
        #Employee's first name
        self.name = name
        #Employee's last name
        self.family = family
        #Employee's number
        self.employeenumber = number

#Creating the Arrival Time Class and it inherits the Flight Class methods
class ArrivalTime(Flight):
    # Constructor to initialize the flight number and the arrival time of the flight
    def __init__(self, number: object, time: object) -> object:
        #Using super function to set the method for the flight number
        super().__init__(number)
        #Arrival Time
        self.time = time

#Creating the Passenger Class and it inherits both the methods for the Person class and ArrivalTime Class
class Passenger(Person,ArrivalTime):
    # Constructor to initialize the first and last name of the passenger, the flight number, and the arrival time
    def __init__(self, name, family, number, time):
        #Constructor to set the same method's as Person Class.
        Person.__init__(self, name, family)
        #Constructor to set the same method's as ArrivalTime Class.
        ArrivalTime.__init__(self, number, time)

#Create an instance for the Flight Class
flight1 = Flight(123)
#Create an instance for the Person Class
person1 = Person('Jane', 'Doe')
#Create an instance for the Employee Class
employee1 = Employee('Bob', 'Smith', 567)
#Create an instance for the Arrival Time Class
arrival = ArrivalTime(456, '4:00 pm')
#Create an instance for the Passenger Class
passenger1 = Passenger('Jane', 'Doe', 123, '4:00 pm')

#Checking what attributes are in what class.
print('Does Flight, ArrivalTime, and Passenger classes have the attribute "number":')
if (hasattr(flight1, 'number')) == (hasattr(arrival, 'number')):
    if (hasattr(passenger1, 'number')) == True:
        print('Yes they do.')
    else:
        print('No they do not.')

print('Does ArrivalTime and Passenger classes have the attribute "arrival time":')
if (hasattr(arrival, 'time')) == (hasattr(passenger1, 'time')):
    print('Yes they do.')
else:
    print('No they do not.')

print('Does Person and Passenger classes have attributes "name" and "family":')
if (hasattr(person1, 'name')) == (hasattr(passenger1, 'name')):
    if (hasattr(person1, 'family')) == (hasattr(passenger1, 'family')):
        print('Yes they do.')
    else:
        print('They only have the "name" attribute.')
else:
    print('No they do not.')