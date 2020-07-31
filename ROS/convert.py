#! /usr/bin/env python
import rospy
import tf
from beginner_tutorials.msg import quaternion
from beginner_tutorials.msg import euler
q=quaternion()
q.x=2 #taking some random values to be converted
q.y=2
q.z=2
q.w=2

def callback(msg):
	a=euler()
	a.roll,a.pitch,a.yaw=tf.transformations.euler_from_quaternion([msg.x,msg.y,msg.z,msg.w])
	rospy.loginfo(a)

rospy.init_node("converted")
r=rospy.Rate(1)
p1=rospy.Publisher('topic2',euler,queue_size=10)
p2=rospy.Publisher('topic1',quaternion,queue_size=10)
s=rospy.Subscriber('t',q,callback)
while not rospy.is_shutdown():
	p2.publish(a)
	 #publishing only the converted values
	r.sleep()
