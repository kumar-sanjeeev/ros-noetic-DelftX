import rospy
import actionlib

from all_msgs.msg import CounterWithDelayAction, CounterWithDelayFeedback, CounterWithDelayResult

class Counter(object):
    #create variable to hold feedback and result action msgs
    _feedback = CounterWithDelayFeedback()
    _result = CounterWithDelayResult()

    def __init__(self, name) -> None:
        #name of the action server that clients will use to connect with it
        self._action_name = name

        #create a action server 
        self._as = actionlib.SimpleActionServer(self._action_name, CounterWithDelayAction, execute_cb=self.action_callback, auto_start=False)

        #start the action server
        self._as.start()
        rospy.loginfo("Action Server Started and available for taking request from clients")
    
    def action_callback(self, goal_from_client):
        delay_value = 1
        #set the delay rate
        rospy.Rate(delay_value)
        #variable to decide the success of action server for completing the goal
        success = True
        self._feedback.counts_completed = 0

        #start executing action

        for i in range(0, goal_from_client.num_counts):
            #check if the preempt has been requested or not by some action clients
            rospy.loginfo("%s: Preempted" % self._action_name)
            self._as.set_preempted()
            success = False
            break

        #publish the feedback
        self._result.result_message = "Successfully completed counting"
        rospy.loginfo("%s :Succeeded" % self._action_name)
        self._as.set_succeeded(self._result)
    
if __name__ == '__main__':

    #initialize the ros node for this action server
    rospy.init_node('counter_with_delay')

    #create an instance of the action server here
    server = Counter(rospy.get_name())
    rospy.spin()


