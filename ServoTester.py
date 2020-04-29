from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x111111)
servo0 = unit.get(unit.SERVO, unit.PORTA)




title0 = M5Title(title="Servo Tester", x=3 , fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label0 = M5TextBox(20, 50, "Mode : ", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label1 = M5TextBox(20, 90, "Servo Output :", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
txtMode = M5TextBox(110, 50, "Manual", lcd.FONT_DejaVu24,0xf7ff00, rotate=0)
txtServoOut = M5TextBox(205, 90, "90", lcd.FONT_DejaVu24,0xf7ff00, rotate=0)
menuMode = M5TextBox(135, 213, "MODE", lcd.FONT_Default,0xfffc00, rotate=0)
menuMinus = M5TextBox(52, 213, "-10", lcd.FONT_Default,0x00ff3b, rotate=0)
menuPlus = M5TextBox(237, 213, "+10", lcd.FONT_Default,0xff0000, rotate=0)

servoOut = None
mode = None
servoStep = None

def modeManual():
  global servoOut, mode, servoStep
  servo0.write_angle(servoOut)
  wait(0.2)

def modeCenter():
  global servoOut, mode, servoStep
  servoOut = 90
  servo0.write_angle(servoOut)
  wait(0.2)

def modeSweep():
  global servoOut, mode, servoStep
  servoOut = 0
  txtServoOut.setText(str(servoOut))
  servo0.write_angle(servoOut)
  wait(1)
  servoOut = 90
  txtServoOut.setText(str(servoOut))
  servo0.write_angle(servoOut)
  wait(1)
  servoOut = 180
  txtServoOut.setText(str(servoOut))
  servo0.write_angle(servoOut)
  wait(1)
  servoOut = 90
  txtServoOut.setText(str(servoOut))
  servo0.write_angle(servoOut)
  wait(1)


def buttonA_wasPressed():
  global servoOut, mode, servoStep
  menuMinus.setColor(0xffffff)
  wait(0.1)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global servoOut, mode, servoStep
  menuMode.setColor(0xffffff)
  wait(0.1)
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global servoOut, mode, servoStep
  menuPlus.setColor(0xffffff)
  wait(0.1)
  pass
btnC.wasPressed(buttonC_wasPressed)

def buttonA_wasReleased():
  global servoOut, mode, servoStep
  servoOut = servoOut - servoStep
  if servoOut < 0:
    servoOut = 0
  menuMinus.setColor(0x33ff33)
  pass
btnA.wasReleased(buttonA_wasReleased)

def buttonB_wasReleased():
  global servoOut, mode, servoStep
  mode = mode + 1
  if mode > 2:
    mode = 0
  menuMode.setColor(0xffff00)
  pass
btnB.wasReleased(buttonB_wasReleased)

def buttonC_wasReleased():
  global servoOut, mode, servoStep
  servoOut = servoOut + servoStep
  if servoOut > 180:
    servoOut = 180
  menuPlus.setColor(0xff0000)
  pass
btnC.wasReleased(buttonC_wasReleased)


mode = 0
servoOut = 90
servoStep = 10
menuMinus.setColor(0x33ff33)
menuMode.setColor(0xffff00)
menuPlus.setColor(0xff0000)
while True:
  if mode == 0:
    txtMode.setText('Manual')
    txtServoOut.setText(str(servoOut))
    modeManual()
  if mode == 1:
    txtMode.setText('Center')
    txtServoOut.setText(str(servoOut))
    modeCenter()
  if mode == 2:
    txtMode.setText('Sweep')
    modeSweep()
  wait_ms(2)
