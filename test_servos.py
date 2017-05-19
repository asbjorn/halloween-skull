"""
Test code to control a servo on GPIO pin 18 (PWM pin).
"""

import wiringpi
import time

# Use GPIO naming
wiringpi.wiringPiSetupGpio()

# PINS
servoPin = 18

# set #servoPin to be a PWM output
wiringpi.pinMode(servoPin, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to ms stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)


wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01

while True:
    for pulse in range(50, 250):
        wiringpi.pwmWrite(servoPin, pulse)
        time.sleep(delay_period)

    for pulse in range(250, 50, -1):
        wiringpi.pwmWrite(servoPin, pulse)
        time.sleep(delay_period)
