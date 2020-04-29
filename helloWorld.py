from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x222222)




uptimeScr = M5TextBox(291, 7, "0", lcd.FONT_Default,0xFFFFFF, rotate=0)
title0 = M5Title(title="Ron", x=3 , fgcolor=0xFFFFFF, bgcolor=0x0000FF)
hello = M5TextBox(2, 48, "Hello", lcd.FONT_Comic,0xFFFFFF, rotate=0)
label0 = M5TextBox(2, 150, "Battery level", lcd.FONT_Default,0xFFFFFF, rotate=0)
batlev = M5TextBox(133, 143, "Text", lcd.FONT_Comic,0xFFFFFF, rotate=0)
label1 = M5TextBox(44, 214, "Beep", lcd.FONT_Default,0xFFFFFF, rotate=0)
Count = M5TextBox(138, 213, "Count", lcd.FONT_Default,0xFFFFFF, rotate=0)
timer = M5TextBox(148, 93, "0", lcd.FONT_Comic,0xFFFFFF, rotate=0)
label2 = M5TextBox(194, 141, "%", lcd.FONT_Comic,0xFFFFFF, rotate=0)

sec = None
uptimeCount = None


def buttonA_wasPressed():
  global sec, uptimeCount
  speaker.sing(349, 1/4)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global sec, uptimeCount
  sec = 0
  timer.setText(str(sec))
  timerSch.run('timerCount', 1000, 0x00)
  pass
btnB.wasPressed(buttonB_wasPressed)

@timerSch.event('timer1')
def ttimer1():
  global sec, uptimeCount
  uptimeCount = uptimeCount + 1
  uptimeScr.setText(str(uptimeCount))
  batlev.setText(str(power.getBatteryLevel()))
  pass

@timerSch.event('timerCount')
def ttimerCount():
  global sec, uptimeCount
  sec = sec + 1
  timer.setText(str(sec))
  if sec > 3:
    timerSch.stop('timerCount')
    speaker.sing(889, 1/4)
  pass


speaker.setVolume(1)
hello.setText('Hello World')
uptimeCount = 0
timerSch.run('timer1', 1000, 0x00)
