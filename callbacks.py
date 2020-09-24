connected = False

def on_connect(client, userdata, flags, rc):
  if rc == 0:
    print('[INFO] Conectado ao broker')

    global connected
    connected = True 

  else:
    print('[INFO] A conexão falhou')


def on_publish(client, userdata, result):
  print('[INFO] Publicado!')
  print('')


def get_connection_status():
  return connected


def on_message(mqtt_client, obj, msg):
    print("[INFO] Valor recebido: {}".format(float(msg.payload)))
    print('')


def on_subscribe(mqtt_client, obj, mid, granted_qos):
    print("[INFO] Inscrito!")