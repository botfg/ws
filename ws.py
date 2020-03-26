import neopixel
import board
from time import sleep
from RPi import GPIO
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

pixels = neopixel.NeoPixel(board.D18, 30, auto_write=True, pixel_order=neopixel.RGB)


def end():
    pixels.fill((0,0,0))

def test2():
    colors = [(0, 0, 255),(0, 255, 0),(255, 0, 0),(255, 255, 255),(255, 0, 255),(75, 0, 130),(255, 69, 0),(128, 0, 128),(47, 79, 79)]
    #colors =[(255, 0, 0),(0, 0, 255),(0, 255, 0),(0, 255, 255)]
    sl = (0.1, 0.2, 0.3, 0.4)
    while True:
        for j in colors:
            for i in range(30):
                if GPIO.input(12) == GPIO.LOW:
                    end()
                    sleep(0.3)
                    main()
                pixels[i] = j
                sleep(0.02)
                if GPIO.input(12) == GPIO.LOW:
                    end()
                    sleep(0.3)
                    main()
            for i in sl:
                if GPIO.input(12) == GPIO.LOW:
                    end()
                    sleep(0.3)
                    main()
                sleep(i)


def test3():
    pixels.fill((0,150,0))



            
def main():
    try:
        while True:
            key_b = GPIO.input(12)
            if key_b == GPIO.LOW:
                sleep(0.3)
                test2()
    except KeyboardInterrupt:
        end()
        GPIO.cleanup()
        sys.exit()
    finally:
        end()
        GPIO.cleanup()

main()
