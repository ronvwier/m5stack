from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x000000)
light0 = unit.get(unit.LIGHT, unit.PORTB)




rectangle0 = M5Rect(0, 0, 160, 240, 0x000000, 0x000000)
rectangle1 = M5Rect(160, 0, 160, 240, 0x000000, 0x000000)
circle0 = M5Circle(250, 76, 30, 0xFFFFFF, 0xFFFFFF)
label0 = M5TextBox(187, 145, "Night", lcd.FONT_DejaVu40,0xFFFFFF, rotate=0)
circle1 = M5Circle(262, 67, 30, 0x000000, 0x000000)
circle2 = M5Circle(82, 76, 30, 0xFFFFFF, 0xFFFFFF)
label1 = M5TextBox(46, 145, "Day", lcd.FONT_DejaVu40,0xFFFFFF, rotate=0)


while True:
  if (light0.analogValue) < 300:
    rgb.setColorAll(0xffffff)
    rectangle0.setBorderColor(0x000000)
    rectangle1.setBorderColor(0x3333ff)
  else:
    rgb.setColorAll(0x000000)
    rectangle0.setBorderColor(0x3333ff)
    rectangle1.setBorderColor(0x000000)
  wait_ms(2)
