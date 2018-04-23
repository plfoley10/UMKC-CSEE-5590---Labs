import tensorflow
import numpy
import os
import time
import datetime
import DataFunc
import BuildTextCNN
from tensorflow.contrib import learn

#Select certain percentage of data for validation set
percentdata = 0.2
#Pos ex of data
datafpos = './data/rottentomatodata/roteentomatopol.pos'
#Neg ex of data
datafneg = './data/rottentomatodata/rottentomoatopol.neg'

#Size for Embedding
embed = 128
#The filer size will be 3, 4, and 5. Place filter in a string
fstr = "3,4,5"
#Size for filter
szfil = list(map(int, fstr.split(",")))
#Number of filters
numfil = 128
#Original dropout keep probability
dropkeep = 0.5
#Initialize l2_lambda_reg as 0.0
l2 = 0.0
#Learning Rate
learnrate = 1e-4

#Size of each batch
szbatch = 64
#Total number of epochs
epnum = 200
#Validation evaluations
evdev = 100
#Checkpoint evaluations
checkpt = 100
#Total number of checkpoints
checkptnum = 5

sftpl = True

lgpl = False

#Load data
print("\nLoad data from input files...")
xtxt, Y = DataFunc.dataset(datafpos, datafneg)

#Build vocabulary
print("\nBuilding Vocabulary...")
#Determine the maximum length of the document from the combined data of positive and negative samples
maxdoclength = max([len(X.split(" ")) for X in xtxt])
#Process the vocabulary using VocabularyProcessory from tensorflow.contrib learn
prvoc = learn.preprocessing.VocabularyProcessor(maxdoclength)
#Convert data into numpy array and use fit_transform from the vocabulary above
X = numpy.array(list(prvoc.fit_transform(xtxt)))

#-->Randomly shuffle data
#Random number generator through numpy
numpy.random.seed(10)
#Create index for start and end for randomly shuffled data
shfindex = numpy.random.permutation(numpy.arange(len(Y)))
#Shuffled value of x
Xsh = X[shfindex]
#Shuffled value of y
Ysh = Y[shfindex]

#Split data into training and testing data.
#Testing/Validation data is percentdata of data. In this case it is 20% of the data
perindex = -1 * int(percentdata * float(len(Y)))
Xtr, Xper = Xsh[:perindex], Xsh[perindex:]
Ytr, Yper = Ysh[:perindex], Ysh[perindex:]

