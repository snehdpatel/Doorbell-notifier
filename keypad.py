import Adafruit_BBIO.GPIO as GPIO
import time

key = '12457'
count = 5
flag = 0
input = list()

while True:
        r0=-1
        r1=-1
        r2=-1
        r3=-1
        c0=-1
        c1=-1
        c2=-1

        GPIO.setup("P8_11", GPIO.OUT)
        GPIO.output("P8_11", GPIO.LOW)
        GPIO.setup("P8_12", GPIO.OUT)
        GPIO.output("P8_12", GPIO.LOW)
        GPIO.setup("P8_13", GPIO.OUT)
        GPIO.output("P8_13", GPIO.LOW)


        GPIO.setup("P8_7", GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup("P8_8", GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup("P8_9", GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup("P8_10", GPIO.IN, GPIO.PUD_DOWN)

        r0 = GPIO.input("P8_7")
        r1 = GPIO.input("P8_8")
        r2 = GPIO.input("P8_9")
        r3 = GPIO.input("P8_10")
#	print r0
#	time.sleep(1)

        GPIO.setup("P8_11", GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup("P8_12", GPIO.IN, GPIO.PUD_DOWN)
        GPIO.setup("P8_13", GPIO.IN, GPIO.PUD_DOWN)

        if r0 == 0:
                GPIO.setup("P8_7", GPIO.OUT)
                GPIO.output("P8_7", GPIO.HIGH)

                c0 = GPIO.input("P8_11")
                if c0 == 1:
                        print "1"
			input.append(1)
			flag = flag+1
                        time.sleep(1)
#                        break

                c1 = GPIO.input("P8_12")
                if c1 == 1:
                        print "2"
			input.append(2)
                        flag = flag+1

                        time.sleep(1)
 #                       break

                c2 = GPIO.input("P8_13")
                if c2 == 1:
                        print "3"
			input.append(3)
                        flag = flag+1

                        time.sleep(1)
  #                      break

        if r1 == 0:
                GPIO.setup("P8_8", GPIO.OUT)
                GPIO.output("P8_8", GPIO.HIGH)

                c0 = GPIO.input("P8_11")
                if c0 == 1:
                        print "4"
			input.append(4)
                        flag = flag+1
                        time.sleep(1)
   #                     break

                c1 = GPIO.input("P8_12")
                if c1 == 1:
                        print "5"
			input.append(5)
                        flag = flag+1
                        time.sleep(1)
    #                    break

                c2 = GPIO.input("P8_13")
                if c2 == 1:
                        print "6"
			input.append(6)
                        flag = flag+1
                        time.sleep(1)
     #                   break

        if r2 == 0:
                GPIO.setup("P8_9", GPIO.OUT)
                GPIO.output("P8_9", GPIO.HIGH)

                c0 = GPIO.input("P8_11")
                if c0 == 1:
                        print "7"
			input.append(7)
                        flag = flag+1
                        time.sleep(1)
      #                  break

                c1 = GPIO.input("P8_12")
                if c1 == 1:
                        print "8"
			input.append(8)
                        flag = flag+1
                        time.sleep(1)
       #                 break

                c2 = GPIO.input("P8_13")
                if c2 == 1:
                        print "9"
			input.append(9)
                        flag = flag+1
                        time.sleep(1)
        #                break


        if r3 == 0:
                GPIO.setup("P8_10", GPIO.OUT)
                GPIO.output("P8_10", GPIO.HIGH)

                c0 = GPIO.input("P8_11")
                if c0 == 1:
                        print "*"
			input.append('*')
                        flag = flag+1
                        time.sleep(1)
         #               break

                c1 = GPIO.input("P8_12")
                if c1 == 1:
                        print "0"
			input.append(0)
                        flag = flag+1
                        time.sleep(1)
          #              break

                c2 = GPIO.input("P8_13")
                if c2 == 1:
                        print "#"
			input.append('#')
                        flag = flag+1
                        time.sleep(1)
           #             break

	if flag == count:
		if input == map(int,key):
			print "DOOR OPEN!"
			del input[:]
			flag = 0
			time.sleep(1)
		else:
			print "WRONG PIN!"
			del input[:]
			flag = 0
			time.sleep(1)
