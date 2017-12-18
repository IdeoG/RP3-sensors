import time
import Adafruit_ADS1x15

if __name__ == "__main__":
    adc = Adafruit_ADS1x15.ADS1115()
    GAIN = 1
    V_MAX = 3.300
    V_MIN = 0.550
    KV = V_MAX / float(1<<15)
    
    while True:
        adc_value = adc.read_adc(0, gain=GAIN) * KV
        humidity = (V_MAX - (adc_value - V_MIN)) / (V_MAX-V_MIN)
        print("humidity: {0:.3f}%".format(humidity))
        time.sleep(1)