from microbit import *
import random
import gc

#G=Green leds => 47 Ohm => Digital 12
#O=Orange leds => 47 Ohm => Digital 16
#R=Red leds => 47 Ohm => Digital 8
#A=RGB led => Red pin:Analog 0, Green pin:Analog 1, Blue pin:Analog 2, Common=>47 Ohm=>Ground

#G---R
#-O---
#--A--
#---O-
#R---G

greeting = [Image.HEART, Image.HEART, Image.HEART, "X", "X", "X", "-", "-", "M", "A", "S", " ", " ",
            Image.XMAS, Image.XMAS, " ", Image.XMAS, Image.XMAS, " ", Image.XMAS, Image.XMAS, " ", Image.XMAS, Image.XMAS, " "]

debug = 1

def light(red=0, green=0, orange=0):
    #RESET the center RGB led
    pin0.write_analog(0)
    pin1.write_analog(0)
    pin2.write_analog(0)
    
    if (red):
        pin8.write_digital(1)
        pin0.write_analog(150)
        if (debug): print("RED")
    else:
        pin8.write_digital(0)
        pin0.write_analog(0)
    if (green):
        pin12.write_digital(1)
        pin1.write_analog(50)
        if (debug): print("GREEN")
    else:
        pin12.write_digital(0)
        pin1.write_analog(0)
    if (orange):
        pin16.write_digital(1)
        if (debug): print("ORANGE")
    else:
        pin16.write_digital(0)
        
    if (not (green or red or orange)):
        pin2.write_analog(200)
        
        
loop_counter = 0
loop_stop = 50
greeting_counter = 0
greeting_length = len(greeting)
reset_counter = 0
green = 0
red = 0
orange = 0
while True:
    loop_counter += 1
    if button_a.is_pressed() or button_b.is_pressed():
        if (debug): print("Button pressed")
        break
    elif (loop_counter == loop_stop):
        #Generate random colors
        green=random.randint(0,1)
        red=random.randint(0,1)
        orange=random.randint(0,1)
        
        #Light them up
        light(red, green, orange)
        #Increment counter for greeting list
        greeting_counter += 1
        if (greeting_counter >= greeting_length):
            greeting_counter = 0
        #Display greeting
        display.show(greeting[greeting_counter])
        
    else:
        sleep(10)
        if (gc.mem_free()<1000):
            gc.collect()

        
    if (loop_counter > loop_stop):
        loop_counter=0
        gc.collect()
        if (debug):
            reset_counter += 1
            print("Reset counter : %d" % reset_counter)
            print("Free mem  : {}  -  Allocated mem : {}".format(gc.mem_free(), gc.mem_alloc()))
        
if (debug): print("Shutting down")
light(0,0,0)
pin2.write_analog(0)
display.clear()

