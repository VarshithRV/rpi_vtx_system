// Sketch to convert the pwm signals of two channels to digital
// Current config
// channel6 -> io2
// channel7 -> io4 (IO4 is also connected to the internal flashlight)

const int pwmPin1 = 12; // PWM channel 1
const int digitalout1=4; // Digital out corresponding to pwm channel 1
const int pwmPin2 = 13; // PWM channel 2
const int digitalout2=2;// Digital out corresponding to pwm channel 2

void setup() {
 Serial.begin(115200);
 pinMode(digitalout1,OUTPUT);
 pinMode(digitalout2,OUTPUT);
}

void loop() {
 long duration1 = pulseIn(pwmPin1, HIGH); // Measure the duration of the HIGH pulse
 long duration2 = pulseIn(pwmPin2, HIGH); // Measure the duration of the HIGH pulse
 int pwmValue1 = duration1 * 100 / 20000; // Calculate the PWM value (0 to 100)
 int pwmValue2 = duration2 * 100 / 20000; // Calculate the PWM value (0 to 100)
 if (pwmValue1<6)
 {
    digitalWrite(digitalout1,HIGH);
 }
 else
 {
    digitalWrite(digitalout1,LOW);         
 }

 if (pwmValue2<6)
 {
    digitalWrite(digitalout2,HIGH);
 }
 else
 {
    digitalWrite(digitalout2,LOW);         
 } 
 Serial.println(pwmValue1); // Print the PWM value to the Serial Monitor
 delay(10); // Wait for 100 milliseconds
}
