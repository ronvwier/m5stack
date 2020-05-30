from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import unit
import json
import wifiCfg
import machine

class RetainM5mqtt(M5mqtt):
    
    def publish(self, topic, data, retain=False, qos=0):
        if type(topic) is int:
            topic = str(topic)
        if type(data) is int:
            data = str(data)
        if self.mqttState:
            try:
                self.mqtt.publish(topic, data, retain=retain, qos=qos)
            except:
                self.mqttState = False


def blink(color):
    if color=='red':
        rgb.setColorAll(0xFF0000)
    if color=='green':
        rgb.setColorAll(0x00FF00)
    if color=='yellow':
        rgb.setColorAll(0xFFFF00)
    if color=='white':
        rgb.setColorAll(0xFFFFFF)
    wait_ms(150)
    rgb.setColorAll(0x404080)    
        
def wificheck():
    while not wifiCfg.wlan_sta.isconnected():
        blink('red')
        wifiCfg.reconnect()
    blink('white')    

wificheck()

m5mqtt = RetainM5mqtt('nanomqttwait', '192.168.0.129', 1883, '', '', 300)
m5mqtt.start()

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
    msg = 'deep sleep starter'
else:
    print('NOT woke from a deep sleep')
    msg = 'normal starter'

while True:
    t_dict = { "ticks": time.ticks_ms(), 'msg': msg }
    s_dict = json.dumps(t_dict)
    m5mqtt.publish('timer/ticks',s_dict, retain=True, qos=1) # qos=1 is needed with lightsleep!
    blink('green')
    wait(10)

#machine.deepsleep(10000) # sleep 60 seconds and restart machine


