from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x000000)




bar1 = M5Rect(75, 75, 30, 80, 0x33cc00, 0x33cc00)
bar2 = M5Rect(120, 75, 30, 80, 0x000000, 0x000000)
bar3 = M5Rect(164, 75, 30, 80, 0x000000, 0x000000)
bar4 = M5Rect(210, 75, 30, 80, 0x000000, 0x000000)
rect4 = M5Rect(60, 61, 200, 1, 0xFFFFFF, 0xFFFFFF)
rect5 = M5Rect(60, 63, 1, 100, 0xFFFFFF, 0xFFFFFF)
rect6 = M5Rect(60, 164, 200, 1, 0xFFFFFF, 0xFFFFFF)
rect7 = M5Rect(259, 64, 1, 100, 0xFFFFFF, 0xFFFFFF)
rect8 = M5Rect(259, 99, 20, 30, 0xFFFFFF, 0xFFFFFF)
percentage = M5TextBox(60, 190, "0", lcd.FONT_Comic,0xFFFFFF, rotate=0)
label1 = M5TextBox(106, 189, "%", lcd.FONT_Comic,0xFFFFFF, rotate=0)

def slow():
  wait(1)



rgb.setColorAll(0x33cc00)
while True:
  percentage.setText(str(power.getBatteryLevel()))
  if power.isCharging():
    bar2.setBgColor(0x33cc00)
    slow()
    bar3.setBgColor(0x33cc00)
    slow()
    bar4.setBgColor(0x33cc00)
    slow()
    bar2.setBgColor(0x000000)
    bar3.setBgColor(0x000000)
    bar4.setBgColor(0x000000)
  else:
    bar2.setBgColor(0x000000)
    bar3.setBgColor(0x000000)
    bar4.setBgColor(0x000000)
    if (power.getBatteryLevel()) >= 25:
      bar2.setBgColor(0x33cc00)
    if (power.getBatteryLevel()) >= 50:
      bar3.setBgColor(0x33cc00)
    if (power.getBatteryLevel()) >= 75:
      bar4.setBgColor(0x33cc00)
  slow()
  wait_ms(2)
