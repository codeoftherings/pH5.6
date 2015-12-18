#include<Servo.h>

int servoPin=3;
int servoPin2=9;
int inputPin=8;
int angle=0;
bool isHigh=true;
bool isLow=true;
Servo servo;
Servo servo2;
void setup() {
 servo.attach(servoPin);
 servo2.attach(servoPin2);
 pinMode(inputPin, INPUT);
}

void loop() {
 if(digitalRead(inputPin)==HIGH && isHigh)
  {
    for(angle=60;angle<180;angle++)
    {
      servo.write(angle);
      servo2.write(angle);
     
      delay(15);
    }
    isHigh=false;
    isLow=true;
}
    else if (digitalRead(inputPin)==LOW && isLow))
   {
   for(angle=180;angle>60;angle--)
   {
     servo.write(angle);
     servo2.write(angle);
     delay(15);
    
    }
    isHigh=true;
    isLow=false;
  }

}
