#Using MNIST data
#Model Logistic Regression
#Import the different libraries
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#Inport the MNIST data set
Mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#Model Parameters
LearningRate = 0.001
TrainingEpochs = 50
BatchSize = 200
Step = 1

#These are the placeholders for the data X and Y
#Use 784 since MNIST data is an image with a shape of 28x28
Xmatrix = tf.placeholder(tf.float32, [None, 784], name='Xmatrix')
#10 classes since the digits are from 0 to 9
Ymatrix = tf.placeholder(tf.float32, [None, 10], name='Ymatrix')

#Variables for the models: biases and weights
Weights = tf.Variable(tf.zeros([784, 10]), name='Weights')
Biases = tf.Variable(tf.zeros([10]), name='Biases')

#Build the model and use softmax to normalize the model and produce the probability
Ypred = tf.nn.softmax(tf.matmul(Xmatrix, Weights) + Biases)

# Minimize error using cross entropy
losscalc = tf.reduce_mean(-tf.reduce_sum(Ymatrix * tf.log(Ypred), reduction_indices=1), name = 'losscalc')

# Gradient Descent to minimize loss
opt = tf.train.GradientDescentOptimizer(LearningRate).minimize(losscalc)

#Start the session
with tf.Session() as sess:
    #Initialize all the variables
    sess.run(tf.global_variables_initializer())
    #Start the writer for tensorboard
    writertb = tf.summary.FileWriter('./graphs/logistic_reg', sess.graph)
    # Train the model
    for z in range(TrainingEpochs):
        AvgLoss = 0.
        iterations = int(Mnist.train.num_examples / BatchSize)
        #Iterate through all the different groups
        for a in range(iterations):
            Xmodel, Ycalc = Mnist.train.next_batch(BatchSize)
            # Calculate the loss by running opt and loss calc
            _, l = sess.run([opt, losscalc], feed_dict={Xmatrix: Xmodel,
                                                          Ymatrix: Ycalc})
            # Compute average loss
            AvgLoss += l / iterations
        #Display loss per epoch step
        print("Epoch:", '%02d' % (z + 1), "loss =", "{:.9f}".format(AvgLoss))

    #Close the writer for tensorboard
    writertb.close()

    #Test the model
    RightPrediction = tf.equal(tf.argmax(Ypred, 1), tf.argmax(Ymatrix, 1))
    #Calculate the accuracy of the model
    acc = tf.reduce_mean(tf.cast(RightPrediction, tf.float32))
    print("Accuracy:", acc.eval({Xmatrix: Mnist.test.images, Ymatrix: Mnist.test.labels}))