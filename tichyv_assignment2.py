import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

R = 17  # input pin for red color
G = 27  # input pin for green color
B = 22  # input pin for blue color
SIA = 16  # input pin for rotary encoder
SIB = 20  # input pin for rotary encoder
SW = 21  # input pin for button in rotary encoder
s = 0  # inicialize position in color list
color = [0, 0, 0]  # inicialize list of intensitie for each color R-G-B
fr = 100  # frequency for colors

RPi.GPIO.setup(SW, RPi.GPIO.IN)  # setup of encoder button as input
RPi.GPIO.setup(R, RPi.GPIO.OUT)
RPi.GPIO.setup(G, RPi.GPIO.OUT)
RPi.GPIO.setup(B, RPi.GPIO.OUT)  # setup of led pins as outputs
RPi.GPIO.setup(SIA, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_DOWN)
RPi.GPIO.setup(SIB, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_DOWN)  # setup of encoder pins as inputs
state = RPi.GPIO.input(SIA)
RPi.GPIO.setwarnings(False)  # disabling warnings, that should have been mitigated by adding cleanup command at the end of the code

R_pwm = RPi.GPIO.PWM(R, fr)
G_pwm = RPi.GPIO.PWM(G, fr)
B_pwm = RPi.GPIO.PWM(B, fr)  # seting each color variable to PWM instance
R_pwm.start(10)
G_pwm.start(10)
B_pwm.start(10)  # setting the start for each color to 10% to verify the start 

    
def color_change(_):  # function cycling through list of primary colors on pushed button input
    global s
    x = [0, 1, 2]
    s = (s + 1) % len(x)
    print(s)
RPi.GPIO.add_event_detect(SW, RPi.GPIO.FALLING, callback=color_change, bouncetime=20)

def rotary_encoder(_):  # function that adds or substracts 20% of power from currently selected color
    global color
    time.sleep(0.01)
    state = RPi.GPIO.input(SIA)
    if state:
        if RPi.GPIO.input(SIB) == RPi.GPIO.HIGH:
            time.sleep(0.01)
            color[s] += 20
        else:
            color[s] -= 20
    color[s] = min(color[s], 100)
    color[s] = max(color[s], 0)
    print(color[s])
    R_pwm.ChangeDutyCycle(color[0])
    G_pwm.ChangeDutyCycle(color[1])
    B_pwm.ChangeDutyCycle(color[2])
    return
RPi.GPIO.add_event_detect(SIA, RPi.GPIO.FALLING, callback=rotary_encoder, bouncetime=20)

while True:  # infinite while loop to keep program running
    pass
