const int piezoPins[] = {A0, A1, A2, A3, A4, A5};
const int numPiezos = sizeof(piezoPins) / sizeof(piezoPins[0]);
const int threshold = {700};
const int debounceDelay = 2000;

unsigned long lastImpactTime[numPiezos];

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < numPiezos; i++) {
    lastImpactTime[i] = 0;
  }
}

void loop() {
  unsigned long currentTime = millis();

  for (int i = 0; i < numPiezos; i++) {
    analogRead(piezoPins[i]); // Dummy read for ADC settling
    int sensorReading = analogRead(piezoPins[i]);

    if (sensorReading >= threshold) {
      if (currentTime - lastImpactTime[i] > debounceDelay) {
        //Serial.print("Impact detected on Piezo ");
        //Serial.print(i);
        //Serial.print(" with reading: ");
        //Serial.println(sensorReading);
        Serial.print("PIEZO_");
        Serial.println(i);
        Serial.println(" ");
        lastImpactTime[i] = currentTime;
      }
    }
  }
}
