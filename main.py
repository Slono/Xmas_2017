#!/usr/bin/env python
# by Andre Petrov
# credits to Adeept for use of Matrix Keyboard code &
# credits to Adafruit for use of their LCD code

GPIO.setmode(GPIO.BCM) # setting input/output mode to BCM format
def xmasleds(): #defining function for LEDs activation (there are 3 LEDs on board)
    while len(year) < 4 : # another loop to accept 4 digits
    year = int(year) # year becomes integer from string
    if year == 2017: # matching the integer with '2017'
        
    elif year < 2017: # comparing the integer with '2017', if the integer is less than 2017
    elif year > 2017: # comparing the integer with '2017', if the integer is more than 2017
    mylcd.clear() # clearing LCD
    while digit == None: # waiting for an input "0" = break out of loop, "anykey" = continue loop
    if digit == 0: #break out of loop,
        mylcd.message("Good Bye !") # displaying the message
        time.sleep(2) #short delay
        mylcd.clear() # clearing LCD
        sys.exit() # calling exit function from sys module to end the program