# https://pypi.org/project/pcf8574-library/
# https://docs.micropython.org/en/latest/library/time.html

# (1) import related library
from time import ticks_add,ticks_ms, ticks_diff 
from machine import Pin
from PCF8574 import PCF8574, P0, P1, P2, P3, P4, P5, P6, P7

# (2) Declare Constant Value
SDA_PIN = const (21)
SCL_PIN = const (22)
PCF1_ADDRESS = const (0x20)

# (3) Creating Object
pcf = PCF8574(PCF1_ADDRESS, sda=SDA_PIN, scl=SCL_PIN)

# (4) Variable
task1_interval = ticks_add (ticks_ms(), 500)
led1_state = False

# (5) Setup
pcf.Pin(P0, Pin.OUT)


# (6) Loop
try:
    while True:
        if ticks_diff (task1_interval, ticks_ms())<= 0:
            led1_state ^= 1
            task1_interval = ticks_add(ticks_ms(),500)
            pcf.digital_write(P0, led1_state)
            print ("Led:%d" %led1_state)
            
except KeyboardInterrupt:
    print("Bye")
