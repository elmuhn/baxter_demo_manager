#!/usr/bin/env python

import rospy
from bondpy import bondpy


def main():
	rospy.init_node('child_node_a')
	bond = bondpy.Bond("bond_topic", "m2a")
	bond.start()
	print "Child A has just joined!"
	rospy.sleep(2)
	print "A after sleep..."
	rospy.spin()

if __name__ == "__main__":
	main()