from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import unit
import json
import wifiCfg
import machine

class RetainM5mqtt(M5mqtt):
    
    def publish(self, topic, data):
        if type(topic) is int:
            topic = str(topic)
        if type(data) is int:
            data = str(data)
        if self.mqttState:
            try:
                self.mqtt.publish(topic, data, retain=True)
            except:
                self.mqttState = False


def blink(color):
    if color=='red':
        setScreenColor(0xFF0000)
    if color=='green':
        setScreenColor(0x00FF00)
    if color=='yellow':
        setScreenColor(0xFFFF00)
    if color=='white':
        setScreenColor(0xFFFFFF)
    wait_ms(150)
    setScreenColor(0x404080)    
        
def wificheck():
    while not wifiCfg.wlan_sta.isconnected():
        blink('red')
        wifiCfg.reconnect()
    blink('white')    

lcd.setBrightness(5)
wificheck()

m5mqtt = RetainM5mqtt('mqttminimal', '192.168.0.129', 1883, '', '', 3000)
m5mqtt.start()

while True:
    wificheck()
    t_dict = { "ticks": time.ticks_ms(), 'msg': 'waiter' }
    s_dict = json.dumps(t_dict)
    m5mqtt.publish('timer/ticks',s_dict)
    blink('green')
    wait(20)

