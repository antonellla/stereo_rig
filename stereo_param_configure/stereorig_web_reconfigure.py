<<<<<<< HEAD
#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def callback(data):
=======
import rospy
from std_msgs.msg import Float64

def callback(data)
>>>>>>> 69c03c97b1156738716b16969e2ab8d7b594c7e4
    rospy.loginfo(rospy.get_caller_id()+ "I got %d", data.data);

def listener():
    rospy.init_node('stereorig_web_reconfigure', anonymous=True)
<<<<<<< HEAD
    rospy.loginfo('Stereo Rig Web Reconfigure up and running')
=======
>>>>>>> 69c03c97b1156738716b16969e2ab8d7b594c7e4

    rospy.Subscriber('exposure',Float64, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    listener()

