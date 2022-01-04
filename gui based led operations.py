import tkinter as tk
import RPi. GPIO as GPIO
import time
import math
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
root = tk.Tk()

def on():
    GPIO.output(12, True)

def off():
    GPIO.output(12, False)

def Blink():
    for i in range(20):
        GPIO.output(12, True)
        time.sleep(1)
        GPIO.output(12, False)
        time.sleep(1)
    print("end of blink")

def Pwm():
    pwm = GPIO.PWM(12, 100)
    dc = 0
    pwm.start(dc)
    for i in range(100):
        pwm.ChangeDutyCycle(int(math.sin(i/10*math.pi)*10+10))
        time.sleep(0.05)
    print("end of pwm")

button1 = tk.Button(root,text="on",command = on)
button1.pack()
button2 = tk.Button(root,text="off",command = off)
button2.pack()
button3 = tk.Button(root,text="blink",command = Blink)
button3.pack()
button4 = tk.Button(root,text="pwm",command = Pwm)
button4.pack()
button5 = tk.Button(root,text="quit",command = root.destroy)
button5.pack()

root.mainloop()

        
        
    
    