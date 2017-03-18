import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Recurrent,Embedding,LSTM
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from keras import optimizers
import keras

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# load dataset
#dataset_test = numpy.genfromtxt ('../r-calculations/k-means/output16_test.csv', delimiter=",")
#X_test = dataset_test[:,0:2].astype(float)
#Y_test = dataset_test[:,2]

dataset = numpy.genfromtxt ('../r-calculations/k-means/output16_2dim.csv', delimiter=",")
X = dataset[:,0:2].astype(float)
Y = dataset[:,2]
print(Y[0])
#Y = np_utils.to_categorical(Y)

# create model
model = Sequential()
model.add(Dense(2, input_dim=2, init='normal', activation='relu'))
#model.add(Dropout(0.20))
#model.add(Dense(2, activation='relu'))
model.add(Dense(13, init='normal', activation='sigmoid'))
# Compile model
#model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

sgd = optimizers.Nadam(lr=0.002, beta_1=0.9, beta_2=0.999, epsilon=1e-08, schedule_decay=0.004)

model.compile(loss='sparse_categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

model.fit(X,Y, epochs=20, batch_size=5)
#print( model.predict(numpy.array([2,36,2,5,2384,1,2,4,3,1,1,4,33,3,1,1,2,1,1,1]).reshape((1,20))) )
#print( model.predict(numpy.array(X[0]).reshape((1,4))) )
#print( model.predict(numpy.array(X[1]).reshape((1,4))) )
#print( model.predict(numpy.array(X[2]).reshape((1,4))) )

for x in xrange(1,10):
	result = model.predict_classes(numpy.array(X[x]).reshape((1,2)))
	print(result)

#score, acc = model.evaluate(X_test, Y_test,
#                            batch_size=1)
#print('Test score:', score)
#print('Test accuracy:', acc)