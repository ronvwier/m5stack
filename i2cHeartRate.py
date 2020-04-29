from m5stack import *
from m5ui import *
from uiflow import *
import i2c_bus

setScreenColor(0x222222)




devicesList = M5TextBox(1, 81, "Devices on I2C bus", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
title0 = M5Title(title="Devices on I2C bus", x=3 , fgcolor=0xFFFFFF, bgcolor=0x0000FF)
statusLabel = M5TextBox(0, 44, "?", lcd.FONT_DejaVu18,0xFFFFFF, rotate=0)

lijst = None



i2c0 = i2c_bus.easyI2C(i2c_bus.PORTA, 0x5C)
statusLabel.setText('Port open')
lijst = i2c0.scan()
devicesList.setText(str(lijst))
