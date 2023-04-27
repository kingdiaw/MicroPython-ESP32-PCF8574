# Scanner i2c en MicroPython | MicroPython i2c scanner
# Renvoi l'adresse en decimal et hexa de chaque device connecte sur le bus i2c
# Return decimal and hexa adress of each i2c device
# https://projetsdiy.fr - https://diyprojects.io (dec. 2017)

# (1) import related library
from time import ticks_add,ticks_ms, ticks_diff
from machine import Pin, I2C

# (2) Declare Constant Value
SDA_PIN = const (21)
SCL_PIN = const (22)

# (3) Creating Object
i2c = I2C(0, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN))

# (4) Setup
task1_interval = ticks_add (ticks_ms(), 100)
print('Scan i2c bus...')

# (5) Loop
try:
    while True:
        if ticks_diff (task1_interval, ticks_ms())<= 0:
            task1_interval = ticks_add(ticks_ms(),5000)
            
            devices = i2c.scan()

            if len(devices) == 0:
              print("No i2c device !")
            else:
              print('i2c devices found:',len(devices))

            for device in devices:  
                print("Decimal address: ",device," | Hexa address: ",hex(device))

except KeyboardInterrupt:
    print("Bye")