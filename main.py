from machine import Pin, I2C, SPI
from ssd1306 import SSD1306_I2C
from nrf24 import NRF24L01
import utime
from ds1307 import DS1307
# Pin assignment from Mas6180c: pin 39 = vsys 5v in[red], pin 29/gp22 = led (open = off)[blue], pin 3 = ground[purple],
# pin 21/gp16 pdn (open = off)[orange],  Pin 22/gp17 = data [Brown]
#
# set the datetime 24th March 2018 at 1:45:21 PM
#>>> now = (2018, 3, 24, 6, 13, 45, 21, 0)
#>>> ds.datetime(now)
# set a var for each argument to convert from wwvb 



  # figure out how to set pins you want here: https://docs.micropython.org/en/latest/library/machine.SPI.html

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(1), sda = Pin(0), freq = 40000)

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

oled.fill(0)


oled.text("testhjgjhfgjgfhg",0,0)

oled.show()

radio = nrf24l01.NRF24L01(SPI(1), cs=Pin(15), ce=Pin(16),
                          channel=7, payload_size=32) # cs to SPI0 CSn and ce to generic GPIO



