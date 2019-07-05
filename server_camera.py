import socket
import time

import RPi.GPIO as GPIO
#GPIO setup

GPIO.setmode(GPIO.BCM)
# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22, 10, 9]

# loop through pins and set mode and state to 'low'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop
SleepTimeL = 1



server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
server.settimeout(0.2)
server.bind(("", 44444))
message = b"your very important message"
#while True:
server.sendto(message, ('<broadcast>', 37020))
print("1st photo taken")
time.sleep(1)


time.sleep(SleepTimeL);

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)
server.sendto(message, ('<broadcast>', 37020))
print("2nd photo taken")
time.sleep(1)
time.sleep(SleepTimeL);
GPIO.cleanup();
