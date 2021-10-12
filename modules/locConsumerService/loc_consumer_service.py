from kafka import KafkaConsumer
import logging
import os
import json
from sqlalchemy import create_engine

kafka_url = os.environ["KAFKA_URL"]
kafka_topic = os.environ["KAFKA_TOPIC"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

consumer = KafkaConsumer(kafka_topic, bootstrap_servers=[kafka_url])
logging.debug('kafka_url : ', kafka_url)
logging.debug('kafka_topic : ', kafka_topic)

def write_to_db(location):
    conn = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
    cur = conn.cursor()
    user_id = int(location["userId"])
    latitude, longitude = int(location["latitude"]), int(location["longitude"])
    table_insert = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))" \
        .format(user_id, latitude, longitude)

    print(table_insert)
    cur.execute(table_insert)


for topic in consumer:
    location_message = json.loads(topic.value.decode('utf-8'))
    print (location_message)