import webiopi
import datetime
import time
import os
import RPi.GPIO as GPIO

#Define the ports
Led_blue = 21 
Led_red = 17
Buzzer = 22
Sonar = 14
MotorA_dir = 7 #Rightside
MotorA_speed = 8 #Rightside
MotorB_dir = 9 #LeftSide
MotorB_speed = 10 #LeftSide

#Set the servo port
GPIO.setmode(GPIO.BCM) # Use Gpio pin numbering
#Set ports OUT
GPIO.setup(Led_red,GPIO.OUT) 
GPIO.setup(Led_blue,GPIO.OUT)
GPIO.setup(Buzzer,GPIO.OUT)
GPIO.setup(MotorB_speed, GPIO.OUT)
GPIO.setup(MotorB_dir, GPIO.OUT)
GPIO.setup(MotorA_speed, GPIO.OUT)
GPIO.setup(MotorA_dir, GPIO.OUT)


#Functions Driving
@webiopi.macro
def Stop():
    GPIO.output (MotorA_speed,GPIO.LOW)
    GPIO.output (MotorA_dir,GPIO.LOW)
    GPIO.output (MotorB_speed,GPIO.LOW)
    GPIO.output (MotorB_dir,GPIO.LOW)
    
@webiopi.macro
def Forward():
    # switch MotorA on forwards
    GPIO.output (MotorA_speed, 1)
    GPIO.output (MotorA_dir, 0)
    # switch MotorB on forwards
    GPIO.output (MotorB_speed, 1)
    GPIO.output (MotorB_dir, 0)

@webiopi.macro   
def Forward_right():
    # switch MotorA on backwards
    GPIO.output (MotorA_speed, 0)
    GPIO.output (MotorA_dir, 1)
    # switch MotorB on forwards
    GPIO.output (MotorB_speed, 1)
    GPIO.output (MotorB_dir, 0)
    
@webiopi.macro
def Forward_left():
    # switch MotorA on forwards
    GPIO.output (MotorA_speed, 1)
    GPIO.output (MotorA_dir, 0)
    # switch MotorB on backwards
    GPIO.output (MotorB_speed, 0)
    GPIO.output (MotorB_dir, 1)

@webiopi.macro
def Backwards():
    # switch MotorA on backwards
    GPIO.output (MotorA_speed, 0)
    GPIO.output (MotorA_dir, 1)
    # switch MotorB on backwards
    GPIO.output (MotorB_speed, 0)
    GPIO.output (MotorB_dir, 1)    
    
@webiopi.macro
def Backwards_right():
    # switch MotorA on forwards
    GPIO.output (MotorA_speed, 1)
    GPIO.output (MotorA_dir, 0)
    # switch MotorB on backwards
    GPIO.output (MotorB_speed, 0)
    GPIO.output (MotorB_dir, 1)
    
@webiopi.macro
def Backwards_left():
    # switch MotorA on backwards
    GPIO.output (MotorA_speed, 0)
    GPIO.output (MotorA_dir, 1)
    # switch MotorB on forwards
    GPIO.output (MotorB_speed, 1)
    GPIO.output (MotorB_dir, 0)

	#Function Pan and Tilt
@webiopi.macro
def pan_left():
    cmd = 'sudo echo 7=+10 > /dev/servoblaster'
    os.system(cmd)

@webiopi.macro
def pan_right():
    cmd = 'echo 7=-10 > /dev/servoblaster'
    os.system(cmd)

@webiopi.macro
def pan_neutral():
    cmd = 'echo 7=150 > /dev/servoblaster'
    os.system(cmd)

@webiopi.macro	
def tilt_up():
    cmd = 'echo 6=-10 > /dev/servoblaster'
    os.system(cmd)

@webiopi.macro	
def tilt_down():
    cmd = 'echo 6=+10 > /dev/servoblaster'
    os.system(cmd)

@webiopi.macro	
def tilt_neutral():
    cmd = 'echo 6=150 > /dev/servoblaster'
    os.system(cmd)

@webiopi.macro	
def reboot():
    cmd = 'sudo reboot'
    os.system(cmd)

@webiopi.macro	
def shutdown():
    cmd = 'sudo shutdown -h now'
    os.system(cmd)

#Function LEDS and Buzzer
@webiopi.macro
def LedBlue_on():
    GPIO.output(Led_blue,GPIO.HIGH)

@webiopi.macro
def LedBlue_off():
    GPIO.output(Led_blue,GPIO.LOW)

@webiopi.macro
def LedRed_on():
    GPIO.output(Led_red,GPIO.HIGH)

@webiopi.macro
def LedRed_off():
    GPIO.output(Led_red,GPIO.LOW)

@webiopi.macro
def Buzzer_on():
    GPIO.output(Buzzer,GPIO.HIGH)

@webiopi.macro
def Buzzer_off():
    GPIO.output(Buzzer,GPIO.LOW)
   
#Emergency function to stop all output   
@webiopi.macro
def Emergency():
    GPIO.output(Buzzer,GPIO.LOW)
    GPIO.output(Led_red,GPIO.LOW)
    GPIO.output(Led_blue,GPIO.LOW)
    GPIO.output (MotorA_speed,GPIO.LOW)
    GPIO.output (MotorA_dir,GPIO.LOW)
    GPIO.output (MotorB_speed,GPIO.LOW)
    GPIO.output (MotorB_dir,GPIO.LOW)
    GPIO.cleanup()