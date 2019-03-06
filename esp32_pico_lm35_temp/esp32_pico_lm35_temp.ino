const int analogIn = 26;
 
int raw = 0;
double voltage = 0;
double tempC = 0;


void setup(){
  Serial.begin(115200);
  adcAttachPin(analogIn);
  adcStart(analogIn);
  analogReadResolution(12); // Default of 12 is not very linear. 10 or 11 are other options. If changing these, the voltage calculation will need to change by 2^resolution
  analogSetAttenuation(ADC_11db); // Default is 11db is apparently noisy. could be worth looking at 6 (Although this changes this voltage calculation!) 11db seems to have a range from 0-5v.
}

void loop(){
  raw = analogRead(analogIn);
  voltage = (raw / 4096.0) * 5000; // 5000 to get millivots.
  tempC = voltage * 0.1;
  Serial.print("TEMP C: ");
  Serial.println(tempC);
  delay(500);
}
