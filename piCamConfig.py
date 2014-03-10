#!/usr/bin/env python
###############################
# 
# Pi in the Sky Cam Config 
#            v0.01
#
# Configuration manager
# for the raspberry Pi
# Camera controller module
#
# Ryan Waters
# Esma Susuz
# Justine Villar
#
##############################

#Imports
import sys

camConfig = {}
stillConfig = {}
vidConfig = {}

def readConfig():
	with open("piCamConfig.conf") as f:
		for line in f:
			if line.startswith(('c')):
				(key, val) = line.split()
				camConfig[key] = val
			elif line.startswith(('i')):
				(key, val) = line.split()
				stillConfig[key] = val
			elif line.startswith(('v')):
				(key, val) = line.split()
				vidConfig[key] = val

def mainMenu():
	print "################################"
	print "# 1) Camera Configuration"
	print "# 2) Still Configuration"
	print "# 3) Video Configuration"
	print "# 0) Exit Application"
	print "################################"
	selection = input("Selection: ")

	if selection < 0 or selection > 3:
		print "Invalid selection..."
		mainMenu()
	elif selection == 1:
		camConfig()
	elif selection == 2:
		stillConfig()
	elif selection == 3:
		vidConfig()
	else:
		sys.exit(0)

###############################
# Configure settings for 
# general camera
# such as ISO, exposure, etc.
###############################
def camConfig():
	print "Cam Config"
	
	
	
		
###############################
# Configure Still specific
# options for the PiCam
###############################
def stillConfig():
	print "Still Config"

###############################
# Configure Video Specific 
# options for the piCam
###############################
def vidConfig():
	print "Vid Config"

# Begin execution of program
readConfig()
mainMenu()
