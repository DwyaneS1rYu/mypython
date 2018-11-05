
import time,datetime
import telnetlib
from socket import *
import shutil
count=0
i = 0
while True:
    t1 = time.time()
    count = 0
    while count < 1:
        i = i + 1
        count = count + 1
        print i
        shutil.copyfile("/home/hadoop/Desktop/darr/data.txt", "/home/hadoop/Desktop/darr/data"+str(i)+".txt")
        time.sleep(2);
    if i==40:
        break


