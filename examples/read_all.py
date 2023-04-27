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
pcf.Pin(P0, Pin.IN)
pcf.Pin(P1, Pin.IN)
pcf.Pin(P2, Pin.IN)
pcf.Pin(P3, Pin.IN)
pcf.Pin(P4, Pin.IN)
pcf.Pin(P5, Pin.IN)
pcf.Pin(P6, Pin.IN)
pcf.Pin(P7, Pin.IN)
pcf.begin()

# (6) Loop
try:
    while True:
        if ticks_diff (task1_interval, ticks_ms())<= 0:
            task1_interval = ticks_add(ticks_ms(),1000)
            digital_input = pcf.digital_read_all()
            
            print("P0:{} P1:{} P2:{} P3:{} P4:{} P5:{} P6:{} P7:{}".format(digital_input.p0,
                                                                           digital_input.p1,
                                                                           digital_input.p2,
                                                                           digital_input.p3,
                                                                           digital_input.p4,
                                                                           digital_input.p5,
                                                                           digital_input.p6,
                                                                           digital_input.p7))
            
except KeyboardInterrupt:
    print("Bye")

