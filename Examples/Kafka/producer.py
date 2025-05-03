from kafka import KafkaProducer
import json
import time
import sys

def main():
    # Kafka broker address
    broker = 'localhost:9092'
    # Topic to produce to
    topic = 'my-topic'

    try:
        # Create a Kafka producer
        producer = KafkaProducer(
            bootstrap_servers=broker,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    except Exception as e:
        print(f"Failed to create producer: {e}")
        sys.exit(1)

    # Produce messages to the topic
    for i in range(10):
        message = {'message': f'Message from Python Producer: {i}', 'timestamp': time.time()}
        try:
            producer.send(topic, message)
            print(f"Produced message: {message}")
            producer.flush()
        except Exception as e:
            print(f"Failed to produce message: {e}")

    producer.close()

if __name__ == "__main__":
    main()