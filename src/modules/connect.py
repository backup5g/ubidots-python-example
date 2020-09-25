import time

from modules.publish import on_publish
from modules.subscribe import on_message, on_subscribe

connected = False


def on_connect(client, userdata, flags, rc):
  if rc == 0:
    print('[INFO] Conectado ao broker')

    global connected
    connected = True 

  else:
    print('[INFO] A conexão falhou')


def connect(
  mqtt_client, 
  mqtt_username, 
  mqtt_password, 
  broker_endpoint, 
  port
):
  global connected

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
      print('[INFO] Aguardando conexão...')
      time.sleep(1)
      attempts += 1

  if not connected:
    print('[ERROR] Não foi possível conectar-se ao broker')
    return False

  return True