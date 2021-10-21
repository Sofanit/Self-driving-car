import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
Buzzer=12
GPIO.setup(Buzzer,GPIO.OUT)
p = GPIO.PWM(Buzzer,1)
p.start(0)

def play_c(freq):
    print("playing music")
    p.start(60)
    p.ChangeFrequency(freq)
    
    time.sleep(0.3)
    p.stop()
            
    