import RPi.GPIO as GPIO
import time

speed_pin = 18
mla_pin = 23
mlb_pin = 24
angle_pin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(angle_pin, GPIO.OUT)
GPIO.setup(speed_pin, GPIO.OUT)
GPIO.setup(mla_pin, GPIO.OUT)
GPIO.setup(mlb_pin, GPIO.OUT)

pwm1 = GPIO.PWM(speed_pin, 500)
pwm1.start(0)
speed = 0

pwm2 = GPIO.PWM(angle_pin, 100)
angle = 14
pwm2.start(angle)

while True:
    
	cmd = raw_input("command:")
	direction = cmd[0]
	if direction == '2':
		if speed < 100: speed += 50
	elif direction == '8':
		if speed > -100: speed -= 50
	elif direction == '4':
		angle = 11
	elif direction == '5':
		angle = 14
	elif direction == '6':
		angle = 17
	if speed > 0:
		GPIO.output(mla_pin, True)
		GPIO.output(mlb_pin, False)
	else:
		GPIO.output(mla_pin, False)
		GPIO.output(mlb_pin, True)
	if angle < 3:
		angle = 3
	elif angle > 20:
		angle = 20
	print "speed=", speed
	print "angle=", (angle-3)*10
	pwm1.ChangeDutyCycle(abs(speed))
	pwm2.ChangeDutyCycle(angle)
