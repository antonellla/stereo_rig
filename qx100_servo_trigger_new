

/* 
Takes pictures the camera QX100 and turns on and off 

*/
// REU 2014
// Jordann McCarty.


#include <Servo.h> 
 
Servo powerservo; // create servo object to control turning on and off 
Servo shutterservo; //create serve to control taking pictures      

int shutterSIGPin = 4;
int powerSIGPin = 5;
 
int shutterPressPos  = 0;    // variable to store the servo position 
int shutterDepressPos = 255;
int powerPressPos    = 0; 
int powerDepressPos    = 255; 


//#define DEBUG
 
void setup(){ 
  powerservo.attach(7); 
  shutterservo.attach(9); // attaches the servo on pin 9 to the servo object 
  pinMode(shutterSIGPin, INPUT);
  pinMode(powerSIGPin, INPUT);
} 
 
 
void loop(){ 
  
  if(digitalRead(shutterSIGPin)){
     shutterservo.write(shutterPressPos);
     delay(15);
  } else {
     shutterservo.write(shutterDepressPos);
     delay(15);
  }

  if(digitalRead(powerSIGPin)){
     powerservo.write(powerPressPos);
     delay(15);
  } else {
     powerservo.write(powerDepressPos);
     delay(15);
  }  
 
  #ifndef DEBUG
  //Turn on 
  powerservo.write(powerPressPos);
  delay(15);
  powerservo.write(powerDepressPos);
  delay(150); 
  
  shutterservo.write(shutterPressPos);
  delay(15);
  shutterservo.write(shutterDepressPos);
  delay(15);
  
  #endif

} 
