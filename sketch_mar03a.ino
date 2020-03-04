void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int mpp = 10;
int mpr = 10;

int measure() {
  float res = 0;
  for (int i = 0; i < mpr; i++) {
    float val = 0;
    for (int j = 0; j < mpp; j++) {
      val = val + analogRead(1);
    }
    val = val / mpp;
    res = res + val;
  }
  res = res / mpr;
  return res;
  
}
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
    int currentByte = Serial.read();
    if(currentByte == 109) {
      Serial.println(measure());
    }
  }
}
