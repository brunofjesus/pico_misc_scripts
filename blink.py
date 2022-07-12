from machine import Pin
from time import sleep

class SequentialLed():
    ledObjs = [];
    
    def __init__(self, ledPins: list):
        
        for led in ledPins:
            led = Pin(led, Pin.OUT)
            led.value(0)
            self.ledObjs.append(led)
        

            
    def toggle(self, interval :int, reverse: bool):
        
        ledList = self.ledObjs if not reverse else reversed(self.ledObjs)
        
        for led in ledList:
            led.toggle()
            sleep(interval)


button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)


sequentialLed = SequentialLed([13, 14, 15, "LED"])
reverse = False
sequentialLed.toggle(0.2,False)
sequentialLed.toggle(0.2,True)

while True:        
    if (button.value() == 1 and not reverse) or (button.value() == 0 and reverse):
        sequentialLed.toggle(0.2, reverse)
        reverse = not reverse
        sleep(0.5)
