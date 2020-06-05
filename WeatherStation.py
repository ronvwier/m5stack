from m5stack import *
from m5ui import *
from uiflow import *
import i2c_bus
import json
import network

from m5mqtt import M5mqtt

def wificheck():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
        
    while not wlan.isconnected():
        #blink('red')
        wifi = cfgRead('wifi')
        print('connecting to network...',wifi)
        wlan.connect(wifi['ssid'], wifi['password'])
        wait(1)

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


setScreenColor(0x222222)
wificheck()
print('Patched M5MQTT use')
m5mqtt = PatchedM5mqtt('', '192.168.0.129', 1883, '', '', 300)

title0 = M5Title(title="M5Stack2 Weatherstation", x=3 , fgcolor=0xFFFFFF, bgcolor=0x0000FF)
s_temperature = M5TextBox(5, 80, "12.3", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
rectangle1 = M5Rect(220, 72, 100, 140, 0x944104, 0xFFFFFF)
rectangle0 = M5Rect(0, 72, 100, 140, 0x01515a, 0xFFFFFF)
s_pressure = M5TextBox(2, 187, "1234", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)
s_humidity = M5TextBox(5, 130, "12", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label3 = M5TextBox(80, 80, "C", lcd.FONT_Default,0xFFFFFF, rotate=0)
label4 = M5TextBox(65, 185, "hPa", lcd.FONT_Default,0xFFFFFF, rotate=0)
label5 = M5TextBox(80, 130, "%", lcd.FONT_Default,0xFFFFFF, rotate=0)
s_temp_in = M5TextBox(224, 80, "12.3", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
s_hum_in = M5TextBox(224, 130, "12", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
s_date = M5TextBox(66, 36, "Mon 05 dec 2020", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)
label0 = M5TextBox(300, 80, "C", lcd.FONT_Default,0xFFFFFF, rotate=0)
label1 = M5TextBox(300, 130, "%", lcd.FONT_Default,0xFFFFFF, rotate=0)
s_time = M5TextBox(120, 104, "12:35", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)

t_env = None
t_dict = None
regs = None
i2c0 = i2c_bus.easyI2C(i2c_bus.PORTA, 0x5c)

from dht12 import DHT12
dht12 = DHT12(i2c0.i2c)

def read_dht12():
  global t_env, t_dict, regs, i2c0, dht12
  #regs = i2c0.read_reg(0x00, 5)
  #s_temp_in.setText(str(regs[2]))
  #s_hum_in.setText(str(regs[0]))
  dht12.measure()
  h = dht12.humidity()
  s_hum_in.setText(str(h))
  t = dht12.temperature()
  s_temp_in.setText(str(t))
  
def fun_env_out_(topic_data):
  global t_env, t_dict, regs
  t_env = json.loads(topic_data)
  s_temperature.setText(str(t_env['temperature']))
  s_pressure.setText(str(t_env['pressure']))
  s_humidity.setText(str(t_env['humidity']))
  read_dht12()
  pass
m5mqtt.subscribe('env/out', fun_env_out_)

def fun_time_display_(topic_data):
  global t_env, t_dict, regs
  t_dict = json.loads(topic_data)
  s_date.setText(str(t_dict['date']))
  s_time.setText(str(t_dict['time']))
  pass
m5mqtt.subscribe('time/display', fun_time_display_)


m5mqtt.start()
lcd.setBrightness(5)
#read_dht12()
