"""This program prompts a user to enter a password. The password has certain requirements that must be met.
The requirements are expressed to the user first. After the password is entered by the user the program checks
to make sure the password meets all requirements. If the requirements are not met then the user is told what
was wrong and asked to enter another password."""
def PasswordRequirements ():
    # This function explains the requirements for the password.
    print ("Password requirements are the following:",
           "1)The password length should have a range of 6-16 characters.",
           "2)Should have at least one number.",
           "3)Should have one of the follow special characters: $, @, !, or *",
           "4)Should have one lowercase and one uppercase character", sep="\n")

def EnterPassword ():
    # This function asks the user to enter a password.
    global password
    password = input('Enter Password Here:')

def CheckPasswordLength ():
    # This fuction determines the length of the password.
    global length
    length = len(password)

def CheckForNumber(s):
    # This function checks that there is at least one number in the password.
    return any(i.isdigit() for i in s)

def CheckForCharacter (s):
    # This function checks to see that the password contains at least one special character.
    chars = set('[$@!*]')
    return any((c in chars) for c in s)

def CheckForLetters (s):
    # This function checks to see if there are letters in the password.
    return any(c.isalpha() for c in s)


def CheckForCase (s):
    # This function checks to see that there is at least one upper case and one lower case letter in the password.
    return s.isupper()

# State the password requirements
PasswordRequirements ()

i = 0
while i < 1:
    # User enters password.
    EnterPassword()
    # Determine the length of the password
    CheckPasswordLength()
    # If the length is between 6 to 16 then check the next requirement.
    if ( 6 <= length <= 16):
        # If the password has at least one number then check the next requirement.
        if CheckForNumber(password) == True:
            # If the password has at least one special character then check the next requirement.
            if CheckForCharacter(password) == True:
                if CheckForLetters(password) == True:
                    # If the password has at least one upper case and one lower case then check the next requirement.
                    if (CheckForCase(password) != True):
                        i = 1
                    # The password must have at least one uppercase and one lowercase letter.
                    else:
                        print("Password does not contain one lowercase and one uppercase letter.",
                        "The password must have one lowercase and one uppercase character.", sep="\n")
                # The password must contain a letter.
                else:
                    print("Password does not contain a letter.",
                          "The password must have at least two letters. One uppercase and one lowercase.", sep="\n")
            # If the password doesn't contain a special character then tell the user.
            else:
                print("Password does not contain a special character.",
                      "The password must have one of the follow special characters: $, @, !, or *.", sep="\n")
        # If the password doesn't have at least one number then tell the user.
        else:
            print("Password does not contain a number.",
                  "The password must contain at least one number.", sep="\n")
    # If the length isn't between 6 to 16 then tell the user the password doesn't meet the length requirements.
    else:
        print("Password does not meet length requirements.",
              "The password length should have a range of 6-16 characters.", sep="\n")
