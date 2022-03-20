import pandas as pd
from awscrt import io, mqtt
from awsiot import mqtt_connection_builder

import json
import time as t

ENDPOINT = "a3kv2eb6iajxne-ats.iot.us-east-1.amazonaws.com"
CLIEND_ID = "SmartWatch"
PATH_TO_CERTIFICATE = "Code/Operationalization/certificates/smartWatch-certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "Code/Operationalization/certificates/smartWatch-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "Code/Operationalization/certificates/AmazonRootCA1.pem"

TOPIC = "SmarWatch/publish"

df = pd.read_csv("Data/Processed/datasetConcatAT.csv")

def publishAws(payload):
    mqtt_connection.publish(topic=TOPIC, payload=payload, qos=mqtt.QoS.AT_LEAST_ONCE)
    t.sleep(.1)


if __name__ == "__main__":
    read_from_line = 0
    while True:
        event_loop_group = io.EventLoopGroup(1)
        host_resolver = io.DefaultHostResolver(event_loop_group)
        client_bootstrap = io.ClientBootstrap(event_loop_group,  host_resolver)
        mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=ENDPOINT,
            cert_filepath=PATH_TO_CERTIFICATE,
            pri_key_filepath=PATH_TO_PRIVATE_KEY,
            ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
            client_bootstrap=client_bootstrap,
            client_id=CLIEND_ID,
            clean_session=False,
            keep_alive_secs=6
        )
        connection_future = mqtt_connection.connect()
        connection_future.result()
        df.apply(lambda x: publishAws(json.dumps(json.loads(x.to_json()))), axis=1)
        disconnect_future = mqtt_connection.disconnect()
        disconnect_future.result()