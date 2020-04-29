from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x222222)
ncir0 = unit.get(unit.NCIR, unit.PORTA)

# Setup the screen
title0 = M5Title(title="Thermometer", x=3 , fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label0 = M5TextBox(3, 100, "Temperature", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label2 = M5TextBox(295, 102, "C", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)
rectangle2 = M5Rect(178, 144, 100, 40, 0x060606, 0x0620fb)
rectangle0 = M5Rect(178, 40, 100, 40, 0x060606, 0xf70404)
scrHigh = M5TextBox(191, 46, "00.00", lcd.FONT_DejaVu24,0xfb0404, rotate=0)
scrLow = M5TextBox(189, 150, "00.00", lcd.FONT_DejaVu24,0x0314f7, rotate=0)
scrTemp = M5TextBox(189, 99, "00.00", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
label1 = M5TextBox(46, 221, "Reset", lcd.FONT_Default,0xffffff, rotate=0)
label3 = M5TextBox(138, 51, "High", lcd.FONT_Default,0xFFFFFF, rotate=0)
label4 = M5TextBox(136, 158, "Low", lcd.FONT_Default,0xFFFFFF, rotate=0)
rectangle1 = M5Rect(178, 93, 100, 40, 0x060606, 0xfffdfd)

# init low/high with max values
Low  =  1000
High = -1000

while True:

  # Button A resets low and high values 
  if btnA.isPressed():
    Low  =  1000
    High = -1000

  # Read temperature  
  Current = ncir0.temperature
  Low     = min(Low, Current)
  High    = max( High, Current)
  
  # Show temperatures  
  scrHigh.setText(str(High))
  scrTemp.setText(str(Current))
  scrLow.setText(str(Low))
  
  wait_ms(250)
  
