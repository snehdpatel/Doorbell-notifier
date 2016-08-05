import Adafruit_BBIO.GPIO as GPIO
import time

echo_pin = 'P8_7'
trig_pin = 'P8_8'

while True:
	GPIO.setup(trig_pin, GPIO.OUT)
	GPIO.setup(echo_pin, GPIO.IN)
	
	GPIO.output(trig_pin, GPIO.LOW)
	time.sleep(2)
	GPIO.output(trig_pin, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(trig_pin, GPIO.LOW)
	
	while GPIO.input(echo_pin)==0:
		print(GPIO.input(echo_pin))
		time.sleep(1)
		pulse_start = time.time()

	while GPIO.input(echo_pin)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration *1800

	print('There is an object %d inches away' %(distance))
	time.sleep(1)
