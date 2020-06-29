from m5stack import *
from m5ui import *
from uiflow import *
import i2c_bus
import json
import network
from dht12 import DHT12
from m5mqtt import M5mqtt

def wificheck():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
        
    while not wlan.isconnected():
        wifi = cfgRead('wifi')
        wlan.connect(wifi['ssid'], wifi['password'])
        wait(4)

class PatchedM5mqtt(M5mqtt):
    
    # Make retainable messages possible
    def publish(self, topic, data, retain=True, qos=1):
        if self.mqttState:
            try:
                self.mqtt.publish(topic, data, retain=retain, qos=qos)
            except:
                self.mqttState = False

    def subscribe(self, topic, callback):
        # Add callback first before subscribe! otherwise timing error
        self.topic_callback[topic] = callback
        self.mqtt.subscribe(topic)
        
    def _on_data(self, topic, data):
        stopic = str(topic,'utf-8')
        sdata = str(data,'utf-8')
        self.topic_callback[stopic](sdata)


lcd.setBrightness(5)
setScreenColor(0x222222)
wificheck()
m5mqtt = PatchedM5mqtt('weatherstation', '192.168.0.129', 1883, '', '', 30)

# date and time  on top line
s_date = M5TextBox(0, 0, "Mon 05 dec 2020", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)
s_time = M5TextBox(200, 0, "12:35", lcd.FONT_DejaVu40,0xFFFFFF, rotate=0)

# boxes around figures
rectangle0 = M5Rect(0,   50, 150, 180, 0x01515a, 0xFFFFFF)
rectangle1 = M5Rect(170, 50, 150, 180, 0x944104, 0xFFFFFF)

# temperatures outside
s_temp_max    = M5TextBox(25,  60, "34.5", lcd.FONT_DejaVu24,0xD0D0D0, rotate=0)
s_temperature = M5TextBox(25,  90, "23.4", lcd.FONT_DejaVu40,0xFFFFFF, rotate=0)
s_temp_min    = M5TextBox(25, 130, "12.3", lcd.FONT_DejaVu24,0xD0D0D0, rotate=0)
s_humidity = M5TextBox(25, 170, "12", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label5 = M5TextBox(100, 170, "%", lcd.FONT_Default,0xFFFFFF, rotate=0)
s_pressure = M5TextBox(25, 200, "1234", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)
label4 = M5TextBox(85, 200, "hPa", lcd.FONT_Default,0xFFFFFF, rotate=0)

# temperature inside
s_temp_in = M5TextBox(200, 90, "12.3", lcd.FONT_DejaVu40,0xFFFFFF, rotate=0)
s_hum_in = M5TextBox(200, 170, "12", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label1 = M5TextBox(260, 170, "%", lcd.FONT_Default,0xFFFFFF, rotate=0)

i2c0 = i2c_bus.easyI2C(i2c_bus.PORTA, 0x5c)
dht12 = DHT12(i2c0.i2c)

def read_dht12():
  global dht12
  try:
      dht12.measure()
      h = dht12.humidity()
      s_hum_in.setText(str(h))
      t = dht12.temperature()
      s_temp_in.setText(str(t))
  except:
      s_hum_in.setText("Error")
      s_temp_in.setText("Error")
        
def fun_env_out_(topic_data):
  t_env = json.loads(topic_data)
  s_temperature.setText(str(t_env['temperature']))
  s_pressure.setText(str(t_env['pressure']))
  s_humidity.setText(str(t_env['humidity']))
  pass
m5mqtt.subscribe('env/out', fun_env_out_)

def fun_time_display_(topic_data):
  t_dict = json.loads(topic_data)
  s_date.setText(str(t_dict['date']))
  s_time.setText(str(t_dict['time']))
  read_dht12()
  pass
m5mqtt.subscribe('time/display', fun_time_display_)

def fun_env_out_maxtemp_(topic_data):
  s_temp_max.setText(topic_data)
  pass
m5mqtt.subscribe('env/out/maxtemp', fun_env_out_maxtemp_)

def fun_env_out_mintemp_(topic_data):
  s_temp_min.setText(topic_data)
  pass
m5mqtt.subscribe('env/out/mintemp', fun_env_out_mintemp_)

m5mqtt.start()
