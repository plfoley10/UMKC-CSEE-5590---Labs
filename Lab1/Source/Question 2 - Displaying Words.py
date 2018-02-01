"""This program prompts a user to enter a sentence. Once the sentence has been entered the program determines the
middle word, the longest word, and then reverses the words in the sentence. The results are displayed to the user."""

# This function prompts the user to enter a sentence.
def UserSentence ():
    global UserInput
    UserInput = input ("Please enter a sentence:")
    global SentenceList
    # Place the sentence into a list.
    SentenceList = UserInput.split()

# This function determines the middle word in the sentence.
def MiddleWords ():
    # Determine the length of the sentence.
    numberofelements = len(SentenceList)
    midnumb = 0.0
    # Determine the middle of the sentence.
    midnumb = numberofelements / 2
    # If the sentence only has 1 or 2 words then print the sentence.
    if numberofelements <= 2:
        print("Middle word is:", SentenceList)
    # If the sentence has an even number of words then print the two middle words.
    elif numberofelements % 2 == 0:
        lownumb = int(midnumb - 0.5)
        print("Middle word is:", SentenceList[lownumb:(lownumb + 2)])
    # If the sentence has an odd number of words then print the middle word.
    else:
        intmidnumb = int(midnumb)
        print("Middle word is:", SentenceList[intmidnumb])

# This function determines the longest word in the sentence.
def LongestWords ():
    longest = ''
    longwords = []
    # Loop for the number of elements in the list
    for s in SentenceList:
        # Check to see if the current word is longer than the previous word.
        if len(longest) < len(s):
            longest = s
            longwords = [s]
        # If the current word is longer than the previous word than save the new word.
        elif len(longest) == len(s):
            longwords.append(s)
    print("Longest word is:", longwords)

# Reverse the letters in the sentence but not the word order.
def ReverseLetters ():
    print(UserInput[::-1])


UserSentence()

MiddleWords()

LongestWords()

ReverseLetters()