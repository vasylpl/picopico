from machine import Pin
from dht import DHT11
import time

sensor = DHT11(Pin(0))

led1 = Pin(1, Pin.OUT)  # LED pro 21 °C
led2 = Pin(2, Pin.OUT)  # LED pro 22 °C
led3 = Pin(3, Pin.OUT)  # LED pro 23 °C
led4 = Pin(4, Pin.OUT)  # LED pro 24 °C


while True:
    try:
        
        sensor.measure()
        
        temperature = sensor.temperature()  

        print("++++++++++++++++")
        print("Teplota: {}°C".format(temperature))
        
        led1.value(1 if temperature >= 21 else 0)
        led2.value(1 if temperature >= 22 else 0)
        led3.value(1 if temperature >= 23 else 0)
        led4.value(1 if temperature >= 24 else 0)
        
    except OSError as e:
        print("Chyba při čtení ze senzoru:", e)
    
    time.sleep(2)
