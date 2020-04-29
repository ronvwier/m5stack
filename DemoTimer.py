from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x222222)




title0 = M5Title(title="Timer Begin", x=130 , fgcolor=0xFFFFFF, bgcolor=0x3434ae)
label0 = M5TextBox(0, 50, "Timer1:", lcd.FONT_Default,0xFFFFFF, rotate=0)
label1 = M5TextBox(70, 50, "0", lcd.FONT_Default,0xFFFFFF, rotate=0)
label2 = M5TextBox(0, 100, "Timer2:", lcd.FONT_Default,0xFFFFFF, rotate=0)
label3 = M5TextBox(69, 99, "0", lcd.FONT_Default,0xFFFFFF, rotate=0)

COUNT = None
COUNT2 = None


def buttonA_wasPressed():
  global COUNT, COUNT2
  timerSch.stop('timer1')
  timerSch.stop('timer2')
  title0.setTitle('Stop')
  pass
btnA.wasPressed(buttonA_wasPressed)

@timerSch.event('timer1')
def ttimer1():
  global COUNT, COUNT2
  COUNT = (COUNT if isinstance(COUNT, int) else 0) + 1
  rgb.setColorFrom(6 , 10 ,0xff0000)
  label1.setText(str(COUNT))
  rgb.setColorFrom(6 , 10 ,0x000000)
  pass

@timerSch.event('timer2')
def ttimer2():
  global COUNT, COUNT2
  COUNT2 = (COUNT2 if isinstance(COUNT2, int) else 0) + 1
  rgb.setColorFrom(1 , 5 ,0x33ff33)
  label3.setText(str(COUNT2))
  rgb.setColorFrom(1 , 5 ,0x000000)
  pass

@timerSch.event('timer3')
def ttimer3():
  global COUNT, COUNT2
  speaker.tone(1800, 200)
  pass


timerSch.run('timer3', 3000, 0x01)
timerSch.run('timer1', 1000, 0x00)
timerSch.run('timer2', 2000, 0x00)
COUNT = 0
COUNT2 = 0
