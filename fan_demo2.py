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
        if float(temp) < 48.0:
            p.ChangeDutyCycle(0)
        elif float(temp) > 48.0 and float(temp) < 60.0:
            p.ChangeDutyCycle(100)
            time.sleep(0.1)
        elif float(temp) > 60.0:
            p.ChangeDutyCycle(100)
            time.sleep(0.1)

except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()