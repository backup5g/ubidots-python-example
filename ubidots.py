import time
import json
import random

from callbacks import (
  on_connect, 
  on_publish, 
  on_message,
  on_subscribe,
  get_connection_status
)


def connect(
  mqtt_client, 
  mqtt_username, 
  mqtt_password, 
  broker_endpoint, 
  port
):
  connected = get_connection_status()

  if not connected:
    mqtt_client.username_pw_set(mqtt_username, password = mqtt_password)

    mqtt_client.on_connect = on_connect
    mqtt_client.on_publish = on_publish
    mqtt_client.on_subscribe = on_subscribe
    mqtt_client.on_message = on_message

    mqtt_client.connect(broker_endpoint, port = port)
    mqtt_client.loop_start()

    attempts = 0

    while not connected and attempts < 5:
      connected = get_connection_status()
      print('[INFO] Aguardando conexão...')
      time.sleep(1)
      attempts += 1

  if not connected:
    print('[ERROR] Não foi possível conectar-se ao broker')
    return False

  return True


def publish(mqtt_client, topic, device_label, variable_label):
  sensor_value = random.random() * 100

  payload = json.dumps({ variable_label: sensor_value })
  topic = "{}{}".format(topic, device_label)

  print('[INFO] Aguardando para publicar o seguinte payload:')
  print(payload)

  try:
    mqtt_client.publish(topic, payload)
  except Exception as e:
    print('[ERROR] Houve um erro: \n{}'.format(e))


def subscribe(
  mqtt_client,
  topic,
  device_label,
  variable_label
):
  topic = "{}{}/{}/lv".format(topic, device_label, variable_label)
  print(topic)

  mqtt_client.subscribe(topic, 0)
  mqtt_client.unsubscribe(topic, 0)
