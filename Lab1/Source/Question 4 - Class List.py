"""This program compares two lists of students from two different classes and determines if there are students
that are taking both classes. If the student is in both classes save the name a list and if the student is only in one
class then save the name to a different list."""

# This function prompts the user to enter the class lists for the two different classes.
def ClassList():
    global PythonClassList
    global WebAppClassList
    PythonClassList = []
    WebAppClassList = []
    # Initializing the two while loops.
    pythonprofessorinput = 'yes'
    webappprofessorinput = 'yes'
    # The while loop will continue as long as the user enters yes to having more students.
    while pythonprofessorinput == 'yes':
        PythonClassListInput = input("Please enter Python Class Student Name:")
        pythonprofessorinput = input("Do you have another student?:")
        PythonClassList.append(PythonClassListInput)
    # The while loop will continue as long as the user enters yes to having more students.
    while webappprofessorinput == 'yes':
        WebAppClassListInput = input("Please enter Web Application Class List:")
        webappprofessorinput = input("Do you have another student?:")
        WebAppClassList.append(WebAppClassListInput)

# This function determines if the student is in one or both classes.
def BothClasses():
    i = 0
    z = 0
    InBothClasses = []
    OnlyInOneClass = []
    for x in PythonClassList:
        # If the student is in both classes then update the InBothClasses list.
        if (PythonClassList[i] in WebAppClassList) == True:
            InBothClasses.append(PythonClassList[i])
        # If the student is in only one class then update the OnlyInOneClass list.
        else:
            OnlyInOneClass.append(PythonClassList[i])

        i = i + 1

    for w in WebAppClassList:
        # Determine the students who have not been included in the OnlyInOneClass list.
        if (WebAppClassList[z] in PythonClassList) == False:
            OnlyInOneClass.append(WebAppClassList[z])

        z = z + 1

    print("These students are in both classes:", InBothClasses)
    print("These students are only in one class:", OnlyInOneClass)


ClassList()

BothClasses()