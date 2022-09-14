#Libraries
import RPi.GPIO as GPIO
import time


#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO direction (IN / OUT)
GPIO.setup(gpio_trigger, GPIO.OUT)
GPIO.setup(gpio_echo, GPIO.IN)


def distance():
    # set Trigger to HIGH
    GPIO.output(gpio_trigger, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(gpio_trigger, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(gpio_echo) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(gpio_echo) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
