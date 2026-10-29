# Blink test. Run with the "Run on ESP32" tool. Stop with Ctrl+C.
from machine import Pin
import time

led = Pin(2, Pin.OUT)   # on-board LED on most ESP32 DevKits
while True:
    led.value(not led.value())
    time.sleep(0.5)
