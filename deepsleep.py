import machine

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
else:
    print('NOT woke from a deep sleep')

# put the device to sleep for 10 seconds
machine.deepsleep(10000)