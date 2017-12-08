from mpu6050 import mpu6050
from time import sleep
import plt

sensor = mpu6050(0x68)

def update():
    accel_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()
    temp = sensor.get_temp()

    print("Accelerometer data")
    print("x: " + str(accel_data['x']))
    print("y: " + str(accel_data['y']))
    print("z: " + str(accel_data['z']))
    print
    print("Gyroscope data")
    print("x: " + str(gyro_data['x']))
    print("y: " + str(gyro_data['y']))
    print("z: " + str(gyro_data['z']))
    print
    print("Temp: " + str(temp) + " C")
    print
    sleep(0.5)
    
    