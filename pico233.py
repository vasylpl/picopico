from machine import Pin
import time

# Nastavení pinu pro tlačítko a LED
button = Pin(0, Pin.IN, Pin.PULL_UP)  # Tlačítko na pinu GP0, s vestavěným pull-up rezistorem
led1 = Pin(1, Pin.OUT)               # LED na pinu GP1
led2 = Pin(2, Pin.OUT)               # LED na pinu GP2
led3 = Pin(3, Pin.OUT)               # LED na pinu GP3
led4 = Pin(4, Pin.OUT)               # LED na pinu GP4

# Proměnné pro sledování stisku tlačítka
press_count = 0
last_press_time = 0
leds_on = False  # Stav LED: vypnuto (False) nebo zapnuto (True)

# Časové okno pro dvojité stisknutí (v milisekundách)
double_press_window = 500

def turn_on_all_leds():
    """Rozsvítí všechny LEDky."""
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)

def turn_off_all_leds():
    """Zhasne všechny LEDky."""
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)

# Hlavní smyčka
while True:
    # Kontrola stisknutí tlačítka
    if button.value() == 0:  # Tlačítko je stisknuté (LOW)
        current_time = time.ticks_ms()
        
        # Pokud je první stisk nebo druhý stisk v rámci časového okna
        if press_count == 0 or (current_time - last_press_time) < double_press_window:
            press_count += 1
            last_press_time = current_time

        # Malé zpoždění, aby se zabránilo detekci šumu při stisku tlačítka
        time.sleep(0.1)
        
        # Pokud je dvojité stisknutí detekováno
        if press_count == 2:
            print("Dvojité stisknutí detekováno!")
            
            # Přepínání stavu LED
            if leds_on:
                turn_off_all_leds()  # Pokud byly zapnuté, vypnout
                leds_on = False
                print("LEDky vypnuty.")
            else:
                turn_on_all_leds()  # Pokud byly vypnuté, zapnout
                leds_on = True
                print("LEDky zapnuty.")
            
            press_count = 0  # Resetuje čítač stisknutí

    # Pokud tlačítko nebylo stisknuto znovu v časovém okně, resetuje čítač
    if press_count > 0 and (time.ticks_ms() - last_press_time) > double_press_window:
        press_count = 0

    # Malé zpoždění před dalším čtením
    time.sleep(0.01)
