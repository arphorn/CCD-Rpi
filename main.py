import RPi.GPIO as GPIO
import time
import cv2

def init():
 
            
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(true_lamp ,GPIO.OUT)
    GPIO.setup(ready_lamp ,GPIO.OUT)
    GPIO.setup(flase_lamp,GPIO.OUT)
    GPIO.setup(sw_start,GPIO.IN)
    GPIO.output(true_lamp,GPIO.LOW)
    GPIO.output(flase_lamp,GPIO.LOW)

    
    



Threshold = 0.78
true_lamp = 19
flase_lamp = 11
ready_lamp = 13

sw_start = 6
init()

time.sleep(2)


try:

    
    
    while(1):
        status_work = GPIO.input(sw_start)
        if(status_work != 1):
                    
                    GPIO.output(ready_lamp,GPIO.LOW)
                    import Camera
                    import Correlation

                    time.sleep(2)
                    Camera.getImages()
                    result = Correlation.Corre()
                    print(result)

                    if(  result >= Threshold ):
                        print("normally")
                        
                        GPIO.output(true_lamp,GPIO.HIGH)
                        #GPIO.output(flase_lamp,GPIO.LOW)
                        
                    else:
                        print("Moldy")
                        time.sleep(5)
                        
                        #GPIO.output(true_lamp,GPIO.LOW)
                        GPIO.output(flase_lamp,GPIO.HIGH)


                    time.sleep(10)
                    GPIO.output(true_lamp,GPIO.LOW)
                    GPIO.output(flase_lamp,GPIO.LOW)
                    #cv2.destroyAllWindows()
                    time.sleep(10)
        else:
            print( 'READY !')
            GPIO.output(ready_lamp,GPIO.HIGH)
            
            
except:
    GPIO.output(ready_lamp,GPIO.LOW)
    print("Please restart device !!!")


          
