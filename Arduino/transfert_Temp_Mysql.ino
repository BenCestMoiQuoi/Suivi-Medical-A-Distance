#include <Ethernet.h>
#include <MySQL_Connection.h>
#include <MySQL_Cursor.h>

byte mac_addr[] = { 0x90, 0xA2, 0xDA, 0x10, 0xA9, 0x58 }; // Adress MAC de la carte
const int ledPin =  3;
const int temp = A0;
bool Tempo ;
float Temperature ;

//Type requète : "INSERT INTO tipe.valeurs (idPatients, idType_prise, Date_prise, Valeur_prise) VALUES ("idpatient", "idprise", now(), "valeur");"
const String idpatient = "10";
const String idprise = "";
char query[] = "";


IPAddress ip(192,168,1,5);
IPAddress server_addr(192,168,1,1);  // IP of the MySQL *server* here
const char user[] = "corroc";              // MySQL user login username
const char password[] = "86.07";           // MySQL user login password


EthernetClient client;
MySQL_Connection conn((Client *)&client);

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.begin(115200);
  Ethernet.begin(mac_addr,ip);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(2000);
  digitalWrite(ledPin, LOW);
  Tempo = 1;
  while (Tempo == 1) {
    temperature();
  }


}

void temperature() {
  idprise = "5";
  Serial.println("Connecting...");
  Serial.print("My IP address: ");
  Serial.println(Ethernet.localIP());
  Serial.print("user : ");
  Serial.println(user);
  if (conn.connect(server_addr, 3306, user, password)) {
    MySQL_Cursor *cur_mem = new MySQL_Cursor(&conn);
    Temperature = (analogRead(temp)*0.168)-7.027;
    Serial.println(Temperature);
    
    String query_1 = "INSERT INTO tipe.valeurs (idPatients, idType_prise, Date_prise, Valeur_prise) VALUES (";
    query_1 = query_1 + idpatient + ", " + idprise + ", now(), " + Temperature + ");";
    Serial.println(query_1);
    for(int i=0;i<query_1.length();i++){
      query[i] = query_1[i];
    }
    Serial.println(query);
    
    cur_mem->execute(query);
    Serial.println("Data recorded.");}
  digitalWrite(ledPin, HIGH);
  Tempo = 0;
  return;
}
