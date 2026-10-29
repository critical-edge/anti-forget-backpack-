# config.py - every pin and setting lives here, so changing one never means hunting through files.

# --- I2C (OLED + MPU6050 share these two wires) ---
I2C_SDA = 21
I2C_SCL = 22
OLED_ADDR = 0x3C
MPU_ADDR = 0x68

# --- RC522 RFID (SPI) ---
RFID_SCK = 18
RFID_MOSI = 23
RFID_MISO = 19
RFID_SS = 5      # also called SDA on the module
RFID_RST = 4

# --- Other parts ---
BUZZER_PIN = 13
RESET_BTN_PIN = 14   # button between this pin and GND

# --- Items: name -> card UID (fill in after reading each card) ---
ITEMS = {
    "Laptop": "00000001",
    "ID Card": "00000002",
    "Charger": "00000003",
}

# --- Tuning (calibrate these on the real bag) ---
HOME_RSSI_THRESHOLD = -70      # Wi-Fi signal below this = "outside the home zone" (roughly 5 m)
MOVE_THRESHOLD = 2.5           # m/s^2 away from 9.8 = bag is moving
ALERT_COOLDOWN_S = 30          # seconds between phone notifications
