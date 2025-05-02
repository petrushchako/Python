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
