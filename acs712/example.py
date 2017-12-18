import time
import Adafruit_ADS1x15

if __name__ == "__main__":
    adc = Adafruit_ADS1x15.ADS1115()
    GAIN = 1
    V_REF = 3.2
    KC =  5 / (V_REF*0.1)
    KV = 4.096 / float(1<<15)
    
    while True:
        adc_value = adc.read_adc(0, gain=GAIN) * KV
        current = (adc_value - V_REF/2) * KC
        print("current: {}, adc_value: {}".format(current, adc_value))
        time.sleep(1)