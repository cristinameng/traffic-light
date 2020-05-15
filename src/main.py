from led import Led
from button import Button
from utime import sleep

button_left = Button(23)
button_right = Button(18)
led_green = Led(19)
led_yellow = Led(22)
led_yellow.blink(1000)
led_red = Led(21)

while True:
  first = button_left.state() #sem premir, está em 1. O botão é ativo com 0
  second = button_right.state()

  i = 0
  while i <= 9:
    led_green.on()
    i +=1
    if not first and second: #premir o botão da esquerda apenas
      if i <= 4: #se o led verde estiver aceso por menos de 4s
        sleep(4-i) #deixar verde até completar os 4s e depois passa para amarelo
        led_green.off()
        led_yellow.on()
        sleep(1)
        led_yellow.off()
        led_red.on()
        sleep(5)
        led_red.off()
      if i > 4: #se o led verde estiver aceso por mais de 4s, passa imediatamente para amarelo
        led_green.off()
        led_yellow.on()
        sleep(1)
        led_yellow.off()
        led_red.on()
        sleep(5)
        led_red.off()

    if first and not second: #premir o botão da direita apenas
      while not first and second: #enquanto que o botão não for premido novamente, entra em amarelo intermitente
        led_red.off()
        led_green.off()
        led_yellow.proc()
      led_green.on() #quando é novamente premido, volta ao semáforo normal
      sleep(9)
      led_green.off()
      led_yellow.on()
      sleep(1)
      led_yellow.off()
      led_red.on()
      sleep(5)
      led_red.off()

    else:
      sleep(9)
      led_green.off()
      led_yellow.on()
      sleep(1)
      led_yellow.off()
      led_red.on()
      sleep(5)
      led_red.off()