from m5stack import *
from m5ui import *
from uiflow import *
import unit

setScreenColor(0x111111)
neopixel0 = unit.get(unit.NEOPIXEL, unit.PORTC, 15)




circle0 = M5Circle(95, 90, 15, 0xFFFFFF, 0xFFFFFF)
circle1 = M5Circle(221, 90, 15, 0xFFFFFF, 0xFFFFFF)

import random

R = None
G = None
B = None
i = None



while True:
  R = random.randint(0, 255)
  G = random.randint(0, 255)
  B = random.randint(0, 255)
  for i in range(1, 16):
    neopixel0.setColorFrom(1,i,(R << 16) | (G << 8) | B)
    wait(0.005)
  for i in range(1, 16):
    neopixel0.setColorFrom(1, i, 0x000000)
    wait(0.005)
  wait_ms(2)
