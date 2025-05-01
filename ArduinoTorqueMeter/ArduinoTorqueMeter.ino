/***************************************************
  This is the sketch for controlling the Torque Meter

  Required libraries:
  - HX711
  - Adafruit_PWMServoDriver
 ****************************************************/


#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <HX711.h>


/****************** GLOBAL PARAMETERS ***************
    These parameters may need to be adjusted for your build
 ****************************************************/
#define PWM_ADDRESS 0x40   // I2C Address of the PWM board
#define SERVO_PIN 0       // Servo pins on the PWM board












#define BAUDRATE 115200   // Serial Baudrate -- Make sure program on computer uses same values
//#define DEBUG
/**** PWM / Servo ****/
#define PWM_INTERNAL_CLOCK 26600000  // Calib MM 2025-05-01 -- The int.osc. for the PCA9685 chip is not very precise. Adjust this value so that the PWM frequency match the SERVO_FREQ
#define SERVO_FREQ 50 // Analog servos run at ~50 Hz updates
#define SERVOMIN 100 // This is the 'minimum' pulse length count (out of 4096) -- Different servos might need different values
#define SERVOMIN_ANGLE 0  // This is the corresponding minimum angle 
#define SERVOMAX 470 // This is the 'maximum' pulse length count (out of 4096)
#define SERVOMAX_ANGLE 180 // this is the corresponding maximum angle
#define ANGLE_BASE 90  // This is the angle at which the device idles
#define ANGLE_MAX 135  // this is the angle at the end of the movements
#define ANGLE_MIN 45  // this is the angle at the other end
#define CYCLE_PERIOD 1000 // duration that the whole cycle should take (in ms)
/*****  load cell *****/
#define CALIBRATION_FACTOR -10880.36  // use CalibTorqueMeter sketch to get this value 
/***** Arduino Pins
    Make sure those match the physical circuit */
#define LOADCELL_DOUT_PIN  3
#define LOADCELL_CLK_PIN  2
#define BTN_PIN 11

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(PWM_ADDRESS, Wire);
HX711 cell;

float angle;
const float angle_rate = float(ANGLE_MAX - ANGLE_MIN) / (CYCLE_PERIOD / 2);

//setup loop to be run once on start up
void setup()
{
  //initialize load cell
  cell.begin(LOADCELL_DOUT_PIN, LOADCELL_CLK_PIN);
  cell.set_scale(CALIBRATION_FACTOR);

  //initialize button
  pinMode(BTN_PIN, INPUT);
  digitalWrite(BTN_PIN, HIGH); //turn on internal pullup

  // initialize servo
  pwm.begin();
  pwm.setOscillatorFrequency(PWM_INTERNAL_CLOCK);
  pwm.setPWMFreq(SERVO_FREQ);


  helloWorld(); // the servo waves to say hi!
  delay(100);
  angle = ANGLE_BASE;
  pwm.setPWM(SERVO_PIN, 0, pwmFromAngle(angle)); //bring servo to its baseline angle and wait for button push

  //initialize serial
  Serial.begin(BAUDRATE); //make sure this matches the data rate set in PLXDAQ!
  Serial.println("ArduinoTorqueMeter sketch");
#ifdef DEBUG
  Serial.print("angle rate is ");
  Serial.println(angle_rate);
#endif
  Serial.println("CLEARDATA");
  Serial.println("LABEL, comp time, angle, Force (g)"); //Set up first row of spreadsheet for label names
  Serial.println("RESETTIMER");

  cell.tare();
}


void loop() {
  if (digitalRead(BTN_PIN)==LOW) {
    moveServoAndReadCell(ANGLE_BASE, ANGLE_MAX, angle_rate);
    moveServoAndReadCell(ANGLE_MAX, ANGLE_MIN, angle_rate);
    moveServoAndReadCell(ANGLE_MIN, ANGLE_BASE, angle_rate);
  }
}

void outputData(float angle, float load) {
  Serial.print("DATA,");
  Serial.print(millis());
  Serial.print(",");
  Serial.print(angle);
  Serial.print(",");
  Serial.println(load);
}

void helloWorld() {
  const int Nrep = 3;
  const float angle_step = 10;
  const int del = 20;
  for (int rep = 0; rep < Nrep; rep++) {
    for (float angle = ANGLE_BASE; angle <= ANGLE_MAX; angle += angle_step) {
      pwm.setPWM(SERVO_PIN, 0, pwmFromAngle(angle));
      delay(del);
    }
    for (float angle = ANGLE_MAX; angle >= ANGLE_MIN; angle -= angle_step) {
      pwm.setPWM(SERVO_PIN, 0, pwmFromAngle(angle));
      delay(del);
    }
    for (float angle = ANGLE_MIN; angle >= ANGLE_BASE; angle -= angle_step) {
      pwm.setPWM(SERVO_PIN, 0, pwmFromAngle(angle));
      delay(del);
    }
  }
}

uint16_t pwmFromAngle(float angle) {
  /* This function takes an angle in degrees and returns
      the corresponding pulse count for the PWM board */
  if (angle <= SERVOMIN_ANGLE) {
    angle = SERVOMIN_ANGLE;
  }
  if (angle >= SERVOMAX_ANGLE) {
    angle = SERVOMAX_ANGLE;
  }
  uint16_t ret = map(angle, SERVOMIN_ANGLE, SERVOMAX_ANGLE, SERVOMIN, SERVOMAX);
#ifdef DEBUG
  Serial.print("pulse count is ");
  Serial.println(ret);
#endif
  return ret;
}

void moveServoAndReadCell(float angle_start, float angle_end, float angle_rate) {
  float load;
  unsigned long currTime = millis(), prevTime = currTime;
  float dt;
  if (angle_start < angle_end) {
    do {
      load = cell.get_units();
      outputData(angle, load);
      prevTime = currTime;
      currTime = millis();
      dt = (currTime - prevTime);
#ifdef DEBUG
      Serial.print("prevTime=");
      Serial.print(prevTime);
      Serial.print(", currTime=");
      Serial.print(currTime);
      Serial.print(", dt=");
      Serial.println(dt);
#endif
      angle += angle_rate * dt;
      pwm.setPWM(SERVO_PIN, 0, pwmFromAngle(angle));
    } while (angle < angle_end);
  } else {
    do {
      load = cell.get_units();
      outputData(angle, load);
      prevTime = currTime;
      currTime = millis();
      dt = (currTime - prevTime);
#ifdef DEBUG
      Serial.print("prevTime=");
      Serial.print(prevTime);
      Serial.print(", currTime=");
      Serial.print(currTime);
      Serial.print(", dt=");
      Serial.println(dt);
#endif
      angle -= angle_rate * dt;
      pwm.setPWM(SERVO_PIN, 0, pwmFromAngle(angle));
    } while (angle > angle_end);
  }
}
