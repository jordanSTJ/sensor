import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)    # motors setup
GPIO.setup(17, GPIO.OUT)    
GPIO.setup(27, GPIO.OUT)   
GPIO.setup(23, GPIO.OUT)    

GPIO.setup(25, GPIO.IN)     #sensor setup

def  sensorcheck:()

    i=0                           

    while i<5:   
        sensor=GPIO.input(25)       #reads from the sensor

        if sensor==1:               
            print("there is nothing")
            sleep(0.1)             

        elif sensor==0:            
            print("there is something motors stop")
            GPIO.output(17, GPIO.LOW)   #stops wheels
            GPIO.output(27, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
        elif i=5:                   
            break                 
                
        i=i+1                
while True:

        key=input("Type in your command")
              
        if key == "w":
                GPIO.output(17, GPIO.HIGH)      # forward
                GPIO.output(24, GPIO.HIGH)
                sensorcheck()                   
                GPIO.output(17, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                
        elif key == "a":
                GPIO.output(17, GPIO.HIGH)      # left
                sensorcheck()                    
                GPIO.output(17, GPIO.LOW) 
                                                 
        elif key == "d":
                GPIO.output(24, GPIO.HIGH)      # right
                sensorcheck()                    
                GPIO.output(24, GPIO.LOW) 
                        
        elif key == "s":
                GPIO.output(27, GPIO.HIGH)      #reverse
                GPIO.output(23, GPIO.HIGH)
                sensorcheck()                    
                GPIO.output(27, GPIO.LOW)
                GPIO.output(23, GPIO.LOW)

        elif key == "z":                        #stops the code
                GPIO.cleanup()
                print("Powering down motors")
                print("Have a nice day!")
