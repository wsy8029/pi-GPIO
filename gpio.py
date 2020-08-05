import board
import neopixel
import RPi.GPIO as GPIO
import time

# Set GPIO Pin mode
GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)

# define BCM Pin number of each component
GPIO.setup(12, GPIO.OUT) # LED
GPIO.output(12,True)
GPIO.setup(6, GPIO.IN) # Button
GPIO.setup(13, GPIO.OUT) # Fan
#GPIO.input(6,True)

# define neopixel object
pixels = neopixel.NeoPixel(board.D12, 1) # 1: number of Neopixels
pixels[0] = (255,255,0) # Initialize Neopixel color (not essential)


# fade in function for test
def fadein():
    for i in range(255):
        pixels[0] = (i,255-i,0)
        time.sleep(0.01)
        i += 0
# fan test for control fan speed
def fan_test():
    for i in range(0,100):
        print("100HZ, duty bee = 20%")
        GPIO.output(13, True)
        time.sleep(0.002)


        GPIO.output(13, False)
        time.sleep(0.008)

    for i in range(0,100):
        print("100HZ, duty bee = 50%")
        GPIO.output(13, True)
        time.sleep(0.005)


        GPIO.output(13, False)
        time.sleep(0.005)


    for i in range(0,100):
        print("100HZ, duty bee = 80%")
        GPIO.output(13, True)
        time.sleep(0.008)


        GPIO.output(13, False)
        time.sleep(0.002)


    for i in range(0,100):
        print("100HZ, duty bee = 100%")
        GPIO.output(13, True)
        time.sleep(0.01)
            
while True:
        inputIO = GPIO.input(6)

        if inputIO == False:
            pixels[0] = (255,0,0)
            fan_test()
#             fadein()
            print("False")
            #time.sleep(1)

        else:
            pixels[0] = (0,0,255)
            print("True")
            #time.sleep(1)


