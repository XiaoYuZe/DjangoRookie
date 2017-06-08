import tensorflow as tf



# initialisation
X = tf.placeholder(tf.float32,[None, 28, 28, 1])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
# init = tf.initialize_all_variables()
init = tf.global_variables_initializer()


# model
Y = tf.nn.softmax(tf.matmul(tf.reshape(X,[-1,784]),W)+b)

# placeholder for correct answers
Y_ = tf.placeholder(tf.float32,[None,10])

# Loss function
cross_entropy = -tf.reduce_sum(Y_*tf.log(Y))

# % of correct answers found in batch
is_correct = tf.equal(tf.argmax(Y,1),tf.argmax(Y_,1))
accuracy = tf.reduce_mean(tf.cast(is_correct,tf.float32))

#training step
optimizer = tf.train.GradientDescentOptimizer(0.003)
train_step = optimizer.minimize(cross_entropy)

sess = tf.Session()
sess.run(init)



for i in range(1000):
	# load batch of images and correct answers
	batch_X,batch_Y = mnist.train.next_batch(100)
	train_data = {X:batch_X, Y_:batch_Y}

	# train
	sess.run(train_step, feed_dict=train_data)

	# success ? add code to print it
	a,c = sess.run([accuracy, cross_entropy], feed=train_data)

	# successs on test data ?
	test_data = {X:mnist.test.images,Y_:mnist.test.labels}
	a,c = sess.run([accuracy, cross_entropy], feed=test_data)