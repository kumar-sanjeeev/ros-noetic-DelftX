
# Assignment 1 for Week1: In this assignment you will subscribe to the topic
# that publishes sensor information. Then, you will transform the sensor
# reading from the reference frame of the sensor to compute the height of
# a box based on the illustration shown in the assignment document.
# Then, you will publish the box height on a new message type ONLY if the
# height of the box is more than 10cm.

import rospy

# Import the correct type of message
from hrwros_msgs.msg import SensorInformation


def sensor_info_callback(data):

    # Compute the height of the box from the sensor reading.
    height_box = data.sensor_data.range 

    # Do not publish information if height is more than actual available max_range of sensor
    if (height_box > 1.9):
        pass
    else:
        # will be printed
        rospy.loginfo('Height of box %0.3f' % height_box)


if __name__ == '__main__':
    # Initialize the ROS node here.
    rospy.init_node('compute_box_height', anonymous=False)

    # Wait for the topic that publishes sensor information to become available - Part1
    rospy.loginfo('Waiting for topic %s to be published...', 'sensor_info')
    rospy.wait_for_message('sensor_info', SensorInformation)
    rospy.loginfo('%s topic is now available!', 'sensor_info')

    # Create the subscriber for Part1 here
    rospy.Subscriber('sensor_info', SensorInformation, sensor_info_callback)

    # Prevent this code from exiting until Ctrl+C is pressed.
    rospy.spin()
