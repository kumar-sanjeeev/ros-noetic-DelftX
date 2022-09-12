#Node subscribe to the topic to receive the sensor information


import rospy
from all_msgs.msg import SensorInformation

def sensorCallback(data):
    rospy.loginfo("Distance reading from the sensor is: [%f] ", data.sensor_data.range)

def sensorSubscriber():
    #initialize the ros subscriber node
    rospy.init_node('sensor_info_subscriber',anonymous=False)
    #hooke the initialized subscriber node to the top level callback function
    rospy.Subscriber('sensor_info',SensorInformation,sensorCallback)

    rospy.spin() # keep the python from exiting until this node is stopped

if __name__ == '__main__':
    sensorSubscriber()