#Training
#Create the tensorflow graph and session
with tensorflow.Graph().as_default():
    #Define session configuration
    configuration = tensorflow.ConfigProto(allow_soft_placement=sftpl,log_device_placement=lgpl)
    #Create the session using the configuration created above
    Sess = tensorflow.Session(config=configuration)
    with Sess.as_default():
        #Classify text using TextCNN from file TextConvNet. THis is the convolution neural network for text
        #classification
        CNN = BuildTextCNN.TextCNN(lengthseq=Xtr.shape[1],clsnum=Ytr.shape[1],
                                              voc=len(prvoc.vocabulary_),embed=embed,
                                              szfil=szfil,numfil=numfil,l2rlambda=l2)

        # Define Training procedure
        #Define the global step and create variable tensor
        stpglobal = tensorflow.Variable(0, name="stpglobal", trainable=False)
        #Create optimizer with a learning rate of learning_rate
        opt = tensorflow.train.AdamOptimizer(learnrate)
        #Determine gradients and variables
        gradient = opt.compute_gradients(CNN.loss)
        #Create training optimizer
        trainop = opt.apply_gradients(gradient, global_step=stpglobal)
        #Determine the values of gradient values and sparsity
        gradsum = []
        for g, v in gradient:
            if g is not None:
                #Write gradient history summary
                gradhistsum = tensorflow.summary.histogram("{}/grad/hist".format(v.name), g)
                #Write sparsity summary
                sparsitysum = tensorflow.summary.scalar("{}/grad/sparsity".format(v.name),
                                                             tensorflow.nn.zero_fraction(g))
                #Add to grad_Summaries from gradient history and sparsity history
                gradsum.append(gradhistsum)
                gradsum.append(sparsitysum)
        #Merge summary for grad_summaries
        gradsummerged = tensorflow.summary.merge(gradsum)

        #Determine directory for output of the models and summary
        #timestamp
        timestamp = str(int(time.time()))
        #Output directory
        outdir = os.path.abspath(os.path.join(os.path.curdir, "runs", timestamp))

        #Loss Summary
        losssum = tensorflow.summary.scalar("loss", CNN.loss)
        #Accuracy Summary
        accsum = tensorflow.summary.scalar("accuracy", CNN.accuracy)

        #Train Summaries
        #Train summary optimizer
        trainsumop = tensorflow.summary.merge([losssum, accsum, gradsummerged])
        #Train summary directory
        trainsumdir = os.path.join(outdir, "summaries", "train")
        #Train summary writer
        trainsumwriter = tensorflow.summary.FileWriter(trainsumdir, Sess.graph)

        #Validation Set Summaries
        #Validation summary optimizer
        devsumop = tensorflow.summary.merge([losssum, accsum])
        #Validation summary directory
        devsumdir = os.path.join(outdir, "summaries", "dev")
        #Validation summary writer
        devsumwriter = tensorflow.summary.FileWriter(devsumdir, Sess.graph)

        #Checkpoint directory within current directory
        #Directory for created checkpoints
        checkpointdir = os.path.abspath(os.path.join(outdir, "checkpoints"))
        checkpointprefix = os.path.join(checkpointdir, "model")
        #Check if directory exists. If yes, create a new one
        if not os.path.exists(checkpointdir):
            os.makedirs(checkpointdir)
        #Save to tensorboard
        saver = tensorflow.train.Saver(tensorflow.global_variables(), max_to_keep=checkptnum)

        #Write vocabulary
        prvoc.save(os.path.join(outdir, "vocab"))

        #Initialize variables
        Sess.run(tensorflow.global_variables_initializer())

        #Generate batches inside FileFuntion
        batches = DataFunc.iterbatch(
            list(zip(Xtr, Ytr)), szbatch, epnum)
        #Training loop.
        for batch in batches:
            #Separate batch into x_batch and y_
            Xbatch, Ybatch = zip(*batch)
            #Define the feed_dict to load into tensorflow placeholders for conv_neural_net for training
            feeddict = {
                CNN.Xin: Xbatch,
                CNN.Yin: Ybatch,
                CNN.dropkeep: dropkeep
            }
            #Run the training iteration inside each batch. Returns the step, summaries, loss, and accuracy
            _, step, summaries, loss, accuracy = Sess.run(
                [trainop, stpglobal, trainsumop, CNN.loss, CNN.accuracy],
                feeddict)
            #Create a timestamp for each training iteration
            timestr = datetime.datetime.now().isoformat()
            print("{}: step {}, loss {:g}, acc {:g}".format(timestr, step, loss, accuracy))
            trainsumwriter.add_summary(summaries, step)

            currentstep = tensorflow.train.global_step(Sess, stpglobal)

            #Validation part of training
            if currentstep % evdev == 0:
                print("\nEvaluation:")
                # Define the feed_dict to load into tensorflow placeholders for conv_neural_net for validation
                feeddict = {
                    CNN.Xin: Xbatch,
                    CNN.Yin: Ybatch,
                    CNN.dropkeep: 1.0
                }
                #Run the validation iteration inside each batch. Returns the step, summaries, loss, and accuracy
                step, summaries, loss, accuracy = Sess.run(
                    [stpglobal, devsumop, CNN.loss, CNN.accuracy],
                    feeddict)
                # Create a timestamp for each training iteration
                timestr = datetime.datetime.now().isoformat()
                print("{}: step {}, loss {:g}, acc {:g}".format(timestr, step, loss, accuracy))
                #Write validation summary
                if devsumwriter:
                    devsumwriter.add_summary(summaries, step)
                print("")
            #Save model after each checkpoint
            if currentstep % checkpt == 0:
                path = saver.save(Sess, checkpointprefix, global_step=currentstep)
                print("Saved model checkpoint to {}\n".format(path))