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
        setScreenColor(0xFF0000)
    if color=='green':
        setScreenColor(0x00FF00)
    if color=='yellow':
        setScreenColor(0xFFFF00)
    if color=='white':
        setScreenColor(0xFFFFFF)
    wait_ms(150)
    setScreenColor(0x404080)    
        
def fastwifi():
    
    while not wifiCfg.wlan_sta.isconnected():
        blink('red')

        wifiCfg.wlan_sta.active(True)
        jdata = cfgRead('wifi')
        wifiCfg.wlan_sta.connect(jdata['ssid'], jdata['password'])
            
        wait(1)
            
    blink('white')    

# dim the LCD
lcd.setBrightness(5)

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
    msg = 'deep sleep starter'
else:
    print('NOT woke from a deep sleep')
    msg = 'normal starter'

# activate the WiFI and the MQTT connection
fastwifi()
m5mqtt = RetainM5mqtt('mqttdeepsleep', '192.168.0.129', 1883, '', '', 300)
m5mqtt.start()

# send the message
t_dict = { "ticks": time.ticks_ms(), 'msg': msg }
s_dict = json.dumps(t_dict)
m5mqtt.publish('timer/ticks',s_dict, retain=True, qos=1) # qos=1 is needed with lightsleep!
blink('green')

# sleep 60 seconds and restart the machine
print('going to deepsleep for 30 sec')
machine.deepsleep(30000) 


