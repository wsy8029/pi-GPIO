import board
import neopixel
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12,True)
pixels = neopixel.NeoPixel(board.D12, 1)    # Feather wiring!
# pixels = neopixel.NeoPixel(board.D18, 30) # Raspberry Pi wiring!


pixels[0] = (255,255,0)