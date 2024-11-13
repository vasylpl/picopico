from machine import Pin
from dht import DHT11
import time

# Nastavení DHT11 na pinu GP0
sensor = DHT11(Pin(0))

# Hlavní smyčka
while True:
    try:
        # Čtení hodnot z DHT11
        sensor.measure()
        
        # Získání teploty a vlhkosti
        temperature = sensor.temperature()  # Teplota v °C
        humidity = sensor.humidity()        # Vlhkost v %

        # Výpis naměřených hodnot
        print("++++++++++++++++")
        print("Teplota: {}°C".format(temperature))
        print("Vlhkost: {}%".format(humidity))
        
    except OSError as e:
        print("Chyba při čtení ze senzoru:", e)
    
    # Čekání mezi měřeními (DHT11 vyžaduje pauzu minimálně 2 sekundy)
    time.sleep(0.1)
