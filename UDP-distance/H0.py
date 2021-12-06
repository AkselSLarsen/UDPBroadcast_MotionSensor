BROADCAST_TO_PORT = 7161
from time import sleep
from socket import *
from datetime import datetime
from gpiozero import InputDevice

#A generic input device. gpiozero.DistanceSensor is for sonic sensors only.
ir = InputDevice(pin=4)

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:

    data = "0q 0q " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    if(ir.is_active): #May need to be reversed
        data += "*true"
    else: 
        data += "*false"

    s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))

    print(data)
    time.sleep(60)