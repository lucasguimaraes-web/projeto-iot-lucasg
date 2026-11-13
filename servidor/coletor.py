"""Coletor MQTT — assina inatel/lucasg/dados, valida e grava no MySQL (semana 2/3).

Executar:  python coletor.py   (com o .venv ativo)
"""
import logging
import os

import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("coletor")

FAIXAS = {
    "DHT22": {"temperatura": (-40, 80), "umidade": (0, 100)},
    "DHT11": {"temperatura": (0, 50), "umidade": (20, 90)},
}


def validar(payload: bytes):
    """Devolve (dados, None) se válido ou (None, motivo) se inválido.

    Recusar: JSON inválido, campo faltando, valor não numérico
    (atenção: bool é subclasse de int em Python) ou fora da faixa.
    """
    # TODO
    raise NotImplementedError


def on_connect(client, userdata, flags, reason_code, properties):
    # TODO: assinar o tópico AQUI, para sobreviver a reconexões
    pass


def on_message(client, userdata, msg):
    # TODO: validar(); se válido, db.gravar_leituras(); registrar aceito/descartado
    pass


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="coletor-lucasg")
    client.username_pw_set(os.getenv("MQTT_USER"), os.getenv("MQTT_PASS"))
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(os.getenv("MQTT_HOST", "localhost"), int(os.getenv("MQTT_PORT", "1883")))
    client.loop_forever()


if __name__ == "__main__":
    main()
