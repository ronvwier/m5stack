from m5stack import *
from m5ui import *
from uiflow import *
import unit
import json
import network
import machine

def blink(color):
    colorcode = { 'black': 0x000000, 'red': 0xFF0000, 'green': 0x00FF00, 'yellow': 0xFFFF00, 'white':0x808080 }
    rgb.setColorAll(colorcode[color])
    print(color)
    wait_ms(250)
    rgb.setColorAll(colorcode['black'])
        
def wificheck():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
        
    while not wlan.isconnected():
        blink('red')
        wifi = cfgRead('wifi')
        print('connecting to network...',wifi)
        wlan.connect(wifi['ssid'], wifi['password'])
        wait(4)

    print('network config:', wlan.ifconfig())
    blink('white')    
        
# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
else:
    print('NOT woke from a deep sleep')

wificheck()

blink('green')

print('going to deepsleep')
machine.deepsleep(10000)
