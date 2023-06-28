#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <WiFiClient.h>

const uint16_t port = 666;
const char *host = "IP";
WiFiClient client;
void setup()
{
    Serial.begin(115200);
    Serial.println("Conectando...\n");
    WiFi.mode(WIFI_STA);
    WiFi.begin("", ""); // ('WIFI-SSID','WIFI_SENHA')
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
}

void loop()
{
    if (!client.connect(host, port))
    {
        Serial.println("schuster Triste:(");
        delay(1000);
        return;
    }

    Serial.println("schuster feliz :)");
    client.scanf("%c", &chr);   
    client.println("uhul!");
    delay(250);

    while (client.available() > 0)
    {
        char c = client.read();
        Serial.write(c);
    }
    
    Serial.print('\n');
    client.stop();
    delay(5000);
}