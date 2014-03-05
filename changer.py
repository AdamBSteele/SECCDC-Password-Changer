import os
from collections import namedtuple
print """
List all passwords, ask if you wanna change 'em
"""
os.system("chattr -i /etc/passwd")
os.system("chattr -i /etc/shadow")
lines = [line.split(':') for line in open('/etc/passwd')]
UserTuple = namedtuple('user', 'name guid info')
users = [UserTuple(line[0], line[2], line[5]) for line in lines]
 
knownBad = set(["root", "mysql", "guest", "postgres", "postfix", "apache", "exim", "pimp"])
 
 
for user in users:
        if user.guid == '0' and user.name != "root":
                print user.name + " has a guid of 0 (root)!"
        if user.name in knownBad:
                print "Changing password of user: " + user.name
                os.system("passwd " + user.name)
        else:
                print "Change password of " + user.name\
                 + "guid: " + user.guid + "? yes/[no]"
                print "User description: " + user.info
                answer = str(raw_input()) + " "
                if answer[0] == "y":
                        print "Changing password of user: " + user.name
                        os.system("passwd " + user.name)
                else:      
                        continue