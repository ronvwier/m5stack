from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import unit
import json

setScreenColor(0x222222)
env0 = unit.get(unit.ENV, unit.PORTA)

m5mqtt = M5mqtt('mqttenv', '192.168.0.129', 1883, '', '', 300)

title0 = M5Title(title="M5Stack2 to MQTT on ENV", x=3 , fgcolor=0xFFFFFF, bgcolor=0x0000FF)
s_temperature = M5TextBox(10, 50, "12.3", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
s_pressure = M5TextBox(10, 100, "1234", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
s_humidity = M5TextBox(10, 150, "12", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label3 = M5TextBox(80, 50, "C", lcd.FONT_Default,0xFFFFFF, rotate=0)
label4 = M5TextBox(80, 100, "hPa", lcd.FONT_Default,0xFFFFFF, rotate=0)
label5 = M5TextBox(80, 150, "%", lcd.FONT_Default,0xFFFFFF, rotate=0)
s_ticks = M5TextBox(10, 200, "0", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)

m5mqtt.start()

while True:
  s_ticks.setText(str(time.ticks_ms()))
  t_temp = env0.temperature
  t_temp = "%.1f"%(t_temp)
  t_press = env0.pressure
  t_press = "%.f"%(t_press)
  t_hum = env0.humidity
  t_hum = "%.f"%(t_hum)
  t_dict = { "temperature": t_temp, 'pressure': t_press, 'humidity': t_hum }
  s_dict = json.dumps(t_dict)
  m5mqtt.publish('env/out',s_dict)
  s_temperature.setText(str(t_temp))
  s_pressure.setText(str(t_press))
  s_humidity.setText(str(t_hum))
  wait(10)
