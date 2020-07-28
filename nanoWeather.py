import machine
import time

uart=machine.UART(1,tx=25,rx=21,baudrate=9600)

end_cmd=b'\xFF\xFF\xFF'

def sendNextion(cmd):
    uart.write(cmd)
    uart.write(end_cmd)
    time.sleep_ms(100)
    response = uart.read()
    print("Command:",cmd,"Response:", response)


from m5stack import *
from m5ui import *
from uiflow import *
import i2c_bus
import json
import network

from m5mqtt import M5mqtt

class PatchedM5mqtt(M5mqtt):
    
    # Make retainable messages possible
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

    def subscribe(self, topic, callback):
        # Add callback first before subscribe! otherwise timing error
        self.topic_callback[topic] = callback
        print('topic =',topic)
        self.mqtt.subscribe(topic)
        
    def _on_data(self, topic, data):
        print('topic received:',topic)
        print('data received:',data)
        stopic = str(topic,'utf-8')
        sdata = str(data,'utf-8')
        print('stopic:',topic)
        print('sdata:',data)
        self.topic_callback[stopic](sdata)


def wificheck():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
        
    while not wlan.isconnected():
        #blink('red')
        wifi = cfgRead('wifi')
        print('connecting to network...',wifi)
        wlan.connect(wifi['ssid'], wifi['password'])
        wait(4)

    print('network config:', wlan.ifconfig())
    #blink('white')    


wificheck()
print('Patched M5MQTT use')
m5mqtt = PatchedM5mqtt('weatherNextion', '192.168.0.129', 1883, '', '', 300)

t_env = None
t_dict = None
regs = None
#i2c0 = i2c_bus.easyI2C(i2c_bus.PORTA, 0x5c)

#from dht12 import DHT12
#dht12 = DHT12(i2c0.i2c)

def read_dht12():
  global t_env, t_dict, regs, i2c0, dht12
  #regs = i2c0.read_reg(0x00, 5)
  #s_temp_in.setText(str(regs[2]))
  #s_hum_in.setText(str(regs[0]))
  # dht12.measure()
  #h = dht12.humidity()
  #s_hum_in.setText(str(h))
  #t = dht12.temperature()
  #s_temp_in.setText(str(t))
  
def fun_env_out_(topic_data):
  t_env = json.loads(topic_data)
  sendNextion('global.temperature.txt="'+t_env['temperature']+'"')
  sendNextion('global.humidity.txt="'+t_env['humidity']+'"')
  sendNextion('global.pressure.txt="'+t_env['pressure']+'"')
  print(t_env['temperature'])
  temp = int(float(t_env['temperature']) + 50)
  read_dht12()
  pass
m5mqtt.subscribe('env/out', fun_env_out_)

def fun_time_display_(topic_data):
  t_dict = json.loads(topic_data)
  sendNextion('global.time.txt="'+t_dict['time']+'"')
  sendNextion('global.date.txt="'+t_dict['date']+'"')
  pass
m5mqtt.subscribe('time/display', fun_time_display_)

def fun_sun_home_(topic_data):
  t_dict = json.loads(topic_data)
  sendNextion('global.sun.val='+str(int(t_dict['currentPerc']*100)))
  pass
m5mqtt.subscribe('sun/home', fun_sun_home_)

def fun_env_out_rain_(topic_data):
  sendNextion('global.rain.val='+topic_data)
  pass
m5mqtt.subscribe('env/out/rain', fun_env_out_rain_)

m5mqtt.start()
#lcd.setBrightness(5)
#read_dht12()



