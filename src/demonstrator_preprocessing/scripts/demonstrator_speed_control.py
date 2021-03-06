#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import Int16

current_level = 1
count = 0
potential_level = 0
maximum_speed = rospy.get_param('/demonstrator_speed_control/maximum_speed')
def testInfoCallback(msg):
  global current_level
  global count
  global potential_level
  if msg == current_level:
    count = 0
    potential_level = 0
    
  else:
    if potential_level == 0:
      potential_level = msg
      count = 1

    else:
      if msg == potential_level:
        count = count + 1
        if count > 4:
          rospy.loginfo("Speed changed.")
          speed_level_str = str(potential_level)
          if speed_level_str == "data: 2":
            print "The speed of the robot is set to 30% of the maximum speed."
            current_level = potential_level
            count = 0
            potential_level = 0
            
          elif speed_level_str == "data: 1":
            print "The speed of the robot is set to 0."
            current_level = potential_level
            count = 0
            potential_level = 0
                        
          elif speed_level_str == "data: 3":
            print "The speed of the robot is set to 100% of the maximum speed."
            current_level = potential_level
            count = 0
            potential_level = 0
                       
          else:
            pass

        else:
          pass

      else:
        potential_level = msg
        count = 1

def speed_subscriber():
  rospy.init_node('demonstrator_speed_control')
  rospy.Subscriber("/distance_level", Int16, testInfoCallback, queue_size = 1)
  rospy.spin()

if __name__ == '__main__':
  speed_subscriber()

