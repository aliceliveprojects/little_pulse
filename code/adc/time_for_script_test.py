# testing out how fast the code is read by
#measuring the difference in time between readings

import grove_i2c_adc
import time
current_milli_time = lambda: int(round(time.time() * 1000))

adc= grove_i2c_adc.ADC(address=0x50)

while True:
    data = [adc.adc_read(), current_milli_time()]
#Print the 12 bit value from the I2C ADC next to the current time
    print(data)
    
  #1 reading approximately every 2 milli seconds 
