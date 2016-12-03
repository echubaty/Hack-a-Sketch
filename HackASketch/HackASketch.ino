/*
  ReadAnalogVoltage
  Reads an analog input on pin 0, converts it to voltage, and prints the result to the serial monitor.
  Graphical representation is available using serial plotter (Tools > Serial Plotter menu)
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.
*/

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(57600);
   // analogReference(EXTERNAL);

  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  delay(250);
  // read the input on analog pin 0:
  int x = analogRead(A0);
   delay(1); 
    int y = analogRead(A1);
       delay(1);
    int z = analogRead(A1);
       delay(1);
  float zero_G = 512.0; //ADC is 0~1023 the zero g output equal to Vs/2
  //ADXL335 power supply by Vs 3.3V
  float scale = 102.3; //ADXL335330 Sensitivity is 330mv/g

 Serial.print(x);
 // Serial.print(((float)x - zero_G)/scale);
  Serial.print("\t");
 // Serial.print(((float)y - zero_G)/scale);
    Serial.print(y);
    Serial.print("\t");
  Serial.print(((float)z - zero_G)/scale);
  Serial.print("\n");
}

