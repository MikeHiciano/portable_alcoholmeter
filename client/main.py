from machine import Pin, I2C
import ssd1306
# import progress_bar
from time import sleep
import urequests as requests
from utime import localtime, sleep

i2c = I2C(-1,sda=Pin(4),scl=Pin(5))
adc = machine.ADC(0)
display = ssd1306.SSD1306_I2C(128,64, i2c)

# infinte_bar = progress_bar.ProgressBar(10, 40, display.width - 20, 15, display)

counter = 0
time = "00:00"

display.fill(0)
display.text('HELLO', 40, 0, 1)
display.text('calentando sensor', 0,30,1)
display.text('por favor espere',0,40,1)
display.show()
sleep(3)

led = Pin(2,Pin.OUT)
sensor = Pin(14,Pin.IN)
name="Breathalizer alert"
message = "Fulano esta borracho, dale una mano"
payload = {"name":name,"message":message}

while True:
    
    # infinite_bar.update()
    counter = counter+1
    if counter == 60:
        timestamp = requests.get("http://worldtimeapi.org/api/timezone/America/Santo_Domingo").json()
        time = timestamp['datetime'][11:16]
        counter = 0

    #if sensor.value() == True:
    if adc.read() > 140 and adc.read() < 160: #and adc.read() < 100:
        display.fill(0)
        display.text(time,30,0,2)
        display.text('lectura normal', 0, 30, 1)
        #display.text(str(adc.read()),0,50,1)
        display.show()
        #requests.post("https://crisostomo-app.herokuapp.com/triggers",json=payload)
        sleep(3)

    elif adc.read() > 161: #and adc.read() < 100:
        display.fill(0)
        display.text(time,30,0,2)
        display.text('Esta bajo los efectos', 0, 30, 1)
        display.text('Del alcohol', 0, 40, 1)
        display.text('Se recomienda NO', 0, 50, 1)
        display.text('CONDUCIR', 0, 30, 1)
        #display.text(str(adc.read()),0,50,1)
        display.show()
        #requests.post("https://crisostomo-app.herokuapp.com/triggers",json=payload)
        sleep(10)

    elif adc.read() > 200: #and adc.read() < 100:
        display.fill(0)
        #time = "12:00"
        display.text(time,30,0,2)
        display.text('Estas ebrio', 0, 30, 1)
        #display.text(str(adc.read()),0,50,1)
        display.show()
        requests.post("https://crisostomo-app.herokuapp.com/triggers",json=payload)
        sleep(10)

    else:
        display.fill(0)
        display.text(time,30,0,2)
        display.text('Listo para Toma',0,30,1) 
        display.text('de muestra', 20, 40, 1)
        display.text(str(adc.read()),0,50,1)
        display.show()

