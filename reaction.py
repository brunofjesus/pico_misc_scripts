import machine
import urandom
import utime

pressed = False
led = machine.Pin(15, machine.Pin.OUT)

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)

def button_handler(pin):
    global pressed
    if not pressed:
        pressed=True
    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    print("Your reaction time was " + str(timer_reaction) + " ms!")
        
led.value(1)
utime.sleep(urandom.uniform(5,10))
led.value(0)

timer_start = utime.ticks_ms()
button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
