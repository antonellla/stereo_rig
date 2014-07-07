

/* 
Turns on the camera QX100

*/
// REU 2014
// Jordann McCarty.

#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
       
 
int pos = 0;    // variable to store the servo position 
 
void setup() 
{ 
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
} 
 
 
void loop() 
{ 
  for(pos = 0; pos < 90; pos += 1)  // goes from 0 degrees to 90 degrees 
  {                                  // in steps of 1 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 

} 
