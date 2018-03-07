#Use NLTK library to summarize a text file
from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.collocations import BigramCollocationFinder, BigramAssocMeasures
from nltk import bigrams

#Read a text file that we want to summarize
File = open('TextFile').read()

#Set a variable equal to the BigramAssocMeasures() function which can be used to determines the frequency of a bigram
bigram_measures = BigramAssocMeasures()

#Set a variable equal to the Lemmatizer() function which finds the base of a word (ie. removed "-ing", "s", etc.)
lem = WordNetLemmatizer()

#determine the sentences in the file
sent = sent_tokenize(File)

#Set a variable equal to the RegexpTokenizer function which will determine the words in a function and remove all punctuation
wordtokenizer = RegexpTokenizer(r'\w+')
#Find only the words in a file
words = wordtokenizer.tokenize(File)

#initiate a list
templem = []

#Iterate over each word in the file
for w in words:
    #find the base word for each word in the file
    word = lem.lemmatize(w)
    #place the base word in a list and make sure the word does not contain a uppercase letter
    templem.append(word.lower())

#determine all the bigrams in the file using the normalize words
finder = BigramCollocationFinder.from_words(templem)

#determine the frequency of the bigrams (ie. how many times it occurs in the file)
scored = finder.score_ngrams(bigram_measures.raw_freq)

#determine which 5 bigrams that have the highest frequency
topbigrams = (sorted(finder.nbest(bigram_measures.raw_freq, 5)))

firsttime = 0
sentlist = []

#iterate over each sentence
for numbsent in sent:
    #make sure the words are all lowercase
    lowercasesent = numbsent.lower()
    #determine what the bigrams are for each sentence
    bigramsent = list(bigrams(lowercasesent.split()))
    #look to see if the top 5 bigrams are found within the current sentence
    for bigram in topbigrams:
        #if the bigram is found in the sentence then save the current sentence to a list
        if ((bigram in bigramsent)== True) and (firsttime is 0):
            sentlist.append(numbsent)
            firsttime = 1
    firsttime = 0

#print all sentences that contain the top 5 bigrams which will be the summary of the text file
for number in sentlist:
    print(number)



