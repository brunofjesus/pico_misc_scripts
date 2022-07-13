import machine
import urandom
import utime
import _thread

class Game():
    
    def __init__(self):
        self.playing = False
        self.pressed = False
        self.led = machine.Pin(15, machine.Pin.OUT)
        self.button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.led_waiting = machine.Pin(14, machine.Pin.OUT)
        self.button.irq(trigger=machine.Pin.IRQ_RISING, handler=self.button_handler)
        _thread.start_new_thread(Game.wait, (self,))

    def button_handler(self, pin):        
        if not self.pressed and self.playing:
            self.pressed = True
            self.playing = False
            timer_reaction = utime.ticks_diff(utime.ticks_ms(), self.timer_start)
            print("Your reaction time was " + str(timer_reaction) + " ms!")
            utime.sleep(1)
            print("Click to play again!")
        elif not self.playing:
            self.play()
            
    def play(self):
        self.playing = True
        self.led_waiting.value(0)
        self.led.value(1)
        utime.sleep(urandom.uniform(5,10))
        self.led.value(0)

        self.timer_start = utime.ticks_ms()


    def wait(game):
        while True:
            if not game.playing:
                game.led_waiting.value(1)
                utime.sleep(1)
                game.led_waiting.value(0)
            utime.sleep(0.5)
        

game = Game()


        