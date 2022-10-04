/***************************************************
  This sketch is used to test the Torque Meter
  and calibrate the load cell readings.
  Usage: 
   - Upload sketch from the Arduino IDE
   - Open serial monitor and follow the instructions
     on the screen.
   - Once the calibration factor has been determined,
     update the value in the `ArduinoTorqueMeter` sketch
     and upload that sketch back to the Torque Meter
          

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
#define BAUDRATE 115200   // Serial Baudrate -- Make sure program on computer uses same values
#define PRINT_PERIOD 1000 // refresh rate of the values read from the load cell (in ms)
//#define DEBUG
/**** PWM / Servo ****/
#define PWM_INTERNAL_CLOCK 26500000  // The int.osc. for the PCA9685 chip is not very precise. Adjust this value so that the PWM frequency match the SERVO_FREQ
#define SERVO_FREQ 50 // Analog servos run at ~50 Hz updates
#define SERVOMIN 100 // This is the 'minimum' pulse length count (out of 4096) -- Different servos might need different values
#define SERVOMIN_ANGLE 0  // This is the corresponding minimum angle 
#define SERVOMAX 470 // This is the 'maximum' pulse length count (out of 4096)
#define SERVOMAX_ANGLE 180 // this is the corresponding maximum angle
#define ANGLE_BASE 135  // This is the angle at which the device idles
#define ANGLE_MAX 180  // this is the angle at the end of the movements
#define ANGLE_MIN 100  // this is the angle at the other end
#define CYCLE_PERIOD 1000 // duration that the whole cycle should take (in ms)
/*****  load cell *****/
#define CALIBRATION_FACTOR -13566.24  // use CalibTorqueMeter sketch to get this value 
/***** Arduino Pins
    Make sure those match the physical circuit */
#define LOADCELL_DOUT_PIN  3
#define LOADCELL_CLK_PIN  2
#define BTN_PIN 11
#define SERVO_PIN 0 // Servo pins on the PWM board

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40, Wire);
HX711 cell;

unsigned long prevTime = 0;



//setup loop to be run once on start up
void setup()
{
  //initialize load cell
  cell.begin(LOADCELL_DOUT_PIN, LOADCELL_CLK_PIN);
  cell.set_offset(0.0);
  cell.set_scale(1.0);

  //initialize button
  pinMode(BTN_PIN, INPUT);     //define pin as input to arduino
  digitalWrite(BTN_PIN, HIGH); //turn on internal pullup

  // initialize servo
  pwm.begin();
  pwm.setOscillatorFrequency(PWM_INTERNAL_CLOCK);
  pwm.setPWMFreq(SERVO_FREQ);
  pwm.setPWM(SERVO_PIN, 0, pwmFromAngle(ANGLE_BASE)); //bring servo to its baseline angle and wait

  //initialize serial
  Serial.begin(BAUDRATE); //make sure this matches the data rate set in PLXDAQ!
  Serial.println("#################### LOAD CELL CALIBRATION PROCEDURE ####################");
  Serial.println();
  Serial.println("Send commands through the serial monitor in the Arduino IDE:");
  printCommandSummary();
  Serial.println();
  Serial.println();
  Serial.println("GENERAL PROCEDURE:");
  Serial.println("(1) flip the device perpendicular to the table so as to be able to suspend a weight to the arm.");
  Serial.println("    You may need to place it at the edge of the  table so that the weight can hand freely.");
  Serial.println("(2) With no weight attached, move the arm (M<angle>) so that the arm is parallel to the table.");
  Serial.println("    The weight should be perpendicular to the arm direction.");
  Serial.println("(3) Still with no weight attached, tare the device. the readings should indicated 0g");
  Serial.println("(4) Suspend a known weight to the arm, observe the new readings");
  Serial.println("(5) Provide the value of the weight (W<weight>). The system calculates the correct scaling");
  Serial.println("    and applies it. The readings should match the weight at this point.");
  Serial.println("    Be careful not to exceed the weight rating of the load cell.");
  Serial.println("# Offset | Scaling factor | Raw reading | Weight (g)");
}

void loop() {
  if (Serial.available() > 0) {
    String in = Serial.readStringUntil('\n');
    in.toUpperCase();
    char cmd = in[0];
    float val = in.substring(1).toFloat();
    switch (cmd) {
      case 'T':
        Serial.println("Taring...");
        cell.tare();
        break;
      case 'M':
        Serial.print("Moving to angle=");
        Serial.println(val);
        pwm.setPWM(SERVO_PIN, 0, pwmFromAngle(val));
        delay(200);
        break;
      case 'O':
        Serial.println("Changing offset");
        cell.set_offset(val);
        break;
      case 'S':
        Serial.println("Changing the scaling factor");
        cell.set_scale(val);
        break;
      case 'W':
        long offset = cell.get_offset();
        long raw = cell.read_average(10);
        float newScale = (raw - offset) / val;
        cell.set_scale(newScale);
        Serial.print("Raw reading is [");
        Serial.print(raw);
        Serial.print("] for a weight of [");
        Serial.print(val);
        Serial.print("], use CALIBRATION_FACTOR= ");
        Serial.print(newScale);
        Serial.println(" in ArduinoTorqueMeter!");
        break;
      default:
        Serial.println("Unknown command, please try again. Available commands are:");
        printCommandSummary();
        break;
    }
  }
  unsigned long curTime = millis();
  if (curTime - prevTime > PRINT_PERIOD) {
    printReadings();
    prevTime = curTime;
  }
}

void printReadings() {
  const int Navg = 10;
  float scale = cell.get_scale();
  long offset = cell.get_offset();
  long raw = cell.read_average(Navg);
  float reading = cell.get_units(Navg);
  Serial.print(offset);
  Serial.print(" | ");
  Serial.print(scale);
  Serial.print(" | ");
  Serial.print(raw);
  Serial.print(" | ");
  Serial.print(reading);
  Serial.println();
}

void printCommandSummary() {
  Serial.println(" - T");
  Serial.println("   Tares the load cell. Sets the offset so that the current reading becomes zero");
  Serial.println(" - M<angle (deg)>");
  Serial.println("   Moves to the specified angle (between 0 and 180 deg)");
  Serial.println(" - O<Offset>");
  Serial.println("   Sets the offset. Warning: will untare the device.");
  Serial.println(" - S<scale>");
  Serial.println("   Sets the scaling factor");
  Serial.println(" - W<weight (g)>");
  Serial.println("   Provides the weight of the object attached to the arm at that moment for automatic scaling");
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
