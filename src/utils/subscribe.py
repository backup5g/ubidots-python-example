def on_message(mqtt_client, obj, msg):
    print("[INFO] Valor recebido: {}".format(float(msg.payload)))
    print('')


def on_subscribe(mqtt_client, obj, mid, granted_qos):
    print("[INFO] Inscrito!")


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