#!/usr/bin/env python
import rospy
import math
import time
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point
from math import atan2,pow,sqrt
pi = 3.141
x = 0
y = 0
z = 0
yaw = 0

def move(speed, distance, is_forward):
 
    velocity_publisher = rospy.Publisher('/Diff_Drive/diff_drive_controller/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist() 

    if is_forward:
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    vel_msg.linear.y = 0

    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    distance_moved = 0.0
    loop_rate = rospy.Rate(10)
    while not rospy.is_shutdown():


        ta0 = float(rospy.Time.now().to_sec())
        current_distance = 0


        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
	    loop_rate.sleep()
            #Takes actual time to velocity calculus
            ta1=float(rospy.Time.now().to_sec())
            #Calculates distancePoseStamped
            current_distance= speed*(ta1-ta0)

	grip.data=ext
	pub1.publish(grip)
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)
    
 
x = 0.0
y = 0.0 
theta = 0.0

def newOdom(msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
   


sub = rospy.Subscriber("/Diff_Drive/diff_drive_controller/odom", Odometry, newOdom)
velocity_pub = rospy.Publisher("/Diff_Drive/diff_drive_controller/cmd_vel", Twist, queue_size = 1)

speed = Twist()




goal = Point()

def move2goal(k,l):
	goal.x = k
	goal.y = l
        distance_tolerance = 0.01
        vel_msg = Twist()


        while sqrt(pow((goal.x - x), 2) + pow((goal.y - y), 2)) >= distance_tolerance:

 
            #linear velocity in the x-axis:
            vel_msg.linear.x = 1.5 * sqrt(pow((goal.x - x), 2) + pow((goal.y - y), 2))
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 4 * (atan2(goal.y - y, goal.x - x) - theta)

            velocity_publisher.publish(vel_msg)
          
        #Stopping our robot 
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        velocity_pub.publish(vel_msg)

        rospy.spin()


ext = [0.08,0.5,0.5]
con = [0,0,0]

if __name__ == '__main__':
    try:
        rospy.init_node('task_pub', anonymous=True)
	grip=Float64MultiArray()
        cmd_vel_topic = '/Diff_Drive/diff_drive_controller/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
	pub1=rospy.Publisher('/r2d2_gripper_controller/command',Float64MultiArray,queue_size=5)
	
        time.sleep(2)
        move(1.0, 5.0,1)
        time.sleep(2)
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo('node_terminated')
