import time
from concurrent import futures

import grpc
import location_event_pb2
import location_event_pb2_grpc
from kafka import KafkaProducer
import logging
import os
import json

kafka_url = os.environ["KAFKA_URL"]
kafka_topic = os.environ["KAFKA_TOPIC"]
producer = KafkaProducer(bootstrap_servers=kafka_url)
logging.info('kafka_url : ', kafka_url)
logging.info('kafka_topic : ', kafka_topic)

class LocationEventService(location_event_pb2_grpc.LocationEventService):
    
    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            'userId': int(request.userId),
            'latitude': int(request.latitude),
            'longitude': int(request.longitude)
        }
        print(request_value)
        user_encode_data = json.dumps(request_value, indent=2).encode('utf-8')
        producer.send(kafka_topic, user_encode_data)
        return location_event_pb2.location_eventMessage(**request_value)

# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_event_pb2_grpc.add_location_eventServiceServicer_to_server(LocationEventService(), server)

print("Server starts on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)