from gpiozero import Servo
from time import sleep
from mpu6050 import mpu6050


servo_GPIO = 17

maxPW = 26/10000
minPW = 8/10000

servo = Servo(servo_GPIO,min_pulse_width=minPW,max_pulse_width=maxPW)

sensor = mpu6050(0x68)

servo_position = 0.0
prev_position = 0.0
step_val = 0.05

while True:
    accelerometer_data = sensor.get_accel_data()
    X = accelerometer_data ['x']
    print(X)
    
    #servo_position -= X/150
    servo_position = round(X/9.75, 2)
    
    if servo_position > 1:
        servo_position = 1
    elif servo_position < -1:
        servo_position = -1
    
    servo_position = round(servo_position, 2)
    print(servo_position)
    
    if((abs(servo_position) - abs(prev_position)) >= step_val):
        servo.value = servo_position
        
    sleep(0.1)