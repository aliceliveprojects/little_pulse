# Code

## ADC
Simple code used to read from the Dexter I2C-bus analog to digital converter. We wanted to find out how fast we could read samples from it, for our pulse rate monitor.

## CSV
Quick example code, for reading and writing a CSV file 

## Pulse Sensor
Example code for reading the output from the pulse sensor.

The pulse sensor is from www.pulsesensor.com.
Its analogue output is matched to the input of of a Grove I2C ADC Component:


```
RPi <---> Grove Board <---> I2C ADC <---> Pulse Sensor
```

### Connect the pulse sensor
The pulse sensor is connected to the I2C ADC:

The pins on the pulse sensor cable fit nicely into the grove connector cable:

```
RPI Grove Board    Grove Connector         I2C ADC     Grove Connector    Pulse Sensor Connector
I2C Connector
                    Black            -GND-  |  - GND -      Black         -|-   Black
                    Red              -VCC-  |  - Vcc -      Red           -|-   Red
                    White            -SDA-  |  - NC  -      White         -|-
                    Yellow           -SCL-  |  - SIG -      Yellow        -|-   Purple

```

The sample code should be set-up to communicate with the I2C ADC connector, using the ADC's default bus address of 0x50.



Good Luck! :-)