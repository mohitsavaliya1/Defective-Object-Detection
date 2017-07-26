import time
import RPi.GPIO as GPIO
import subprocess
import os

TRIG = 21 # Pin for ultrasonic sensor
ECHO = 22 # Pin for ultrasonic sensor
LED = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT) #setup
GPIO.setup(23,GPIO.OUT) #setup
GPIO.setup(TRIG,GPIO.OUT) #setup
GPIO.setup(ECHO,​GPIO.IN​) #setup

def main(): # function

start_motor() # motor will start
img="click.jpg" # captured image through webcam
temp_img="template.jpg" # sample template image
while True:
x=read_from_sensor() #continuously sence by sensor
if x!=-1: #if detected
time.sleep(0.4)
stop_motor() #then motor stop
os.system('fswebcam '+str(img)) # command for capturing image
os.system('python im.py '+str(img)+' '+str(temp_img)+'>diff.txt') #compare 2 images
output=open('diff.txt').read().strip()
print output
x=float(output)
print x
print "output is" +str(x)
if x>45: # threshold
blink_led()
start_motor()
time.sleep(1.5)

def blink_led(): #code for LED blink
GPIO.output(LED,True)
time.sleep(3)
GPIO.output(LED,False)
time.sleep(3)

def start_motor(): # code for motor starting
GPIO.output(23,True)

def read_from_sensor(): # read sensor input data
print "Waiting For Sensor To Settle"
pulse_start = 0
GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False)
while GPIO.input(ECHO)==0:
pulse_start = time.time()
while GPIO.input(ECHO)==1:
pulse_end = time.time()
pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance,2)
if distance < 13 :
return 1
else:
return -1

def stop_motor():
GPIO.output(23,False)

if __name__ == "__main__":
main()
