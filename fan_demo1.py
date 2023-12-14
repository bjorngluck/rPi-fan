import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
##Set to false, other processes occupying the pin will be ignored
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12,100)

print("\nPress Ctrl+C to quit \n")
dc = 0
pwm.start(dc)

def ReadTemp():
        # view CPU temperature
        file = open("/sys/class/thermal/thermal_zone0/temp")
        cpu = float(file.read()) / 1000
        file.close()
        print('CPU temperature is: %2.2f' % cpu)
        time.sleep(5)

try:
    while True:
        temp = subprocess.getoutput("vcgencmd measure_temp|sed 's/[^0-9.]//g'")
        ReadTemp()
        if round(float(temp)) >= 40:
            dc = 10
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05)
        else:
            dc = 0
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Ctrl + C pressed -- Ending program")
