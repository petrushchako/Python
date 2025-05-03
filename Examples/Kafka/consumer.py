from kafka import KafkaConsumer
import json
import sys

def main():
    # Kafka broker address
    broker = 'localhost:9092'
    # Topic to consume from
    topic = 'my-topic'
    # Consumer group ID
    group = 'my-consumer-group'

    try:
        # Create a Kafka consumer
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=broker,
            group_id=group,
            auto_offset_reset='earliest',  # Start reading from the beginning
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            consumer_timeout_ms=1000, # Add timeout
        )
    except Exception as e:
        print(f"Failed to create consumer: {e}")
        sys.exit(1)

    # Consume messages
    print("Consumer started. Press Ctrl+C to exit.")
    try:
        while True:
            for message in consumer:
                if message is not None:
                    print(f"Received message: {message.value}")
    except KeyboardInterrupt:
        print("Shutting down consumer...")
    finally:
        consumer.close()

if __name__ == "__main__":
    main()