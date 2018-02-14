#Using numpy to create a random array
import numpy as np
#Create an array of 15 random interger numbers from 0 to 20.
a = np.random.randint(0, high = 20, size = (15))
print(a)
print('\n')
#Count the frequency of each number.
y = np.bincount(a)

index = 0
num = 0
temp = []

#Iterate over each element in the array y
for number in y:
    #If it is the first iteration than save the first element of y into a temporary list
    if index == 0:
        temp.clear()
        temp.append(y[index])
    #Check to see if there is a different element that is larger than the previous one.
    elif temp[num] < (y[index]):
        temp.clear()
        #If number in y is larger than number in temp. Clear temp and save number in y into temp list.
        temp.append(y[index])
    #Check to see if there is an element that is equal to the number in the temp list
    elif (index != 0) and (temp[num] == (y[index])):
        #Place the number into the temp list.
        temp.append(y[index])
    index = index + 1

#If temporary list only has one number than print argmax function will work.
if len(temp) == 1:
    #Find the largest number in y and print it
    z = np.argmax(y)
    print('The most frequenct number is:')
    print(z)
else:
    freqnumb = []
    yindex = 0
    # Iterate over each element in the array y
    for w in y:
        #Check to see if the value saved in temp is in y
        if temp[0] == w:
            #If so then place index of value into a list
            freqnumb.append(yindex)
        yindex = yindex + 1
    print('The most frequenct numbers are:')
    print(freqnumb)

