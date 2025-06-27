from machine import Pin, PWM
from time import sleep, ticks_ms, ticks_diff

led_1 = Pin(10, Pin.OUT)
led_2 = Pin(11, Pin.OUT)
led_3 = Pin(12, Pin.OUT)
led_4 = Pin(22, Pin.OUT)
led_pwr = Pin(9, Pin.OUT)

btn_1 = Pin(18, Pin.IN, Pin.PULL_UP)
btn_2 = Pin(19, Pin.IN, Pin.PULL_UP)
btn_3 = Pin(20, Pin.IN, Pin.PULL_UP)
btn_4 = Pin(21, Pin.IN, Pin.PULL_UP)
btn_timer = Pin(13, Pin.IN, Pin.PULL_UP)
timer_modes = [0, 300, 600, 1800, 3600]
timer_mode = 0
time_left =  0
timestamp = ticks_ms()
timer_btn_active = False

flakt_pwr = Pin(17, Pin.OUT)

pwm_pin = Pin(16)
pwm = PWM(pwm_pin)
pwm.freq(2500)

led_pwr.value(1)

def get_duty():
    duty = 0.95
    total_duty = 0
    div = 0
    if not btn_1.value():
        total_duty +=0.85
        div += 1
    if not btn_2.value():
        total_duty +=0.75
        div += 1
    if not btn_3.value():
        total_duty +=0.25
        div += 1
    if not btn_4.value():
        total_duty +=0.1
        div += 1
    if div > 0:
        duty =total_duty/div
    return duty

def update_leds():
    if time_left >timer_modes[0]:
        led_1.value(1)
    else:
        led_1.value(0)
        
    if time_left >timer_modes[1]:
        led_2.value(1)
    else:
        led_2.value(0)
        
    if time_left >timer_modes[2]:
        led_3.value(1)
    else:
        led_3.value(0)
        
    if time_left >timer_modes[3]:
        led_4.value(1)
    else:
        led_4.value(0)

def get_time():
    global timer_mode, time_left, timer_btn_active, timestamp
    if btn_timer.value():
        timer_btn_active = True
    elif timer_btn_active:
        timer_btn_active = False
        timer_mode += 1
        if timer_mode > 4:
            timer_mode = 0
        time_left = timer_modes[timer_mode]
    update_leds()
    if time_left <= 0:
        return False
    else:
        time_left -= ticks_diff(ticks_ms(), timestamp)/1000
        timestamp = ticks_ms()
        return True

while True:
    if get_time():
        flakt_pwr.value(1)
        pwm.duty_u16(round(65535*get_duty()))
    else:
        flakt_pwr.value(0)
        pwm.duty_u16(65535)
    sleep(0.05)
