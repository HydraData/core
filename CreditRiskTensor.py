from __future__ import print_function

# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
#mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
import csv
import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
rng = numpy.random
#INPUT
filename_queue = tf.train.string_input_producer(["cs.csv"])

reader = tf.TextLineReader()
key, value = reader.read(filename_queue)

# Default values, in case of empty columns. Also specifies the type of the
# decoded result.
#record_defaults = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
#col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14 = tf.decode_csv(
#    value, record_defaults=record_defaults)
#features = tf.stack([col2,col3,col4,col5,col6,col7,col9,col10,col11,col12,col13,col14])

#INPUT
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []
col9 = []
col10 = []
col11 = []
col12 = []
col13 = []
col14 = []
col15 = []
col16 = []
col17 = []
col18 = []
col19 = []
col20 = []
col21 = []
col0 = []

mycsv = csv.reader(open("german_credit.csv"))
for row in mycsv:
    col1.append(row[0])
    col2.append(row[1])
    col3.append(row[2])
    col4.append(row[3])
    col5.append(row[4])
    col6.append(row[5])
    col7.append(row[6])
    col8.append(row[7])
    col9.append(row[8])
    col10.append(row[9])
    col11.append(row[10])
    col12.append(row[11])
    col13.append(row[12])
    col14.append(row[13])
    col15.append(row[14])
    col16.append(row[15])
    col17.append(row[16])
    col18.append(row[17])
    col19.append(row[18])
    col20.append(row[19])
    col21.append(row[20])
    col0.append(0)

#INPUT

# Parameters
learning_rate = 0.00001
training_epochs = 200
display_step = 10

# Training Data
train_X = numpy.asarray([col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20])
train_Y = numpy.asarray([col1])
n_samples = 999#train_X.shape[0] #Samples in a set

# tf Graph Input
X = tf.placeholder("float",shape=20)
Y = tf.placeholder("float",shape=1)

# Set model weights
W = tf.Variable(rng.randn(), name="weight")
b = tf.Variable(rng.randn(), name="bias")

# Construct a linear model
pred = tf.add(tf.mul(X, W), b)

# Mean squared error
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)
# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initializing the variables
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        #for (x, y) in zip(train_X, train_Y):
        #    sess.run(optimizer, feed_dict={X: x, Y: y})
        for xr in xrange(1,n_samples):
          sess.run(optimizer, feed_dict={X: [col2[xr],col3[xr],col4[xr],col5[xr],col6[xr],col7[xr],col8[xr],col9[xr],col10[xr],col11[xr],col12[xr],col13[xr],col14[xr],col15[xr],col16[xr],col17[xr],col18[xr],col19[xr],col20[xr],col21[xr]], Y:[col1[xr]]})
        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            for xr in xrange(1,n_samples):
              c = sess.run(cost, {X: [col2[xr],col3[xr],col4[xr],col5[xr],col6[xr],col7[xr],col8[xr],col9[xr],col10[xr],col11[xr],col12[xr],col13[xr],col14[xr],col15[xr],col16[xr],col17[xr],col18[xr],col19[xr],col20[xr],col21[xr]], Y:[col1[xr]]})
            #c = sess.run(cost, feed_dict={X: train_X, Y:train_Y})
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \
                "W=", sess.run(W), "b=", sess.run(b))

    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: [col2[xr],col3[xr],col4[xr],col5[xr],col6[xr],col7[xr],col8[xr],col9[xr],col10[xr],col11[xr],col12[xr],col13[xr],col14[xr],col15[xr],col16[xr],col17[xr],col18[xr],col19[xr],col20[xr],col21[xr]], Y:[col1[xr]]})
    print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')

    print(pred.eval(feed_dict={X: [1,18,2,0,1216,1,2,4,2,1,3,3,23,3,1,1,3,1,2,1]}))