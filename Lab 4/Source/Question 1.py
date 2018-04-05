#Using MNIST data
#Model Logistic Regression
#Import the different libraries
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#Input the MNIST data set
#Set One_Hot to True means to use a vector to represent the data. All will be zero except the value will be set to 1.
Mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Parameters for the model
LearningRate = 0.01
TrainingEpochs = 25
BatchSize = 100
Step = 1

#These are the placeholders for the data X and Y
#Use 784 since MNIST data is an image with a shape of 28x28
X = tf.placeholder(tf.float32, [None, 784], name='X')
#10 classes since the digits are from 0 to 9
Y = tf.placeholder(tf.float32, [None, 10], name='Y')

#Create Variables for the models: weights and biases
W = tf.Variable(tf.zeros([784, 10]), name='Weights')
B = tf.Variable(tf.zeros([10]), name='Biases')

#Build the model and use softmax to normalize the model and produce the probability
Ypred = tf.nn.softmax(tf.matmul(X, W) + B)

# Minimize error using cross entropy
loss = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(Ypred), reduction_indices=1), name = 'loss')

# Gradient Descent to minimize loss
optimizer = tf.train.GradientDescentOptimizer(LearningRate).minimize(loss)

#Start the session
with tf.Session() as sess:
    #Initialize all the variables
    sess.run(tf.global_variables_initializer())
    #Start the writer for tensorboard
    writer = tf.summary.FileWriter('./graphs/logistic_reg', sess.graph)
    # Train the model
    for epoch in range(TrainingEpochs):
        AvgLoss = 0.
        iterations = int(Mnist.train.num_examples / BatchSize)
        # Loop over all batches
        for i in range(iterations):
            batch_xs, batch_ys = Mnist.train.next_batch(BatchSize)
            # Run optimization op and cost op (to get loss value)
            _, l = sess.run([optimizer, loss], feed_dict={X: batch_xs,
                                                          Y: batch_ys})
            # Compute average loss
            AvgLoss += l / iterations
        #Display loss per epoch step
        print("Epoch:", '%02d' % (epoch + 1), "loss =", "{:.9f}".format(AvgLoss))

    #Close the writer for tensorboard
    writer.close()

    #Test the model
    correct_prediction = tf.equal(tf.argmax(Ypred, 1), tf.argmax(Y, 1))
    #Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print("Accuracy:", accuracy.eval({X: Mnist.test.images, Y: Mnist.test.labels}))