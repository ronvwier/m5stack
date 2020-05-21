from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import unit
import json
import wifiCfg

def blink(color):
    if color=='red':
        setScreenColor(0xFF0000)
    if color=='green':
        setScreenColor(0x00FF00)
    if color=='yellow':
        setScreenColor(0xFFFF00)
    if color=='white':
        setScreenColor(0xFFFFFF)
    wait(1)
    setScreenColor(0x000000)    
        
def wificheck():
    while not wifiCfg.wlan_sta.isconnected():
        blink('red')
        #wifiCfg.screenShow()
        #wifiCfg.autoConnect(lcdShow = False)
        wifiCfg.reconnect()
    blink('white')    
    
wificheck()

m5mqtt = M5mqtt('mqttenv', '192.168.0.129', 1883, '', '', 300)
m5mqtt.start()

while True:
    wificheck()
    t_dict = { "ticks": time.ticks_ms(), 'msg': 'hope' }
    s_dict = json.dumps(t_dict)
    m5mqtt.publish('timer/ticks',s_dict)
    blink('green')
    
    wait(5)
