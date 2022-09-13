from __future__ import print_function
import rospy
import actionlib

from all_msgs.msg import CounterWithDelayAction, CounterWithDelayGoal, CounterWithDelayResult


def counter_client():
    #create the simpleActionClient
    #that subscribe to topic(i.e action server) where we receive the command of preempt
    client = actionlib.SimpleActionClient('counter_with_delay', CounterWithDelayAction)

    #wait untill the action server has started up
    rospy.loginfo("Waiting for action server to come up....")
    client.wait_for_server()

    #creates a goal msg to send to action server
    goal = CounterWithDelayGoal(num_counts = 10)


    #sends to the action server for processing it
    client.send_goal(goal)
    rospy.loginfo("Goal has been sent to the action server for processing")

    #two options: either wait for the action server to finish
    #or do something else

    for i in range(0,10):
        print("I am doing other stuff while the goal is achieved by the server")
        rospy.sleep(1.5)
    
    #return the result that we got from action server that processes the input goal
    return client.get_result()  # return the result received from 


if __name__=='__main__':
    try:
        #initialize the ros node for SimpleActionClient
        rospy.init_node('counter_client')
        result = counter_client()
        rospy.loginfo(result.result_message)
    except rospy.ROSInterruptException:
        print("program interrupted before completion")

    
