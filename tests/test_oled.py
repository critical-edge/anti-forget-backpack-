# OLED "hello" test. Needs the driver first:  mpremote connect COM6 mip install ssd1306
# Standalone on purpose (no imports from the project), so "Run on ESP32" works on it directly.
from machine import Pin, I2C
import ssd1306

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3C)

oled.fill(0)
oled.text("SMART BAG", 0, 0)
oled.text("OLED works!", 0, 16)
oled.text("[OK] Laptop", 0, 32)
oled.text("[--] ID Card", 0, 44)
oled.show()
