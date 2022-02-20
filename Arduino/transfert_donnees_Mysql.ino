#include <Ethernet.h>
#include <MySQL_Connection.h>
#include <MySQL_Cursor.h>

byte mac_addr[] = { 0x90, 0xA2, 0xDA, 0x10, 0xA9, 0x58 }; // Adress MAC de la carte
const int ledPin =  3;
const int temp = A0;
bool Tempo;

//Type requète : "INSERT INTO tipe.valeurs (idPatients, idType_prise, Date_prise, Valeur_prise) VALUES ("idpatient", "idprise", now(), "valeur");"
String idpatient = "10";
String idprise = "";


IPAddress ip(192,168,1,5);
IPAddress server_addr(192,168,1,1);  // IP of the MySQL *server* here
char user[] = "corroc";              // MySQL user login username
char password[] = "86.07";           // MySQL user login password


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
  Serial.println("ok1");
  idprise = "4";
  Serial.println("Connecting...");
  Serial.print("My IP address: ");
  Serial.println(Ethernet.localIP());
  Serial.println("ok2");
  if (conn.connect(server_addr, 3306, user, password)) {
    Serial.println("ok3");
    MySQL_Cursor *cur_mem = new MySQL_Cursor(&conn);
    Serial.println(analogRead(temp));
    
    String query_1 = "INSERT INTO tipe.valeurs (idPatients, idType_prise, Date_prise, Valeur_prise) VALUES (";
    query_1 = query_1 + idpatient + ", " + idprise + ", now(), " + analogRead(temp) + ");";
    Serial.println(query_1);
    char query[] = "";
    for(int i=0;i<query_1.length();i++){
      query[i] = query_1[i];
    }
    Serial.println(query);
    
    cur_mem->execute(query);
    Serial.println("Data recorded.");}
  digitalWrite(ledPin, HIGH);
  Serial.println("ok4");
  Tempo = 0;
  return;
}
