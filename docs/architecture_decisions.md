# UdaConnect

### Architecture Diagrams: Message Passing Strategy
1. REST : RESTFul API for conenction service, fetching custmer information , location events to update in frontend UI. 
3. KAFKA : Kafka event to receive location data produced by mobile devices, this data will be consumed by location consumer microservice.
3. gRPC : to sends request to location event producer service through Protobuf message using gRPC to efficiently transport structured data.