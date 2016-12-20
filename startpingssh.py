import sys
import time
import threading
from subprocess import call

command = call("python pingtool.py", shell = True)
forlooplist = open('ipname.txt', 'r')
mylist = forlooplist.read()
splitlist = mylist.split(', ')


for ips in splitlist:
    command = call("python sshtry.py "+ ips +" pass.txt", shell = True)
    t = threading.Thread(target = command)
    t.start()
    time.sleep(.3)
