import RPi.GPIO as gpio
import time
import os
from flask import Flask, render_template
import smtplib
app=Flask(__name__)
gpio.setmode(gpio.BCM)
ldrpin=21
trig=23
echo=24
led=[27,17,2,03,04]
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.output(x, False)


  
@app.route("/")
def setup1():
    return render_template('start.html')

@app.route("/setup")
def setup1():
    return render_template('setup1.html')

@app.route("/temp")
def temperature():


@app.route("/setup1/<email>")
def setup2(email):
    toAdd=str(email)
    return render_template('setup2.html')

def sendEmail():
    username="saggieb12@gmail.com"
    password="149162536" 
    fromAdd=username
    subject="Full"
    header="To: " + toAdd + "\n" + "From: " + fromAdd + "\n" + "Subject: " + subject
    body="Tank is just about full."
   
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(username, password)
    s.sendmail(fromAdd, toAdd, header + "\n\n" + body)
    s.quit()
    time.sleep(10)


    
@app.route("/phone/<phoneno>")
def setup3(phoneno):
    phone=str(phoneno)
    return render_template('setup3.html')


@app.route("/home")
def home():
    return render_template('home.html')
    GPIO.output(x, False)
    

@app.route("/ldr")
def ldrDisplay():
    reading=0
    gpio.setup(ldrpin,gpio.OUT)
    gpio.output(ldrpin,gpio.LOW)
    time.sleep(0.2)
    gpio.setup(ldrpin,gpio.IN)
    while (gpio.input(ldrpin)==gpio.LOW):
        reading=reading+1
    contamination=reading/42
    contamination=round(contamination,2)

    print("Ph5.6 contamination factor:")
    print (contamination)
    time.sleep(1)
    return str(contamination)

@app.route("/openLid")
def openLid():
    GPIO.output(x, True)
@app.route("/ultrasound")
def ultrasoundDisplay():
   GPIO.output(trig,False)
   time.sleep(.2)
   GPIO.output(trig,True)
   time.sleep(0.00001)
   GPIO.output(trig,False)

   while GPIO.input(echo)==0:
     start=time.time()
   while GPIO.input(echo)==1:
     end=time.time()

   duration=end-start
   cm=duration*17150
   if cm>20:
       cm=20
 
   cm=round(cm,2)
   fill=20-cm
   fillpercent=(fill/20)*100

   if cm<=10.0:

        
         sendEmail()
   

   return fillpercent
   return "%"



if __name__=='__main__':
        app.run(host='0.0.0.0', port=80, debug=True)