import rospy
from all_msgs.srv import ConversionMeterToFeet, ConversionMeterToFeetRequest, ConversionMeterToFeetResponse


def conversion_client(x):
    #waiting for service to become available
    rospy.loginfo("Waiting for service to....")
    rospy.wait_for_service('meters_to_feets')

    try:
        #create a service proxy to call the service
        meters_to_feets = rospy.ServiceProxy('meters_to_feets', ConversionMeterToFeet)

        #call the service here
        service_response = meters_to_feets(x)

        print("printing after service has been completed by the server")

        #return the response to the calling function
        return service_response
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    
if __name__ == '__main__':

    #initialize the ros client node
    rospy.init_node("conversion_client", anonymous=False)

    #distance to be converted in feets
    x_meters = 0.25

    rospy.loginfo("Requesting conversion of %f m into feets"% (x_meters))

    #call the service client function
    service_response = conversion_client(x_meters)

    #process the service response
    if(not service_response.success):
        rospy.logerr("Conversion Unsuccessful! Distance should be positive real number")
    else:
        rospy.loginfo("%f(m) = %f(feet)"%(x_meters, service_response.distance_feets))
        rospy.loginfo("Conversion Successful")


