#!/usr/bin/env python 
# -*- coding: utf-8 -*-
 
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    """
    메시지가 hello_pub 토픽에 도착하면 실행되는 콜백 함수다.
    data 변수에는 토픽에서 얻은 메시지가 들어가며, 이를 rospy.loginfo()를 사용해 출력할 수 있다.
    """

def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber("chatter", String, callback)
    """
    메시지의 데이터 타입은 String이며, 
    메시지가 이 토픽에 도착할 경우 callback이라고 불리는 메소드가 호출된다.
    """
    rospy.spin()
    """
    rospy.spin() 메소드를 사용해 노드가 셧다운될 때까지 노드가 끝나지 않도록 만든다.
    """

if __name__=='__main__':
    listener()
