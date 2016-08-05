
import time
import Adafruit_BBIO.GPIO as GPIO

#in cm
threshold = 180

# Define GPIO to use on Pi
GPIO_TRIGGER = 'P9_11'
GPIO_ECHO = 'P9_12'

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)   # Echo


while True
	# Set trigger to False (Low)
	GPIO.output(GPIO_TRIGGER, GPIO.LOW)

	# Allow module to settle
	time.sleep(0.5)

	# Send 10us pulse to trigger
	GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, GPIO.LOW)
	start = time.time()
	print GPIO.input(GPIO_ECHO)
	while GPIO.input(GPIO_ECHO)==0:
 		start = time.time()

	print GPIO.input(GPIO_ECHO)
	while GPIO.input(GPIO_ECHO)==1:
 		stop = time.time()

	print start
	print stop
	# Calculate pulse length
	elapsed = stop-start

	# Distance pulse travelled in that time is time
	# multiplied by the speed of sound (cm/s)
	distance = elapsed * 34000

	# That was the distance there and back so halve the value
	distance = distance / 2

	print "Distance : %.1f" % distance

	if distance<threshold:
		break

	# Reset GPIO settings
	GPIO.cleanup()

