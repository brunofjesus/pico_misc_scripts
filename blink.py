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


button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)


sequentialLed = SequentialLed(["LED", 14, 15])
reverse = False

while True:
    if button.value() == 1:
        sequentialLed.toggle(0.2, reverse)
        reverse = not reverse
        sleep(0.5)
