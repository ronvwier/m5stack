from m5stack import *
from m5ui import *
from uiflow import *
import espnow
import wifiCfg

setScreenColor(0x222222)



wifiCfg.wlan_ap.active(True)
espnow.init()
title0 = M5Title(title="Title", x=3 , fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label0 = M5TextBox(108, 117, "Text", lcd.FONT_DejaVu40,0xFFFFFF, rotate=0)

send_flag = None
sender_address = None
receive_data = None



def send_cb(flag):
  global send_flag,sender_address,receive_data
  send_flag = flag
  if send_flag:
    label0.setText('succeed')
  else:
    label0.setText('Failed')

  pass
espnow.send_cb(send_cb)



def recv_cb(_):
  global send_flag,sender_address,receive_data
  sender_address, _, receive_data = espnow.recv_data(encoder='str')
  if receive_data == 'on':
    rgb.setColorAll(0x33cc00)
  if receive_data == 'off':
    rgb.setColorAll(0x000000)
  label0.setText(str(receive_data))

  pass
espnow.recv_cb(recv_cb)


def buttonA_wasPressed():
  global send_flag, sender_address, receive_data
  label0.setText('sending on')
  espnow.broadcast(data=str('on'))
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonB_wasPressed():
  global send_flag, sender_address, receive_data
  label0.setText('sending off')
  espnow.broadcast(data=str('off'))
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global send_flag, sender_address, receive_data
  label0.setText('broadcasting')
  espnow.broadcast(data=str('Broadcast'))
  pass
btnC.wasPressed(buttonC_wasPressed)


#the Master
title0.setTitle(str(espnow.get_mac_addr()))
