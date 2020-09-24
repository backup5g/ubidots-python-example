import json
import random

def on_publish(client, userdata, result):
  print('[INFO] Publicado!')
  print('')

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