import machine
import time

uart=machine.UART(1,tx=17,rx=16,baudrate=9600)

end_cmd=b'\xFF\xFF\xFF'

def send(cmd):
    uart.write(cmd)
    uart.write(end_cmd)
    time.sleep_ms(100)
    response = uart.read()
    print("Command:",cmd,"Response:", response)

send('page start')
send('banner.txt="het is gelukt, hello Nextion world"')
send('get dp')
send('page last')
send('banner.txt="het is gelukt, hello Nextion world"')
send('get dp')
send('sendme')
send('get "Returned string"')
send('sleep=1')
send('get start.banner.txt')
send('sleep=0')
send('dim=100')



