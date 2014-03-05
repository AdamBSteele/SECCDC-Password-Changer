#!/usr/bin/python

import os
from collections import namedtuple

print """
See known-good users documentation for users
that we shouldn't have to worry about
"""
#Options (one at a time, please):
#	-r  - List root users
#	-s  - set passwords


os.system("chattr -i /etc/passwd")
os.system("chattr -i /etc/shadow")
lines = [line.split(':') for line in open('/etc/passwd')]
UserTuple = namedtuple('user', 'name guid info')
users = [UserTuple(line[0], line[2], line[5]) for line in lines]

knownBad = set(["root", "mysql", "guest", "postgres", "postfix", "apache", "exim"])


for user in users:
	if user.guid == '0' and user.name != "root":
		print user.name + " has a guid of 0 (root)!"
	if user.name in knownBad:
		print "Changing password of user: " + user.name
	else:
		print "Change password of " + user.name + "? yes/[no]"
		answer = str(input()) + " "
		if answer[0] == 'y':
			
		pass

#os.system("chattr +i /etc/passwd")
#os.system("chattr +i /etc/shadow")
#echo -e "new_password\nnew_password" | (passwd --stdin $USER)