# Kafka Consumer and Producer Example in Python

This project demonstrates how to implement a simple Kafka producer and consumer using Python and the `kafka-python` library. The producer sends messages to a Kafka topic, and the consumer reads messages from that topic.

## Prerequisites

- Python 3.7 or higher
- Apache Kafka (version 2.0 or later)
- A running Kafka broker (locally or on a server)

## Setup Instructions

### 1. Install Dependencies

All dependencies are listed in `requirements.txt`. Install them by running:

```bash
pip install -r requirements.txt
```

### 2. Set Up Kafka

Ensure that you have access to a running Kafka broker. You can run one locally or connect to a remote server.

- **Kafka Broker Address**: Replace `your.kafka.broker:9092` in the scripts with your Kafka broker address.
- **Topic Name**: Replace `my_topic` in the scripts with your desired Kafka topic name.

### 3. Running the Producer and Consumer

#### Kafka Producer

The producer script sends messages to the specified Kafka topic.

```bash
python producer.py
```

#### Kafka Consumer

The consumer script listens to messages from the specified Kafka topic.

```bash
python consumer.py
```

## Configuration

- **Kafka Broker**: Update the `kafka_broker` variable in `producer.py` and `consumer.py` to point to your Kafka broker.
- **Topic Name**: Update the `topic_name` variable in both files.

## Project Files

- `producer.py`: Sends messages to the Kafka topic.
- `consumer.py`: Listens to messages from the Kafka topic and processes them.
- `requirements.txt`: Lists all Python dependencies for the project.
