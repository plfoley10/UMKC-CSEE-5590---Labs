import tensorflow

class TextCNN(object):
    # lengthseq is the length of our sentences
    # clsnum is the number of classes in output layer
    # voc is the size of vocabulary
    # embed is the size of embeddings
    # szfil is the number of words
    # numfil is the number of filters per filter size
    def __init__(
      self, lengthseq, clsnum, voc, embed, szfil, numfil, l2rlambda=0.0):

        # Create placeholders for Xin, Yin and dropkeep
        self.Xin = tensorflow.placeholder(tensorflow.int32, [None, lengthseq], name="Xin")
        self.Yin = tensorflow.placeholder(tensorflow.float32, [None, clsnum], name="Yin")
        self.dropkeep = tensorflow.placeholder(tensorflow.float32, name="dropkeep")

        # Create a constant for the l2 regularization loss
        l2_loss = tensorflow.constant(0.0)

        # Map vocab by using an embedding layer
        # Excute on CPU instead of using the GPU
        
        with tensorflow.device('/cpu:0'), tensorflow.name_scope("embedding"):
            
            # Create variable for the weights
            self.W = tensorflow.Variable(tensorflow.random_uniform([voc, embed], -1.0, 1.0),name="W")
            self.embch = tensorflow.nn.embedding_lookup(self.W, self.Xin)
            self.embchexp = tensorflow.expand_dims(self.embch, -1)

        # First step to construct convolutional layers
        # Next max-pooling

        outs = []
        for i, filtersize in enumerate(szfil):
            with tensorflow.name_scope("conv-maxpool-%s" % filtersize):
                # Layer for Convolution
                filshape = [filtersize, embed, 1, numfil]
                W = tensorflow.Variable(tensorflow.truncated_normal(filshape, stddev=0.1), name="W")
                b = tensorflow.Variable(tensorflow.constant(0.1, shape=[numfil]), name="b")
                conv = tensorflow.nn.conv2d(self.embchexp,W,strides=[1, 1, 1, 1],padding="VALID",
                                            name="conv")
                # Nonlinearity Application
                h = tensorflow.nn.relu(tensorflow.nn.bias_add(conv, b), name="relu")
                # Maxpooling over the outputs
                pd = tensorflow.nn.max_pool(h,ksize=[1, lengthseq - filtersize + 1, 1, 1],strides=[1, 1, 1, 1],
                                                padding='VALID',name="pool")
                outs.append(pd)

        #Combine into feature vector
        numfiltot = numfil * len(szfil)
        self.hpool = tensorflow.concat(outs, 3)
        self.hpoolflat = tensorflow.reshape(self.hpool, [-1, numfiltot])

        # Dropout Layer
        # Dropout later desables a fraction of its neurons. This prevents neurons from co-adapting
        # and forces them to learn individually useful features

        # Add the dropout layer
        with tensorflow.name_scope("dropout"):
            self.hdrop = tensorflow.nn.dropout(self.hpoolflat, self.dropkeep)

        # Determine prediction and score from feature vector from max pooling with the dropout applied
        # Complete matrix multiplication and pick the class with highest score
        with tensorflow.name_scope("output"):
            W = tensorflow.get_variable("W",shape=[numfiltot, clsnum],
                                        initializer=tensorflow.contrib.layers.xavier_initializer())
            b = tensorflow.Variable(tensorflow.constant(0.1, shape=[clsnum]), name="b")
            l2_loss += tensorflow.nn.l2_loss(W)
            l2_loss += tensorflow.nn.l2_loss(b)
            self.scores = tensorflow.nn.xw_plus_b(self.hdrop, W, b, name="scores")
            self.predictions = tensorflow.argmax(self.scores, 1, name="predictions")

        # Determine the loss
        with tensorflow.name_scope("loss"):
            losses = tensorflow.nn.softmax_cross_entropy_with_logits_v2(logits=self.scores, labels=self.Yin)
            self.loss = tensorflow.reduce_mean(losses) + l2rlambda * l2_loss

        # Determine the accuracy
        with tensorflow.name_scope("accuracy"):
            rightpred = tensorflow.equal(self.predictions, tensorflow.argmax(self.Yin, 1))
            self.accuracy = tensorflow.reduce_mean(tensorflow.cast(rightpred, "float"), name="accuracy")
