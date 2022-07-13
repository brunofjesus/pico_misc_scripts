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
            
    def toggleNextUp(self):
        for led in self.ledObjs:
            if led.value() == 0:
                led.value(1)
                break
    
    def toggleNextDown(self):
        for led in reversed(self.ledObjs):
            if led.value() == 1:
                led.value(0)
                break
                
    def toggleNext(self, onElseOff :bool):
        if onElseOff:
            self.toggleNextUp()
        else:
            self.toggleNextDown()
        
        


button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)


sequentialLed = SequentialLed(["LED", 15, 14, 13])
sequentialLed.toggle(0.2,False)
sequentialLed.toggle(0.2,True)
idx = 0;

while True:
    idx = sequentialLed.toggleNext(button.value() == 1)
    sleep(0.2)

        
