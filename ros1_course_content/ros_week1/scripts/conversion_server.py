import numpy as np
import rospy

#importing the service definition, Request message  and Response message definition
from all_msgs.srv import ConversionMeterToFeet, ConversionMeterToFeetRequest, ConversionMeterToFeetResponse

cov_factor = 3.28         # conversion factor from meters to feets


def serviceCallback(req):
    '''
    This service callback function process the received service request
    ---
    Input: request msg
    ---
    Output: respose msg
    '''
    #object of the response message type
    response = ConversionMeterToFeetResponse()

    #implement sanity check
    if (req.distance_meters < 0):
        response.success = False
        response.distance_feets = -np.Inf  # Default error value
    else:
        response.success = True
        response.distance_feets = cov_factor* req.distance_meters

    #using this loop to show that ros service block program flow
    for i in range(0,10):
        rospy.sleep(1)
    
    return response

def conversion_server():
    #initialize the ros node for service server
    rospy.init_node('conversion_server', anonymous=False)

    #create a ROS service type
    service = rospy.Service('meters_to_feets', ConversionMeterToFeet,serviceCallback)

    #log message about service availability
    rospy.loginfo('Convert meters to Feets service is now available')
    rospy.spin()

if __name__ == '__main__':
    conversion_server()