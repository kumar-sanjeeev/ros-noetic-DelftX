## Node to publish the sensor information at the topic

import rospy
from all_msgs.msg import SensorInformation
from hrwros_utilities.sim_sensor_data import distSensorData


def sensorInfo():
    pub_obj = rospy.Publisher('sensor_info',SensorInformation,queue_size=10) # sensor_info is the topic name
    rospy.init_node('sensor_info_publisher',anonymous=False)                # false bcz we don't want to autogenerate the node name
    rate = rospy.Rate(1)

    #create content that need to be published at the topic
    #data type of conents should match with topic type
    ####### strcuture of custom msg data type###########

    # sensor_msgs/Range sensor_data
    # uint8 ULTRASOUND=0
    # uint8 INFRARED=1
    # std_msgs/Header header
    #     uint32 seq
    #     time stamp
    #     string frame_id
    # uint8 radiation_type
    # float32 field_of_view
    # float32 min_range
    # float32 max_range
    # float32 range
    # string manufacturer_name
    # uint32 part_number
    ######################################################
    
    data = SensorInformation()   # object of SensorInformation custom msg type

    #fill in header information
    data.sensor_data.header.stamp = rospy.Time.now()
    data.sensor_data.header.frame_id = 'distance_sensor_frame'

    #fill in sensor data information
    data.sensor_data.radiation_type = data.sensor_data.ULTRASOUND
    data.sensor_data.field_of_view = 0.5
    data.sensor_data.min_range = 0.02
    data.sensor_data.max_range = 2.00

    #fill in part no and manufacturer name
    data.manufacturer_name = 'nxp'
    data.part_number = 12232423


    #sensor information should be continously updated before publishing
    #to topic hence lets update the sensor data in loop
    while not rospy.is_shutdown():
        data.sensor_data.range = distSensorData(data.sensor_data.radiation_type, data.sensor_data.min_range, data.sensor_data.max_range)
        pub_obj.publish(data)
        #good practise to print some acknowlegment regarding publisher is running
        rospy.loginfo("Publisher started publishing on topic")
        rate.sleep()


if __name__== '__main__':
    try:
        sensorInfo()
    except rospy.ROSInternalException:
        pass
