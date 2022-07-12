from machine import Pin
from time import sleep

ledPins = ["LED", 14, 15]
ledObjs = [];

def initLeds():
    for led in ledPins:
        led = Pin(led, Pin.OUT)
        led.value(0)
        ledObjs.append(led)
        
def toggleLeds(ledList: list, interval :int):
    for led in ledList:
        print(led)
        led.toggle()
        sleep(interval)


initLeds()

while True:
    toggleLeds(ledObjs, 0.2)
    sleep(0.5)
    toggleLeds(reversed(ledObjs), 0.2)
    sleep(2)