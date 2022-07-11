
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <ArduinoJson.h>

const char* ssid = "your SSID name";
const char* password = "SSID Password";
int sensor = 13;  // Digital pin D7 for PIR sensor
const char* host = "your-http-server-domain";
const char *api = "http://www.h4mid-hosseini.ir/friday/api/";
const char *password = "yourpassword";

#include "DHT.h"

#define DHTPIN 4     // what digital pin the DHT11 is conected to
#define DHTTYPE DHT11   // there are multiple kinds of DHT sensors. i'm using dht11

DHT dht(DHTPIN, DHTTYPE);
void setup() {
  Serial.begin(115200);
  delay(10);
  pinMode(A0, INPUT); //declare ldr sensor port as input
  pinMode(sensor, INPUT);   // declare sensor as input
  dht.begin();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  pinMode(14, OUTPUT);
  pinMode(12, OUTPUT);


  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    yield();
  }

//  Serial.println("");
//  Serial.println("WiFi connected");  
//  Serial.println("IP address: ");
//  Serial.println(WiFi.localIP());
}

void loop() {
//  Serial.print("connecting to ");
  HTTPClient http;    //Declare object of class HTTPClient
  delay(100);
  // Use WiFiClient class to create TCP connections
  WiFiClientSecure client;
  delay(100);
  const int httpPort = 443; // 80 is for HTTP / 443 is for HTTPS!
  client.setInsecure(); // this is the magical line that makes everything work
  delay(100);
  WiFiClient wifi;
  http.begin(wifi, api);
  delay(100);
  int httpCode = http.GET();            //Send the request
  String payload = http.getString();    //Get the response payload from server
  if(httpCode == 200)
  {
    // Allocate JsonBuffer
    // Use arduinojson.org/assistant to compute the capacity.
    const size_t capacity = JSON_OBJECT_SIZE(3) + JSON_ARRAY_SIZE(2) + 60;
    DynamicJsonBuffer jsonBuffer(capacity);
    delay(50);
  
   // Parse JSON object
    JsonObject& root = jsonBuffer.parseObject(payload);
    delay(50);
    if (!root.success()) {
      Serial.println(F("Parsing failed!"));
      delay(50);
    }

    delay(50);
    if (root["lamp"]=="true")
    {
      digitalWrite(14,HIGH);
      delay(50);
     }
     if (root["lamp"]=="false")
    {
      digitalWrite(14,LOW);
      delay(50);
     }

     if (root["relay"]=="true")
    {
      digitalWrite(12,HIGH);
      delay(50);
     }
     if (root["relay"]=="false")
    {
      digitalWrite(12,LOW);
      delay(50);
     }
  }

  if (!client.connect(host, httpPort)) { //works!
   Serial.println("connection failed");
    delay(50);
  }
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
    int h = dht.readHumidity();
    // Read temperature as Celsius (the default)
    int t = dht.readTemperature();
    if (isnan(h) || isnan(t)) {
//      Serial.println("Failed to read from DHT sensor!");
      delay(50);
    }

  int pir = digitalRead(sensor);
  delay(50);
  int ldr = analogRead(A0);
  delay(50);
  String url = "/friday/home/";
  url += t;
  url += "/";
  url += h;
  url += "/";
  url += pir;
  url += "/";
  url += ldr;
  url += "/";
  url += password;
  url += "/";
  
Serial.println(url);
  delay(50);

Serial.print("Requesting URL: ");

  // This will send the request to the server
  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
 Serial.println();
  delay(50);
 Serial.println("closing connection");
  delay(1500);
}
