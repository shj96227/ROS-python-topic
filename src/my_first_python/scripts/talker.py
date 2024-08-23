#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String

def talker():
     pub = rospy.Publisher('chatter',String,queue_size=10) 
    ##############################
    ##  Publisher name = pub    ##
    ##  Topic name = chatter    ##
    ##  Type = String           ##
    ##  queue_size = 10         ##
    ##############################
     rospy.init_node('talker', anonymous = True)
     rate = rospy.Rate(10) #10hz      
     while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()     #rospy.get_time() 메소드로 현재 시간 정보를 출력
        rospy.loginfo(hello_str)                            #rospy.loginfo() 메소드로 str 메시지를 화면에 출력
        pub.publish(hello_str)
        rate.sleep()
        
if __name__=='__main__': 
    try: 
        talker() 
    except rospy.ROSInterruptException: 
        pass

