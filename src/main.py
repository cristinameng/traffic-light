from led import Led
from button import Button
from utime import ticks_ms
from utime import ticks_diff
button_left = Button(23)
button_right = Button(18)
led_green = Led(19)
led_yellow = Led(22)
led_red = Led(21)

def getMaxTime(currentColor):
  if currentColor == led_red:
    return 5000
  elif currentColor == led_yellow:
    return 1000
  elif currentColor == led_green:
    return 9000

def getNextColor(currentColor):
  if currentColor == led_red:
    return led_green
  elif currentColor == led_yellow:
    return led_red
  elif currentColor == led_green:
    return led_yellow



first = button_left.state() #sem premir, está em 1. O botão é ativo com 0
second = button_right.state()

currentColor = led_green
currentColor.on()
last_change_time = ticks_ms()

while True:
  first = button_left.state()
  second = button_right.state()

  if first and not second: #amarelo intermitente
    currentColor.off()
    led_yellow.blink(1000)
    while first: #esperar que o user deixe de pressionar o botao
      first = button_left.state()
  
    while not first:
      led_yellow.proc()
      first = button_left.state()
    
    led_yellow.off()
    currentColor.on()
    last_change_time = ticks_ms()
    while first:  #esperar que o user deixe de pressionar o botao
      first = button_left.state()
  
  first = button_left.state()
  second = button_right.state()
  print(second)

  if second:
    print("ENTERED IF")
    if ticks_diff(ticks_ms(),last_change_time) < 4000:
      print("SMALL")
      while ticks_diff(ticks_ms(),last_change_time) < 4000:
        print("oi")
      currentColor.off()
      currentColor = led_green
      currentColor.on()
      last_change_time = ticks_ms()
    else:
      print("HUGE - BIG")
      currentColor.off()
      currentColor = led_green
      currentColor.on()
      last_change_time = ticks_ms()
  
  if ticks_diff(ticks_ms(),last_change_time) >= getMaxTime(currentColor):
    currentColor.off()
    currentColor = getNextColor(currentColor)
    currentColor.on()
    last_change_time = ticks_ms()
  
  
  