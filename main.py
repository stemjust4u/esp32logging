'''
https://github.com/peterhinch
'''
import ulogging, micropython
import utime
from machine import Pin, ADC, PWM
import gc
gc.collect()
micropython.alloc_emergency_exception_buf(100)

'''
CRITICAL = 50
ERROR    = 40
WARNING  = 30
INFO     = 20
DEBUG    = 10
NOTSET   = 0
'''
a = "test"

ulogging.basicConfig(level=10)

ulogging.info('root logger info: {0}'.format(a))
ulogging.debug('root logger debugging')

logger_timed = ulogging.getLogger(__name__)
logger_timed.setLevel(10)
logger_timed.info('logger info: {0}'.format(a))
logger_timed.debug('logger debug')

def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = utime.ticks_us()
        result = f(*args, **kwargs)
        delta = utime.ticks_diff(utime.ticks_us(), t)
        logger_timed.debug('Function {} time = {:6.3f}ms'.format(myname, delta/1000))
        return result
    return new_func

@timed_function
def integer(n):
    for i in range(n):
        x = 1 + 1

@timed_function
def float(n):
    for i in range(n):
        x = 1.5 + 1.5

@timed_function
def getpinvalue(pin):
    return pin.value()

@timed_function
def setpinvalue(pin, value):
    pin.value(value)

@timed_function
def set_4_pins(pins, value):
    for pin in pins:
        pin.value(value)

@timed_function
def get_4_pins_list(pins, outgoing):
    outgoing[0] = pins[0].value()
    outgoing[1] = pins[1].value()
    outgoing[2] = pins[2].value()
    outgoing[3] = pins[3].value()
    return outgoing

@timed_function
def get_4_pins_list_loop(pins, outgoing):
    for i, pin in enumerate(pins):
        outgoing[i] = pin.value()
    return outgoing

@timed_function
def get_4_pins_dict(pins, outgoing):
    outgoing['0'] = pins[0].value()
    outgoing['1'] = pins[1].value()
    outgoing['2'] = pins[2].value()
    outgoing['3'] = pins[3].value()
    return outgoing

@timed_function
def getADC(pin):
    return pin.read()

@timed_function
def getADC_4pins(pins, outgoing):
    outgoing[0] = pins[0].read()
    outgoing[1] = pins[1].read()
    outgoing[2] = pins[2].read()
    outgoing[3] = pins[3].read()
    return outgoing

@timed_function
def setPWM(pin):
    pin.duty(75)  

n=10
integer(n)
ulogging.debug('ran {0} times'.format(n))

float(n)
ulogging.debug('ran {0} times'.format(n))

pinlist = [5, 4, 2, 16]
io_pin = [0]*len(pinlist)
for i, pin in enumerate(pinlist):
    io_pin[i] = Pin(pin, Pin.OUT) # 2 is the internal LED

set_4_pins(io_pin, 0)

pin = 32
adc = ADC(Pin(pin))
adc.atten(ADC.ATTN_11DB)

pin = 23
pwm = PWM(Pin(pin), 50)

onoff = getpinvalue(io_pin[2])
ulogging.debug(onoff)
setpinvalue(io_pin[2], 1)
utime.sleep_ms(1000)
setpinvalue(io_pin[2], 0)

outgoing = [0]*len(pinlist)
data = get_4_pins_list(io_pin, outgoing)
ulogging.debug(data)

data = get_4_pins_list_loop(io_pin, outgoing)
ulogging.debug(data)

adcpins = [32, 33, 34, 35]
adc_pin = [0]*len(adcpins)
for i, pin in enumerate(adcpins):
    adc_pin[i] = ADC(Pin(pin))
    adc_pin[i].atten(ADC.ATTN_11DB)
adcdata = getADC_4pins(adc_pin, outgoing)
ulogging.debug(adcdata)

outgoing = {}
data = get_4_pins_dict(io_pin, outgoing)
ulogging.debug(data)

adcvalue = getADC(adc)



setPWM(pwm)
