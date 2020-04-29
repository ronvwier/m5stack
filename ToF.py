from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x000000)
tof0 = unit.get(unit.TOF, unit.PORTA)




label0 = M5TextBox(85, 83, "Text", lcd.FONT_DejaVu72,0x08feab, rotate=0)
label1 = M5TextBox(227, 174, "mm", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label2 = M5TextBox(28, 30, "distance:", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)


while True:
  label0.setText(str(tof0.distance))
  if (tof0.distance) < 300:
    rgb.setColorAll(0xff0000)
    wait(((tof0.distance) / 2000))
    rgb.setColorAll(0x000000)
    wait(((tof0.distance) / 2000))
    speaker.sing(622, 1/16)
  else:
    rgb.setColorAll(0x009900)
  wait_ms(2)
