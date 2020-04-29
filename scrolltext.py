from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x3e0348)




circle2 = M5Circle(106, 83, 40, 0xFFFFFF, 0xFFFFFF)
circle0 = M5Circle(157, 102, 50, 0xf8f874, 0xf5032f)
circle1 = M5Circle(205, 92, 30, 0xFFFFFF, 0x050000)
Welcome = M5Title(title="Welcome", x=3 , fgcolor=0xFFFFFF, bgcolor=0x0000FF)
displayText = M5TextBox(2, 163, "Welcome to the machine...", lcd.FONT_Comic,0xf8ad06, rotate=0)
label0 = M5TextBox(44, 219, "START", lcd.FONT_Default,0xFFFFFF, rotate=0)
label1 = M5TextBox(136, 219, "STOP", lcd.FONT_Default,0xFFFFFF, rotate=0)
label2 = M5TextBox(223, 219, "CLEAR", lcd.FONT_Default,0xFFFFFF, rotate=0)

import random

textToDisplay = None
size = None

def init():
  global textToDisplay, size
  timerSch.stop('timer1')
  textToDisplay = 'Welcome to the machine...'
  displayText.setText(str(textToDisplay))


def buttonA_wasPressed():
  global textToDisplay, size
  timerSch.run('timer1', 200, 0x00)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global textToDisplay, size
  timerSch.stop('timer1')
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global textToDisplay, size
  init()
  pass
btnC.wasPressed(buttonC_wasPressed)

@timerSch.event('timer1')
def ttimer1():
  global textToDisplay, size
  textToDisplay = (textToDisplay[1 : ] + textToDisplay[ : 1])
  displayText.setText(str(textToDisplay))
  size = random.randint(5, 70)
  circle0.setSize(size)
  pass


init()
size = 50
