from __future__ import print_function

import tensorflow as tf
import csv
import numpy as np
# Import MNIST data
#from tensorflow.examples.tutorials.mnist import input_data
#mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

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

mycsv = csv.reader(open("german_credit_for_mp.csv"))
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
learning_rate = 0.0001
training_epochs = 100
batch_size = 100
display_step = 10

# Network Parameters
n_hidden_1 = 2 # 1st layer number of features
n_hidden_2 = 2 # 2nd layer number of features
n_input = 20 
n_classes = 1 

# tf Graph input
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])


# Create model
def multilayer_perceptron(x, weights, biases):
    # Hidden layer with RELU activation
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
    # Hidden layer with RELU activation
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)
    # Output layer with linear activation
    out_layer = tf.matmul(layer_2, weights['out']) + biases['out']
    return out_layer

# Store layers weight & bias
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# Construct model
pred = multilayer_perceptron(x, weights, biases)

# Define loss and optimizer
cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=pred, labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# Initializing the variables
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = 1000#int(mnist.train.num_examples/batch_size)
        # Loop over all batches
        for xr in range(1000):
            #batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # Run optimization op (backprop) and cost op (to get loss value)
            feed_y = np.reshape(([col1[xr]]),(-1,1))
            feed_x = np.reshape(([col2[xr],col3[xr],col4[xr],col5[xr],col6[xr],col7[xr],col8[xr],col9[xr],col10[xr],col11[xr],col12[xr],col13[xr],col14[xr],col15[xr],col16[xr],col17[xr],col18[xr],col19[xr],col20[xr],col21[xr]]),(-1,20))
            _, c = sess.run([optimizer, cost], feed_dict={x: feed_x, y: feed_y})

            # Compute average loss
            avg_cost += c / total_batch
        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))
            print("Eval:", tf.round(tf.sigmoid(pred.eval({x: np.reshape([1,24,2,2,7721,5,2,1,2,1,2,2,30,3,2,1,3,1,2,2],(-1,20))}))))

    print("Optimization Finished!")

    # Test model
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
    # Calculate accuracy
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print("Eval:", pred.eval({x: np.reshape([4,24,2,2,3972,1,4,2,2,1,4,2,25,3,1,1,3,1,2,1],(-1,20))}))
    #32,2,46,38,7,0,0,33,0,20,53,3,0,0