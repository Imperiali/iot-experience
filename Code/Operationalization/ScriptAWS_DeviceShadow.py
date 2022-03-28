from datetime import date, datetime, timedelta
import random 
import pandas as pd
import numpy as np
from awscrt import io, mqtt
from awsiot import mqtt_connection_builder

import json
import time as t

ENDPOINT = "a3kv2eb6iajxne-ats.iot.us-east-1.amazonaws.com"
CLIEND_ID = "SmartWatch"
PATH_TO_CERTIFICATE = "Code/Operationalization/certificates/smartWatch-certificate.pem.crt"
PATH_TO_PRIVATE_KEY = "Code/Operationalization/certificates/smartWatch-private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "Code/Operationalization/certificates/AmazonRootCA1.pem"

TOPIC = "$aws/things/SmartWatch/shadow/name/smart_watch_shadow/update"

df = pd.read_csv('Data\Modeling\SmartWatchDatastore.csv')
df.date = pd.to_datetime(df.date)
df = df.set_index('date')

def findAvarage(df, clName):
    new_df_avg = df[[clName]].sort_values(by='date').copy()
    #colocar datetime.now.weekday() == 0 and 
    if((new_df_avg.index.max() - timedelta(7)).weekday() == 0):
        df_7last_days = new_df_avg[-6:]
        avg = df_7last_days[clName].mean()
        return np.ceil(avg)

def DataAnalyse(dataframe):
    payload = {"state": {"desired": {"steps": "", "calories": "", "rundistance": ""}}}
    
    avgOneWeekSteps = findAvarage(dataframe, 'steps')
    avgOneWeekCalories = findAvarage(dataframe, 'calories')
    avgOneWeekRunDistance = findAvarage(dataframe, 'rundistance')
    
    if random.randint(3500, 5200) < avgOneWeekSteps:
        payload['state']['desired']['steps'] = "Você precisa andar mais."
    else:
        payload['state']['desired']['steps'] = "Você está caminhando o que deveria, continue assim."
        
    if random.randint(100, 350) < avgOneWeekCalories:
        payload['state']['desired']['calories'] = "Você precisa se movimentar mais."
    else:
        payload['state']['desired']['calories'] = "Você está perdendo as calorias que deve, continue assim."
        
    if random.randint(900, 2000) < avgOneWeekRunDistance:
        payload['state']['desired']['rundistance'] = "Você precisa correr mais."
    else:
        payload['state']['desired']['rundistance'] = "Você está correndo mais que o flash, continue assim."
    
    return payload 

if __name__ == "__main__":
    stop = True
    payload = DataAnalyse(df)
    while stop:
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
            clean_session=False
        )
        connection_future = mqtt_connection.connect()
        connection_future.result()
        mqtt_connection.publish(topic=TOPIC, payload=json.dumps(payload), qos=mqtt.QoS.AT_LEAST_ONCE)
        disconnect_future = mqtt_connection.disconnect()
        disconnect_future.result()
        stop = False