from m5stack import *
from m5ui import *
from uiflow import *
import wifiCfg
import urequests
import json


setScreenColor(0x222222)




msg = M5TextBox(28, 57, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)

nunl = None
timeText = None



wifiCfg.autoConnect(lcdShow = False)
try:
  req = urequests.request(method='GET', url='http://worldtimeapi.org/api/ip')
  nunl = req.text
  msg.setText(str(req.status_code))
  msg.setText(str(nunl))
except:
  msg.setText('error denk ik')
timeText = json.loads(nunl)
