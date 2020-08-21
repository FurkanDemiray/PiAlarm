#!/home/pi/Desktop/PiAlarm/tflite1-env/bin python3
import os
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import subprocess

GPIO.setup(23,GPIO.IN)



try:
    time.sleep(2)
    while True:
        if GPIO.input(23):
            
            print("Hareket Algılandı")
            
            time.sleep(3)
            
            os.system("python3 TFLite_detection_webcam.py --modeldir=Sample_TFLite_model/")
except:
    GPIO.cleanup()