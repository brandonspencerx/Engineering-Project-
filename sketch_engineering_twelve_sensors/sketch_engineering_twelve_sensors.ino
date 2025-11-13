const int piezoPins[] = {A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12};
const int numPiezos = sizeof(piezoPins) / sizeof(piezoPins[0]);

const int hitThreshold = 350;      // Nerf impact threshold
const int quietThreshold = 120;    // must fall below this to re-arm
const int lockoutTime = 400;       // ms target stays “locked” after a hit

unsigned long lastImpactTime[numPiezos];
bool locked[numPiezos];

int smooth(int pin) {
  return (analogRead(pin) + analogRead(pin)) / 2;
}

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < numPiezos; i++) {
    lastImpactTime[i] = 0;
    locked[i] = false;
  }
}

void loop() {
  unsigned long currentTime = millis();

  for (int i = 0; i < numPiezos; i++) {

    int reading = smooth(piezoPins[i]);

    // ----- UNLOCK WHEN THE TARGET IS CALM -----
    if (locked[i] && reading < quietThreshold && 
        currentTime - lastImpactTime[i] > lockoutTime) {
      locked[i] = false;
    }

    // ----- IGNORE IF SENSOR IS LOCKED -----
    if (locked[i]) continue;

    // ----- REGISTER A REAL HIT -----
    if (reading >= hitThreshold) {

      Serial.print("PIEZO_");
      Serial.println(i);
      Serial.println(" ");

      lastImpactTime[i] = currentTime;
      locked[i] = true;   // prevent retriggers while swinging
    }
  }
}



/*
const int piezoPins[] = {A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12};
const int numPiezos = sizeof(piezoPins) / sizeof(piezoPins[0]);

const int threshold = 750;          // adjust per sensitivity
const unsigned long debounceDelay = 200;  // ms between valid hits
const int sampleCount = 3;          // number of analog samples per read

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
    // Take a few quick samples and average them
    long total = 0;
    for (int s = 0; s < sampleCount; s++) {
      total += analogRead(piezoPins[i]);
      delayMicroseconds(200); // small pause for ADC stability
    }
    int sensorReading = total / sampleCount;

    // Check threshold and debounce
    if (sensorReading >= threshold && (currentTime - lastImpactTime[i] > debounceDelay)) {
      Serial.print("PIEZO_");
      Serial.println(i);
      lastImpactTime[i] = currentTime;
    }
  }
}
*/

