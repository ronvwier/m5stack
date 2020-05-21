from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import unit
import json
import wifiCfg

def wificheck():
    while !wifiCfg.wlan_sta.isconnected():
        wifiCfg.screenShow()
        wifiCfg.autoConnect(lcdShow = True)
        #wifiCfg.reconnect()

#setScreenColor(0xFF0000)

wificheck()

m5mqtt = M5mqtt('mqttenv', '192.168.0.129', 1883, '', '', 300)
m5mqtt.start()

while True:
    setScreenColor(0x000000)
    wificheck()

    t_dict = { "ticks": time.ticks_ms(), 'msg': 'hope' }
    s_dict = json.dumps(t_dict)
    m5mqtt.publish('timer/ticks',s_dict)
    setScreenColor(0x00FF00)
    
    wait(10)
