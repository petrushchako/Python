from kafka import KafkaConsumer
import json

# Kafka broker and topic configuration
kafka_broker = "your.kafka.broker:9092"  # Replace with your broker address
topic_name = "my_topic"  # Replace with your topic name

# Initialize the Kafka consumer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=[kafka_broker],
    auto_offset_reset="earliest",  # Start reading at the earliest message
    enable_auto_commit=True,  # Automatically commit offsets
    group_id="my-group-id",  # Consumer group ID for tracking
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

print(f"Subscribed to topic '{topic_name}' and waiting for messages...")

# Consume messages
for message in consumer:
    print(f"Received message: {message.value}")

# Close the consumer when done (optional in this example since it's an infinite loop)
consumer.close()
