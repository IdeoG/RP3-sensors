import time
import Adafruit_ADS1x15

if __name__ == "__main__":
    adc = Adafruit_ADS1x15.ADS1115()
    GAIN = 1
    v_ref = 5
    k_c = 50
    k_v = 4.096 / float(1<<15)
    
    while True:
        adc_value = adc.read_adc(1, gain=GAIN) * k_v
        current = adc_value - v_ref/2
        print("current: {}, adc_value: {}".format(current, adc_value))
        time.sleep(1)