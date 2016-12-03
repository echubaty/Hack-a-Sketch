const int accelX = A0;
const int accelY = A1;
const int accelZ = A2;
const int lPot = A8;
const int rPot = A9;

const float VOLT_REF = 3.3 / 5.0;
const float zero_G = 512.0;
const float scale = 102.3;

void setup() {
  Serial.begin(9600);
  
  pinMode(accelX, INPUT);
  pinMode(accelY, INPUT);
  pinMode(accelZ, INPUT);

  pinMode(lPot, INPUT);
  pinMode(rPot, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  delay(25);

  int pot0 = analogRead(lPot);
  int pot1 = analogRead(rPot);

  // read the input on analog pin 0:
  int x = analogRead(accelX);
  delay(5);
  int y = analogRead(accelY);
  delay(5);
  int z = analogRead(accelZ);
  delay(5);

  Serial.print(pot0);
  Serial.print("\t");
  Serial.print(pot1);
  Serial.print("\t");
  Serial.print((((float)(x / VOLT_REF)) - zero_G)/scale);
  Serial.print("\t");
  Serial.print((((float)(y / VOLT_REF)) - zero_G)/scale);
  Serial.print("\t");
  Serial.println((((float)(z / VOLT_REF)) - zero_G)/scale );
}

