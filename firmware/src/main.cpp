// Monitor de temperatura e umidade — firmware do ESP32
// Repositório: projeto-iot-lucasg  |  Dispositivo: esp32-lucasg
//
// Esqueleto organizado do firmware. Cada TODO corresponde a um
// requisito do manual (R1 a R3, semana 1).

#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include <DHT.h>

#include "secrets.h"   // copie include/secrets.example.h para include/secrets.h

// ---------------- Configuração ----------------
constexpr uint8_t  PINO_DHT     = 4;       // GPIO4 — ver docs/esquema-ligacao.svg
constexpr uint8_t  TIPO_DHT     = DHT22;
constexpr uint32_t INTERVALO_MS = 10000;   // 10 s (mínimo do DHT22: 2 s)

const char* DISPOSITIVO   = "esp32-lucasg";   // também é o client ID MQTT
const char* PROJETO       = "temperatura";
const char* TOPICO_DADOS  = "inatel/lucasg/dados";
const char* TOPICO_STATUS = "inatel/lucasg/status";

DHT dht(PINO_DHT, TIPO_DHT);
WiFiClient wifiClient;
PubSubClient mqtt(wifiClient);

uint32_t ultimaLeitura = 0;

// ---------------- Wi-Fi (R3) ----------------
void garantirWiFi() {
  // TODO: se WiFi.status() != WL_CONNECTED, tentar reconectar
  //       sem travar o loop (usar millis() para espaçar as tentativas)
}

// ---------------- MQTT + Last Will (R2, R3) ----------------
void garantirMqtt() {
  // TODO: se desconectado, mqtt.connect(DISPOSITIVO, MQTT_USER, MQTT_PASS,
  //       TOPICO_STATUS, qos, true /*retido*/, "offline")
  // TODO: ao conectar, publicar "online" retido em TOPICO_STATUS
  // TODO: em caso de falha, registrar mqtt.state() no serial
}

// ---------------- Leitura e publicação (R1, R2) ----------------
void lerEPublicar() {
  // TODO: ler temperatura e umidade; se isnan(), registrar e NÃO publicar
  // TODO: montar o JSON padrão com ArduinoJson:
  //   {"dispositivo":"esp32-lucasg","projeto":"temperatura",
  //    "leituras":{"temperatura":24.6,"umidade":58.2}}
  // TODO: publicar em TOPICO_DADOS
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  mqtt.setServer(MQTT_HOST, MQTT_PORT);
}

void loop() {
  garantirWiFi();
  garantirMqtt();
  mqtt.loop();

  if (millis() - ultimaLeitura >= INTERVALO_MS) {
    ultimaLeitura = millis();
    lerEPublicar();
  }
}
