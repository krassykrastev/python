import os
import time

def dskt_locker():
    time.sleep(5)
    winpath = os.environ['windir']
    os.system(winpath + r'\system32\rundll32 user32.dll, LockWorkStation')

while(1):
    dskt_locker()
