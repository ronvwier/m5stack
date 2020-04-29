from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x000000)
env0 = unit.get(unit.ENV, unit.PORTA)




circle4 = M5Circle(56, 61, 20, 0xff9900, 0x000000)
circle2 = M5Circle(108, 99, 20, 0xFFFFFF, 0xFFFFFF)
circle3 = M5Circle(88, 111, 20, 0xFFFFFF, 0xFFFFFF)
circle0 = M5Circle(137, 98, 32, 0xFFFFFF, 0xFFFFFF)
circle9 = M5Circle(115, 110, 20, 0xFFFFFF, 0xFFFFFF)
labelTemp = M5TextBox(247, 52, "00 C", lcd.FONT_Comic,0xffffff, rotate=0)
labelPressure = M5TextBox(226, 90, "1000 P", lcd.FONT_Comic,0xFFFFFF, rotate=0)
labelHumidity = M5TextBox(247, 122, "00 %", lcd.FONT_Comic,0xFFFFFF, rotate=0)
rect3 = M5Rect(91, 134, 1, 2, 0xFFFFFF, 0xFFFFFF)
rect4 = M5Rect(112, 134, 1, 2, 0xFFFFFF, 0xFFFFFF)
rect5 = M5Rect(135, 134, 1, 2, 0xFFFFFF, 0xFFFFFF)
rect6 = M5Rect(159, 134, 1, 2, 0xFFFFFF, 0xFFFFFF)
circle12 = M5Circle(164, 110, 20, 0xFFFFFF, 0xFFFFFF)

import math
import random

random2 = None
i = None



while True:
  labelTemp.setText(str((str(round(env0.temperature)) + ' C')))
  labelPressure.setText(str((str(round(env0.pressure)) + ' P')))
  labelHumidity.setText(str((str(round(env0.humidity)) + ' %')))
  wait(1)
  if (env0.humidity) >= 50:
    circle4.setBgColor(0x000000)
    rgb.setColorAll(0x000099)
    rect3.setBorderColor(0x3333ff)
    rect4.setBorderColor(0x3333ff)
    rect5.setBorderColor(0x3333ff)
    rect6.setBorderColor(0x3333ff)
    random2 = random.randint(2, 50)
    rect3.setSize(height=random2)
    random2 = random.randint(2, 50)
    rect4.setSize(height=random2)
    random2 = random.randint(2, 50)
    rect5.setSize(height=random2)
    random2 = random.randint(2, 50)
    rect6.setSize(height=random2)
  else:
    rect3.setBorderColor(0x000000)
    rect4.setBorderColor(0x000000)
    rect5.setBorderColor(0x000000)
    rect6.setBorderColor(0x000000)
    circle4.setBgColor(0xff6600)
    rgb.setColorAll(0xff6600)
    for i in range(20, 31):
      lcd.circle(56, 61, i, color=0xff9900)
      lcd.circle(56, 61, (i - 1), color=0x000000)
      wait(0.05)
    lcd.circle(56, 61, 30, color=0x000000)
  wait_ms(2)
