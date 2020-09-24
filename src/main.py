import paho.mqtt.client as mqttClient
import time

from connect import connect, connected
from publish import publish
from subscribe import subscribe

from env import (
  BROKER_ENDPOINT,
  PORT,
  MQTT_USERNAME,
  MQTT_PASSWORD,
  TOPIC,
  DEVICE_LABEL,
  VARIABLE_LABELS,
)


def create_menu():
  print('---------ESCOLHA UMA OPÇÃO----------')
  print('(1) Enviar informação dispositivo 01')
  print('(2) Enviar informação dispositivo 02')
  print('(3) Enviar informação dispositivo 03')
  print('(4) Ler dispositivo 04')
  print('(5) Sair')

  menu = int(input(''))

  if menu < 1 or menu > 5:
    create_menu()

  return menu


def main(mqtt_client):
  if not connected:
    connect(
      mqtt_client,
      MQTT_USERNAME,
      MQTT_PASSWORD,
      BROKER_ENDPOINT, 
      PORT
    )

  if menu != 4:
    publish(
      mqtt_client,
      TOPIC,
      DEVICE_LABEL,
      VARIABLE_LABELS[menu - 1],
    )

  else:
    subscribe(
      mqtt_client,
      TOPIC,
      DEVICE_LABEL,
      VARIABLE_LABELS[3]
    )


if __name__ == '__main__': 
  mqtt_client = mqttClient.Client()

  while True:
    menu = create_menu()

    if menu == 5: 
      break
 
    main(mqtt_client)
    time.sleep(1)
