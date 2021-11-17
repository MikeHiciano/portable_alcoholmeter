#from flask.globals import request
from machine import Pin, I2C
import ssd1306
from time import sleep
import urequests as requests

i2c = I2C(sda=Pin(4),scl=Pin(5))
display = ssd1306.SSD1306_I2C(128,64, i2c)

display.fill(0)
display.text('HELLO', 40, 0, 1)
display.show()

led = Pin(2,Pin.OUT)
sensor = Pin(14,Pin.IN,Pin.PULL_UP)
name="Breathalizer alert"
message = "Fulano esta borracho, dale una mano"
payload = {"name":name,"message":message}

while True:
    if sensor.value() == True:
        display.fill(0)
        display.text('U R Drunk dude!', 0, 0, 1)
        display.show()
        requests.post("https://crisostomo-app.herokuapp.com/triggers",json=payload)
        sleep(10)
    else:
        display.fill(0)
        display.text('ur gud tu go!', 0, 0, 1)
        display.show()

