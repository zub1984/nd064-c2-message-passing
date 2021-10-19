# UdaConnect

### Architecture Diagrams: Message Passing Strategy

1. REST : RESTFul API for conenction service, fetching custmer information , location events to update in frontend UI. 

2. gRPC : To sends mobile device generated events ,simulated using `locEventProducerService/client.py` to producer service through Protobuf message for efficient transport of events data.

3. KAFKA : Kafka producer will receive location info from mobile devices and produce the Kafka events , Kafka consumer will cosume these location info events and write them in location database.