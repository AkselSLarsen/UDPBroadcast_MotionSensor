BROADCAST_TO_PORT = 7161
import time
from socket import *
from datetime import datetime
from gpiozero import MotionSensor

pir = MotionSensor(4)

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    pir.wait_for_motion()
    
    data = "2: " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    pir.wait_for_no_motion()

    data += "*" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    
    print(data)
    time.sleep(1)