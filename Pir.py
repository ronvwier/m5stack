from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x000000)
pir0 = unit.get(unit.PIR, unit.PORTB)




circle0 = M5Circle(97, 76, 15, 0x000000, 0x000000)
label0 = M5TextBox(135, 152, "Z", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)
label1 = M5TextBox(168, 127, "Z", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label2 = M5TextBox(204, 93, "Z", lcd.FONT_DejaVu40,0xFFFFFF, rotate=0)
label3 = M5TextBox(245, 56, "Z", lcd.FONT_DejaVu56,0xFFFFFF, rotate=0)
circle1 = M5Circle(214, 76, 15, 0x000000, 0x000000)


while True:
  if (pir0.state) == 1:
    circle0.setBgColor(0xff0000)
    circle1.setBgColor(0xff0000)
    label0.setColor(0x000000)
    label1.setColor(0x000000)
    label2.setColor(0x000000)
    label3.setColor(0x000000)
    speaker.tone(1600, 10)
  else:
    circle0.setBgColor(0x000000)
    circle1.setBgColor(0x000000)
    label0.setColor(0xffffff)
    label1.setColor(0xffffff)
    label2.setColor(0xffffff)
    label3.setColor(0xffffff)
  wait_ms(200)
  wait_ms(2)
