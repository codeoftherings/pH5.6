#include<Servo.h>

int servoPin=9;
int servoPin2=10;
int inputPin=8;
int angle=0;
Servo servo;
void setup() {
 servo.attach(servoPin);
 servo.attach(servoPin2);
 pinMode(inputPin, INPUT);
}

void loop() {
  if(digitalRead(inputPin)==HIGH)
  {
    for(angle=0;angle<=180;angle++)
    {
      servo.write(angle);
    }
    
  }
    else
   {
    for(angle=180;angle>=0;angle--)
    {
      servo.write(angle);
    }
    
  }

}
