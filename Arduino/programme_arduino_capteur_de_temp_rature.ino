void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
Serial.println(analogRead(A0));
Serial.print("température : ");
Serial.println((analogRead(A0)*0.168)-7.27);
delay(2000);
}
