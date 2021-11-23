#from flask.globals import request
from machine import Pin, I2C
import ssd1306
from time import sleep
import urequests as requests
from utime import localtime, sleep

i2c = I2C(sda=Pin(4),scl=Pin(5))
adc = machine.ADC(0)
display = ssd1306.SSD1306_I2C(128,64, i2c)

display.fill(0)
display.text('HELLO', 40, 0, 1)
display.text('calentando sensor', 0,30,1)
display.text('por favor espere',0,40,1)
display.show()
sleep(30)

led = Pin(2,Pin.OUT)
sensor = Pin(14,Pin.IN)
name="Breathalizer alert"
message = "Fulano esta borracho, dale una mano"
payload = {"name":name,"message":message}

while True:

    if sensor.value() == True:
        display.fill(0)
        time = "12:00"
        display.text(time,30,0,2)
        display.text('Alcohol detectado', 0, 30, 1)
        #display.text(str(adc.read()),0,50,1)
        display.show()
        requests.post("https://crisostomo-app.herokuapp.com/triggers",json=payload)
        sleep(10)
    else:
        display.fill(0)
        time = "12:00"
        display.text(time,30,0,2)
        display.text('Listo para Toma',0,30,1) 
        display.text('de muestra', 20, 40, 1)
        #display.text(str(adc.read()),0,50,1)
        display.show()

