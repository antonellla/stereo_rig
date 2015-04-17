import rospy
from std_msgs.msg import Float64

def callback(data)
    rospy.loginfo(rospy.get_caller_id()+ "I got %d", data.data);

def listener():
    rospy.init_node('stereorig_web_reconfigure', anonymous=True)

    rospy.Subscriber('exposure',Float64, queue_size=10)

    rospy.spin()

if __name__ == '__main__':
    listener()

