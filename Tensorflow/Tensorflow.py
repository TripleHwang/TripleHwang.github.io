import tensorflow as tf 															#tensorflow 객체를 tf라는 이름으로 가져옵니다.
from tensorflow.examples.tutorials.mnist import input_data   						#input_data를 가져옴

# Dataset loading
mnist = input_data.read_data_sets("./samples/MNIST_data/", one_hot=True)		   	#데이터 불러오기

# Set up model		
x = tf.placeholder(tf.float32, [None, 784])											#28*28 행렬
W = tf.Variable(tf.zeros([784, 10]))												#variable 초기값 초기화
b = tf.Variable(tf.zeros([10]))														#variable 초기값 초기화
y = tf.nn.softmax(tf.matmul(x, W) + b)												#model 구현

y_ = tf.placeholder(tf.float32, [None, 10])											#교차 엔트로피 구현을 위한 placeholder 선언

cross_entropy = -tf.reduce_sum(y_*tf.log(y))										#교차 엔트로피 구현
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)		#최적화 알고리즘 적용(경사 하강법 사용)

# Session
init = tf.initialize_all_variables()												#만든 변수들을 초기화

sess = tf.Session()																	#모델을 시작한다
sess.run(init)																		#초기화 작업 실행															

# Learning
for i in range(1000):																#학습을 1000번 반복한다
  batch_xs, batch_ys = mnist.train.next_batch(100)									#100개의 데이터들의 batch들을 가져온다.
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})						#plcaseholders를 대체하기 위한 일괄 처리 데이터에 train_step을 실행함.

# Validation
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))						#예측과 실제가 일치하는지 확인
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))					#적중률을 행렬값으로 내줌(평균값)

# Result should be approximately 91%.
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))  #테스트데이터를 대상으로 정확도 확인