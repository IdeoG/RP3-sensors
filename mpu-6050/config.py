from mpu6050 import mpu6050
from time import sleep

ACCEL_RANGE_2G = 0x00
ACCEL_RANGE_4G = 0x08
ACCEL_RANGE_8G = 0x10
ACCEL_RANGE_16G = 0x18

def __name__= "__main__":    
    sensor = mpu6050(0x68)
    sensor.set_accel_range(ACCEL_RANGE_16G)

    while True:
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