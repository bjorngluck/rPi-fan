import RPi.GPIO as GPIO
import time
import subprocess as sp


# initializing GPIO, setting mode to BOARD.
# Default pin of FAN Adapter is physical pin 32, GPIO12;
Fan = 32  #if you connect to pin txd physical pin 8, GPIO14，then set to :Fan = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Fan, GPIO.OUT)

p = GPIO.PWM(Fan, 50)
p.start(0)

try:
    while True:
        temp = sp.getoutput("vcgencmd measure_temp|egrep -o '[0-9]*\.[0-9]*'")
        # print(temp)
        cpu = float(temp)
        #print('CPU temperature is: %2.2f' % cpu)
        if float(temp) < 40.0:
            p.ChangeDutyCycle(0)
            print('Fan is off as CPU temperature is %2.2f' % cpu)
            time.sleep(5)
        elif float(temp) > 40.0 and float(temp) < 45.0:
            p.ChangeDutyCycle(30)
            print('Fan is on 30 as CPU temperature is %2.2f' % cpu)
            time.sleep(5)
        elif float(temp) > 45.0 and float(temp) < 50.0:
            p.ChangeDutyCycle(50)
            print('Fan is on 50 as CPU temperature is %2.2f' % cpu)
            time.sleep(5)
        elif float(temp) > 50.0 and float(temp) < 60.0:
            p.ChangeDutyCycle(75)
            print('Fan is on 75 as CPU temperature is %2.2f' % cpu)
            time.sleep(5)
        elif float(temp) > 60.0:
            p.ChangeDutyCycle(100)
            print('Fan is on 100 as CPU temperature is %2.2f' % cpu)
            time.sleep(5)

except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
