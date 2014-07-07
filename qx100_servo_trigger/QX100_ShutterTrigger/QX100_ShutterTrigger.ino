

/* 
Turns on the camera QX100

*/
// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.


#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
       
 
int pos = 0;    // variable to store the servo position 
 
void setup() 
{ 
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object 
} 
 
 
void loop() 
{ 
  for(pos = 0; pos < 10; pos += 1)  // goes from 0 degrees to 10 degrees 
  {                                  // in steps of 1 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(15);                       // waits 15ms for the servo to reach the position 
  } 
  for(pos = 20; pos>=1; pos -=1)  // goes from 20 degrees to 0 degrees 
 {
  myservo.write(pos);             // tell servo to go to position in variable 'pos'
 delay(15);                       // wait 15ms for the servo to reach the desired postion
 } 

} 
  
  


