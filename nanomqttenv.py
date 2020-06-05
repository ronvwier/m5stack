from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import unit
import json
import network
import machine

class RetainM5mqtt(M5mqtt):
    
    def publish(self, topic, data, retain=False, qos=0):
        topic = str(topic)
        data = str(data)
        if self.mqttState:
            try:
                self.mqtt.publish(topic, data, retain=retain, qos=qos)
            except:
                self.mqttState = False

def blink(color):
    colorcode = { 'black': 0x000000, 'red': 0xFF0000, 'green': 0x00FF00, 'yellow': 0xFFFF00, 'white':0x808080 }
    rgb.setColorAll(colorcode[color])
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
        wait(1)

    blink('white')    

wificheck()

env0 = unit.get(unit.ENV, unit.PORTA)

m5mqtt = RetainM5mqtt('nanomqttenv', '192.168.0.129', 1883, '', '', 300)

m5mqtt.start()

while True:
    wificheck()
    t_temp = env0.temperature
    t_temp = "%.1f"%(t_temp)
    t_press = env0.pressure
    t_press = "%.f"%(t_press)
    t_hum = env0.humidity
    t_hum = "%.f"%(t_hum)
    t_dict = { "temperature": t_temp, 'pressure': t_press, 'humidity': t_hum }
    s_dict = json.dumps(t_dict)
    m5mqtt.publish('env/out',s_dict,retain=True)
    print("env/out " + str(s_dict))
    blink('green')
    #wait(10)
    machine.deepsleep(30000)
