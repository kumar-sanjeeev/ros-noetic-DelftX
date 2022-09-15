#!/usr/bin/env python3

# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

# Node to publish sensor information topic



from asyncio import SendfileNotAvailableError
import rospy
from hrwros_msgs.msg import SensorInformation

# rosmsg show sensor_msgs/Range 
# uint8 ULTRASOUND=0
# uint8 INFRARED=1
# std_msgs/Header header
#   uint32 seq
#   time stamp
#   string frame_id
# uint8 radiation_type
# float32 field_of_view
# float32 min_range
# float32 max_range
# float32 range


def sensorInfoPublisher():
    si_publisher = rospy.Publisher('sensor_info', SensorInformation, queue_size=10)
    rospy.init_node('sensor_info_publisher', anonymous=False)
    rate = rospy.Rate(10) # 10hz

    #create a new SensorInformation object adn fill in its contents
    sensor_info = SensorInformation()

    #fill the header information
    sensor_info.sensor_data.header.stamp = rospy.Time.now()
    sensor_info.senso_data.frame_id = 'distance_sensor_frame'

    #fill in the sensor data information
    sensor_info.sensor_data.radiation_type = sensor_info.sensor_data.ULTRASOUND
    sensor_info.sensor_data.field_of_view = 0.5  # in radians
    sensor_info.sensor_data.min_range = 0.02 # distance in meters
    sensor_info.sensor_data.max_range = 2.00 # distance in meters

    #fill in the manufacture name and part no
    sensor_info.maker_name = "michigan"
    sensor_info.part_number = 123456
    
    while not rospy.is_shutdown():
        # utility function getSensorData() provided to simulate the sensor behaviour
        sensor_info.sensor_data.range   = getSensorData(sensor_info.sensor_data.radiation_type, sensor_info.sensor_data.min_range, sensor_info.sensor_data.max_range)
        #publish the sensor information on the topic '/sensor_info'
        si_publisher.publish(sensor_info)
        #print a log message to show some acknowledgement
        rospy.loginfo("ALl went well")
        rate.sleep()


if __name__ == '__main__':
    try:
        sensorInfoPublisher()
    except rospy.ROSInterruptException:
        pass
