import RPi.GPIO as GPIO
import time
import os, glob, time
from flask import Flask, render_template
import smtplib
app=Flask(__name__)
GPIO.setmode(GPIO.BCM)
ldrpin=21
trig=23
echo=24
linkitLink=15
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.setup(linkitLink, GPIO.OUT)
GPIO.output(linkitLink, False)
toAdd=str(raw_input('add email'))
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

  
@app.route("/")
def setup1():
    return render_template('start.html')



@app.route("/temp")
def temperature():
    return render_template('temp.html', tempRead=read_temp())
    



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


    


@app.route("/home")
def home():
    return render_template('home.html')
    GPIO.output(linkitLink, False)
    

@app.route("/ldr")
def ldrDisplay():
    reading=0
    GPIO.setup(ldrpin,GPIO.OUT)
    GPIO.output(ldrpin,GPIO.LOW)
    time.sleep(0.2)
    GPIO.setup(ldrpin,GPIO.IN)
    while (GPIO.input(ldrpin)==GPIO.LOW):
        reading=reading+1
    contamination=reading/42
    contamination=round(contamination,2)

    print("Ph5.6 contamination factor:")
    print (contamination)
    time.sleep(1)
    return render_template('ldr.html', ldr=contamination)

@app.route("/openLid")
def openLid():
    GPIO.output(linkitLink, True)
    return render_template('home_lid_open.html');
    
    
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
   if cm>10:
       cm=10
 
   cm=round(cm,2)
   fill=10-cm
   fillpercent=(fill/10)*100
   fillpercent=round(fillpercent, 2)
   if cm<=10.0:

        
         sendEmail()
   

   return render_template('us.html', ultrasound=fillpercent)


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

if __name__=='__main__':
        app.run(host='0.0.0.0', port=80,debug=True)
