import board
import neopixel
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12,True)
GPIO.setup(6, GPIO.IN)
#GPIO.input(6,True)

pixels = neopixel.NeoPixel(board.D12, 1)    # Feather wiring!
# pixels = neopixel.NeoPixel(board.D18, 30) # Raspberry Pi wiring!
pixels[0] = (255,255,0)
while True:
        inputIO = GPIO.input(6)

        if inputIO == False:
            pixels[0] = (255,0,0)
            print("False")
            #time.sleep(1)

        else:
            pixels[0] = (0,0,255)
            print("True")
            #time.sleep(1)
