import cv2
import RPi.GPIO as GPIO
import numpy as np
from time import sleep

import tflite_runtime.interpreter as tflite

def trained_model():
    #interpreter = tflite.Interpreter(model_path="f_dataset_new.tflite")
    interpreter = tflite.Interpreter(model_path="monday2_check.tflite")
    interpreter.allocate_tensors()
    return interpreter

PWMA = 18
AIN1   =  22
AIN2   =  27

PWMB = 23
BIN1   = 25
BIN2  =  24

def motor_back(speed):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN1,False)#AIN2
    GPIO.output(AIN2,True) #AIN1
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,False)#BIN2
    GPIO.output(BIN2,True) #BIN1
    
def motor_go(speed):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN1,True)#AIN2
    GPIO.output(AIN2,False) #AIN1
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,True)#BIN2
    GPIO.output(BIN2,False) #BIN1

def motor_stop():
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(AIN1,False)#AIN2
    GPIO.output(AIN2,False) #AIN1
    R_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN1,False)#BIN2
    GPIO.output(BIN2,False) #BIN1
    
def motor_right(speed):
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN1,True)#AIN2
    GPIO.output(AIN2,False) #AIN1
    R_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN1,False)#BIN2
    GPIO.output(BIN2,True) #BIN1
    
def motor_left(speed):
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(AIN1,False)#AIN2
    GPIO.output(AIN2,True) #AIN1
    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1,True)#BIN2
    GPIO.output(BIN2,False) #BIN1
        
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(PWMA,GPIO.OUT)

GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)

L_Motor= GPIO.PWM(PWMA,500)
L_Motor.start(0)

R_Motor = GPIO.PWM(PWMB,500)
R_Motor.start(0)

speedSet = 25

def img_preprocess(image):
    height, _,_= image.shape
    image = image[int(height/2):,:,:]
    
    _,image= cv2.threshold(image,90,255,cv2.THRESH_BINARY_INV)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image = cv2.GaussianBlur(image, (3,3), 0)
    image = cv2.resize(image, (200,66))
    
    image = image / 255
    return image

def main():
    interpreter=trained_model()
    camera = cv2.VideoCapture(0)
    camera.set(3, 640)
    camera.set(4, 480)
    
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    carState = "stop"
    
    while( camera.isOpened()):
        
        keValue = cv2.waitKey(1)
        
        if keValue == ord('q') :
            break
        elif keValue == 82 :
            print("go")
            carState = "go"
        elif keValue == 84 :
            print("stop")
            carState = "stop"
        
        _, image = camera.read()
        image = cv2.flip(image,-1)
        cv2.imshow('Original', image)
        
        preprocessed = img_preprocess(image)
        
        cv2.imshow('pre', preprocessed)
        preprocessed=preprocessed.reshape(66,200,1)
        
        X = np.float32(np.asarray([preprocessed]))
    
        
        interpreter.set_tensor(input_details[0]['index'], X)
        interpreter.invoke()
        
        
        #input_tensor=np.array(X,dtype=np.float32)
        #input_index=interpreter.get_input_details()[0]['index']
    
        ##interpreter.set_tensor(input_index, input_tensor)
        #interpreter.set_tensor(input_index, input_tensor)

       # interpreter.invoke()
       # output_details = interpreter.get_output_details()
    
         #output_data = interpreter.get_tensor(output_details[0]['index'])
        
        steering_angle = int(interpreter.get_tensor(output_details[0]['index']))
        #print("predict angle:",steering_angle)
        
        if carState == "go":
            if steering_angle >= 85 and steering_angle <= 100:
                print("go: " + str(steering_angle))
                motor_go(speedSet)
            elif steering_angle >101:
                print("right: "+ str(steering_angle))
                #motor_left(speedSet)
                motor_right(speedSet)
            elif steering_angle < 84:
                print("left: "+ str(steering_angle))
                #motor_right(speedSet)
                motor_left(speedSet)
                
        elif carState == "stop":
            motor_stop()
        
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
    GPIO.cleanup()

