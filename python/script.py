import webiopi
import datetime
import time
import os

GPIO = webiopi.GPIO

#Define the ports
Led_blue = 21 
Led_red = 17
Buzzer = 22
Sonar = 14
MotorA_dir = 7 #Rightside
MotorA_speed = 8 #Rightside
MotorB_dir = 9 #LeftSide
MotorB_speed = 10 #LeftSide

def setup():
	GPIO.setFunction(Led_red, GPIO.OUT)
	GPIO.setFunction(Led_blue, GPIO.OUT)
	GPIO.setFunction(Buzzer, GPIO.OUT)
	GPIO.setFunction(MotorB_speed, GPIO.OUT)
	GPIO.setFunction(MotorB_dir, GPIO.OUT)
	GPIO.setFunction(MotorA_speed, GPIO.OUT)
	GPIO.setFunction(MotorA_dir, GPIO.OUT)


#Functions Driving
@webiopi.macro
def Stop():
	GPIO.digitalWrite(MotorA_speed, GPIO.LOW)
	GPIO.digitalWrite(MotorA_dir, GPIO.LOW)
	GPIO.digitalWrite(MotorB_speed, GPIO.LOW)
	GPIO.digitalWrite(MotorB_dir, GPIO.LOW)
    
@webiopi.macro
def Forward():
    # switch MotorA on forwards
    GPIO.digitalWrite(MotorA_speed, GPIO.HIGH)
    GPIO.digitalWrite(MotorA_dir, GPIO.LOW)
    # switch MotorB on forwards
    GPIO.digitalWrite(MotorB_speed, GPIO.HIGH)
    GPIO.digitalWrite(MotorB_dir, GPIO.LOW)

@webiopi.macro   
def Forward_right():
    # switch MotorA on backwards
    GPIO.digitalWrite(MotorA_speed, GPIO.LOW)
    GPIO.digitalWrite(MotorA_dir, GPIO.HIGH)
    # switch MotorB on forwards
    GPIO.digitalWrite(MotorB_speed, GPIO.HIGH)
    GPIO.digitalWrite(MotorB_dir, GPIO.LOW)
    
@webiopi.macro
def Forward_left():
    # switch MotorA on forwards
    GPIO.digitalWrite(MotorA_speed, GPIO.HIGH)
    GPIO.digitalWrite(MotorA_dir, GPIO.LOW)
    # switch MotorB on backwards
    GPIO.digitalWrite(MotorB_speed, GPIO.LOW)
    GPIO.digitalWrite(MotorB_dir, GPIO.HIGH)

@webiopi.macro
def Backwards():
    # switch MotorA on backwards
    GPIO.digitalWrite(MotorA_speed, GPIO.LOW)
    GPIO.digitalWrite(MotorA_dir, GPIO.HIGH)
    # switch MotorB on backwards
    GPIO.digitalWrite(MotorB_speed, GPIO.LOW)
    GPIO.digitalWrite(MotorB_dir, GPIO.HIGH)    
    
@webiopi.macro
def Backwards_right():
    # switch MotorA on forwards
    GPIO.digitalWrite(MotorA_speed, GPIO.HIGH)
    GPIO.digitalWrite(MotorA_dir, GPIO.LOW)
    # switch MotorB on backwards
    GPIO.digitalWrite(MotorB_speed, GPIO.LOW)
    GPIO.digitalWrite(MotorB_dir, GPIO.HIGH)
    
@webiopi.macro
def Backwards_left():
    # switch MotorA on backwards
    GPIO.digitalWrite(MotorA_speed, GPIO.LOW)
    GPIO.digitalWrite(MotorA_dir, GPIO.HIGH)
    # switch MotorB on forwards
    GPIO.digitalWrite(MotorB_speed, GPIO.HIGH)
    GPIO.digitalWrite(MotorB_dir, GPIO.LOW)

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
    GPIO.digitalWrite(Led_blue,GPIO.HIGH)

@webiopi.macro
def LedBlue_off():
    GPIO.digitalWrite(Led_blue,GPIO.LOW)

@webiopi.macro
def LedRed_on():
    GPIO.digitalWrite(Led_red,GPIO.HIGH)

@webiopi.macro
def LedRed_off():
    GPIO.digitalWrite(Led_red,GPIO.LOW)

@webiopi.macro
def Buzzer_on():
    GPIO.digitalWrite(Buzzer,GPIO.HIGH)

@webiopi.macro
def Buzzer_off():
    GPIO.digitalWrite(Buzzer,GPIO.LOW)
   
#When webIoPi shutsdown   

def destroy():
    GPIO.digitalWrite(Buzzer,GPIO.LOW)
    GPIO.digitalWrite(Led_red,GPIO.LOW)
    GPIO.digitalWrite(Led_blue,GPIO.LOW)
    GPIO.digitalWrite(MotorA_speed,GPIO.LOW)
    GPIO.digitalWrite(MotorA_dir,GPIO.LOW)
    GPIO.digitalWrite(MotorB_speed,GPIO.LOW)
    GPIO.digitalWrite(MotorB_dir,GPIO.LOW)
    GPIO.cleanup()
