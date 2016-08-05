import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_15", GPIO.IN)
while True:
	if GPIO.input("P9_15"):
    		print("HIGH")
		time.sleep(1)
		break
#	else:
#    		print("LOW")
#		time.sleep(1)
