# I2C scanner. Expect 0x3c (OLED) and 0x68 (MPU6050). An empty list means a wiring problem.
from machine import Pin, I2C

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
print([hex(a) for a in i2c.scan()])
