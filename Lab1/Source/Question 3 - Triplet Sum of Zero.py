"""This program determines which set of 3 numbers sums to zero. When the triplets are determine the program prints
the sets."""
# This functions takes a random set of numbers and determines the length of the list.
def RandomNumbers():
    global randomnumb
    global length
    randomnumb = []
    randomnumb = [1, 3, 6, 2, -1, 2, 8, -2, 9]
    length = len(randomnumb)

# This function runs through each possible set of 3 numbers and determines if they sum to zero.
def SumstoZero():
    temp = []
    TripleSumZero = []
    numbingroup = 3
    x = 0
    secondindex = 1
    thirdindex = 2
    firstindex = 0
    zeroindex = 0
    # Depending on how many elements are in the list determines how many times the loop is executed.
    for x in range (0,(length -(numbingroup-1))):
        #  This loop determines the first number in the set of 3.
        while x < (length -(numbingroup-1)):
            # This loop determines the second number in the set of 3.
            while secondindex < (length -1):
                # This loop determines the third number in the set of 3.
                while thirdindex < length:
                    # Sum the 3 numbers together.
                    sum = randomnumb[firstindex] + randomnumb[secondindex] + randomnumb[thirdindex]
                    # If the sum is zero then save the values into a list.
                    if sum == 0:
                        temp.append(randomnumb[firstindex])
                        temp.append(randomnumb[secondindex])
                        temp.append(randomnumb[thirdindex])
                        TripleSumZero.append(temp)
                        temp = []
                        zeroindex = zeroindex + 1
                    thirdindex = thirdindex + 1
                secondindex = secondindex + 1
            x = x + 1
            secondindex = x + 1
            thirdindex = secondindex + 1
        firstindex = firstindex + 1
        secondindex = firstindex + 1
        thirdindex = secondindex + 1
    # Once all sets of 3 are determined print the sets.
    print(TripleSumZero)

RandomNumbers()

SumstoZero()