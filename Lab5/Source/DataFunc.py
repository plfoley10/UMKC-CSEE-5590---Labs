import numpy
import re

#This function takes the input text and then line by line, cleans up the data by removing the special
#characters and other unwanted characters
def stanadardizedata(textstr):
    textstr = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", textstr)
    textstr = re.sub(r"\'s", " \'s", textstr)
    textstr = re.sub(r"\'ve", " \'ve", textstr)
    textstr = re.sub(r"n\'t", " n\'t", textstr)
    textstr = re.sub(r"\'re", " \'re", textstr)
    textstr = re.sub(r"\'d", " \'d", textstr)
    textstr = re.sub(r"\'ll", " \'ll", textstr)
    textstr = re.sub(r",", " , ", textstr)
    textstr = re.sub(r"!", " ! ", textstr)
    textstr = re.sub(r"\(", " \( ", textstr)
    textstr = re.sub(r"\)", " \) ", textstr)
    textstr = re.sub(r"\?", " \? ", textstr)
    textstr = re.sub(r"\s{2,}", " ", textstr)
    return textstr.strip().lower()

#This function pulls data from the dataset. It reads the dataset line by line
#and removes the special characters. Once the characters are removed then labels are generated and saved
def dataset(datafpos, datafneg):
    #read it line by line
    posexam = list(open(datafpos, "r").readlines())
    #Strip the data contained in the pos dataset
    posexam = [s.strip() for s in posexam]
    #read it line by line
    negexam = list(open(datafneg, "r").readlines())
    #Strip the dadta contained in the neg dataset
    negexam = [s.strip() for s in negexam]
    # combine both datasets into one
    xtxt = posexam + negexam
    #Clean the data
    xtxt = [stanadardizedata(sentence) for sentence in xtxt]
    # Generate labels
    poslb = [[0, 1] for _ in posexam]
    
    neglb = [[1, 0] for _ in negexam]
    #combine labels into one array
    y = numpy.concatenate([poslb, neglb], 0)

    return [xtxt, y]

#Split data into batches
def iterbatch(dataset, szbat, epnum, shuffle=True):
    #Place the dataset into a numpy array
    dataset = numpy.array(dataset)
    #Determine size
    szdata = len(dataset)
    #Determine the number of batches per epoch
    epbat = int((len(dataset)-1)/szbat) + 1
    #Go through each epoch epnum times
    for ep in range(epnum):
        #Shuffle data. Default is to shuffle
        if shuffle:
            #Determine the index for the shuffled data
            ind = numpy.random.permutation(numpy.arange(szdata))
            shufdat = dataset[ind]
        
        else:
            shufdat = dataset
        #Determine start and end index for each batch
        #data
        for x in range(epbat):
            intial = x * szbat
            finish = min((x + 1) * szbat, szdata)
            yield shufdat[intial:finish]