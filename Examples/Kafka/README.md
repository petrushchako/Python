# Python Kafka consumer and producer

## Step 1: Set up Kafka using Docker Compose
    ```yaml
    services:
    zookeeper:
        image: 'bitnami/zookeeper:latest'
        ports:
        - '2181:2181'
        environment:
        - ALLOW_ANONYMOUS_LOGIN=yes
    kafka:
        image: 'bitnami/kafka:latest'
        ports:
        - '9092:9092'
        - '9094:9094'
        environment:
        - KAFKA_BROKER_ID=1
        - KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9094
        - KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092
        - KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181
        - KAFKA_CONTROLLER_QUORUM_VOTERS=1@kafka:9094
        - ALLOW_PLAINTEXT_LISTENER=yes
        depends_on:
        - zookeeper
    ```

- Start Kafka:
    `docker-compose up -d`

<br><br><br>

## Step 2: Set up a Python Project and Install the Kafka Library
- Create a Python project:
    ```sh
    mkdir kafka-python-example
    cd kafka-python-example
    python3 -m venv venv # Create a virtual environment
    source venv/bin/activate # Activate the virtual environment
    ```
- Install the kafka-python library:
    `pip install kafka-python`

<br><br><br>

## Step 3: Create a Kafka Producer in Python
- Create `producer.py`:
    ```py
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
    ```

- Run the producer:
    `python producer.py`

<br><br><br>
