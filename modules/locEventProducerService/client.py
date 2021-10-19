import grpc
import location_event_pb2
import location_event_pb2_grpc

"""
write messages to gRPC.
"""

print("Send payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = location_event_pb2_grpc.location_eventServiceStub(channel)

# Update this with desired payload
location_event = location_event_pb2.location_eventMessage(
    userId=1,
    latitude=-100,
    longitude=30
)

location_event2 = location_event_pb2.location_eventMessage(
    userId=2,
    latitude=-90,
    longitude=40
)

location_event3 = location_event_pb2.location_eventMessage(
    userId=3,
    latitude=-80,
    longitude=50
)

response1 = stub.Create(location_event)
response2 = stub.Create(location_event2)
response3 = stub.Create(location_event3)

print("Location sent...")
print(location_event, location_event2, location_event3)