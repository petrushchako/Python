from kafka import KafkaProducer
import json
import time

# Configure the producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Replace with your Kafka broker address
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # JSON encoding
)

# Function to send messages
def send_message(topic, message):
    try:
        # Send a message to the specified topic
        producer.send(topic, message)
        print(f"Message sent to topic '{topic}': {message}")
    except Exception as e:
        print(f"Failed to send message: {e}")

# Example usage
if __name__ == "__main__":
    topic_name = 'my_topic'

    # Send 5 messages with a delay
    for i in range(5):
        message = {'number': i, 'timestamp': time.time()}
        send_message(topic_name, message)
        time.sleep(1)  # Delay between messages

    # Flush and close the producer
    producer.flush()
    producer.close()
