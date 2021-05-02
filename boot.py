# This file is executed on every boot (including wake-boot from deepsleep)
import esp, machine
esp.osdebug(None)
#import webrepl
#webrepl.start()

machine.freq(240000000)
