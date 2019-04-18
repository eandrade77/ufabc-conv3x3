# high chip select means writing, low means reading
# clock is negative edged
import RPi.GPIO as GPIO
from time import time

GPIO.setmode(GPIO.BCM)

data_pins = [16, 26, 20, 21, 5, 6, 13, 12, 4, 17, 27, 22]
clock_pin = 23
chip_select = 24
output = 25

GPIO.setwarnings(False)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(chip_select, GPIO.OUT)
GPIO.setup(output, GPIO.IN)

#Send 12 bits.

GPIO.output(clock_pin, 0)
# set the chip select to write
GPIO.output(chip_select, 1)
# send the bits

GPIO.setup(data_pins, GPIO.OUT)
values=[0,0,0,0,0,0,0,0,0,0,0,0]
GPIO.output(data_pins, values)
raw_input("Press Enter to continue...")
values=[0,1,0,0,0,0,0,0,0,0,0,0]
GPIO.output(data_pins, values)
raw_input("Press Enter to continue...")
values=[0,0,1,0,0,0,0,0,0,0,0,0]
GPIO.output(data_pins, values)
raw_input("Press Enter to continue...")
values=[0,0,0,1,0,0,0,0,0,0,0,0]
GPIO.output(data_pins, values)
raw_input("Press Enter to continue...")
values=[0,0,0,0,1,0,0,0,0,0,0,0]
GPIO.output(data_pins, values)
raw_input("Press Enter to continue...")
values=[0,0,0,0,0,1,0,0,0,0,0,0]
GPIO.output(data_pins, values)
raw_input("Press Enter to continue...")
values=[0,0,0,0,0,0,1,0,0,0,0,0]
GPIO.output(data_pins, values)
raw_input("Press Enter to continue...")
values=[0,0,0,0,0,0,0,1,0,0,0,0]
GPIO.output(data_pins, values)
raw_input("Press Enter to continue...")
values=[0,0,0,0,0,0,0,0,1,0,0,0]
GPIO.output(data_pins, values)
values=[0,0,0,0,0,0,0,0,0,1,0,0]
raw_input("Press Enter to continue...")
GPIO.output(data_pins, values)
raw_input("Press Enter to continue...")
values=[0,0,0,0,0,0,0,0,0,0,1,0]
GPIO.output(data_pins, values)
raw_input("Press Enter to continue...")
values=[0,0,0,0,0,0,0,0,0,0,0,1]
GPIO.output(data_pins, values)
raw_input("Press Enter to continue...")
values=[0,0,0,0,0,0,0,0,0,0,0,0]
GPIO.output(data_pins, values)
raw_input("Press Enter to continue...")
# flash the clock pin
GPIO.output(clock_pin, 1)
GPIO.output(clock_pin, 0)   
raw_input("Press Enter to continue...")

values=[1,1,1,1,1,1,1,1,1,1,1,1]
GPIO.output(data_pins, values)
# flash the clock pin
print("get output = clk = 1")
GPIO.output(clock_pin, 1)
print(GPIO.input(output))
raw_input("Press Enter to continue... clk = 0")   
GPIO.output(clock_pin, 0)
print(GPIO.input(output))


