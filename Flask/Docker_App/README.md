# Developing Python 3 Apps with Docker


### Course Contents
- Dockerizing a Python application
- Multi-Container Python application
- Productionalizing a docker-based application
- Debugging a Python application

> [Course source code](https://github.com/geekcap-pluralsight/python-docker)

<br>

## Getting Started with Python and Docker
- **Environment setup**
    - Download Python (3.9.1 used in this course) from [official website](https://www.python.org)
    - Create project directory
        ```sh
        mkdir wired-brain
        cd wired-brain
        mkdir product-service
        cd product-service
        ```
    - Setup a Virtual Environment (venv)
        ```sh
        # Create virtual environment
        python -m venv venv
        source venv/bin/activate
        ```
    - Install Flask
        ```sh
        pip install Flask
        ```
- **VSCode vs. PyCharm**
  |Visual Studio Code | PyCharm|
  |---|---|
  |Open Source<br>Written using Electron<br>Small Memory Footprint<br>Extensible to program in many languages<br>Code Editor|Commercial<br>Written in Java<br>Larger Memory Footprint|Designed specifically for Python<br>Fully Python IDE|

## Create Python Flask app
- **Flask**<br>Flask is a micro web framework written in Python. It does not provide a database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. It supports extensions that add application features as if they were implemented in Flask itself.
- Create a Flask application
    ```sh
    touch app.py
    ```

- Add endpoints
  - `GET` `/products`
  - `GET` `/products/{id}`
  - `POST` `/product`
  - `POST` `/product{id}`
  - `DELETE` `/product/{id}`

<br><br><br>


## Testing Flask API Using curl
### Setup
* **Navigate to your project directory**
* **Activate virtual environment**:
  * macOS/Linux: `source venv/bin/activate`
  * Windows: `venv\Scripts\activate.bat`
* **Start Flask app**:
  ```bash
  python source/app.py
  ```
* App runs in **debug mode** on `0.0.0.0:5000`

<br>

### Using curl to Test Endpoints
#### 1. **GET /products**
```bash
curl http://localhost:5000/products
```

* Returns the list of all products
* Use `-v` to see HTTP headers:
  ```bash
  curl -v http://localhost:5000/products
  ```

#### 2. **GET /product/<id>**
```bash
curl -v http://localhost:5000/product/1
```

* Returns a product with ID 1
* Invalid ID returns:
  * `404 NOT FOUND`
  * Error message

#### 3. **POST /product** (Add product)
```bash
curl --header "Content-Type: application/json" \
     --request POST \
     --data '{"name": "Product 3"}' \
     -v http://localhost:5000/product
```

* Adds a new product
* Returns:
  * `201 CREATED`
  * JSON with generated product ID

#### 4. **PUT /product/<id>** (Update product)
```bash
curl --header "Content-Type: application/json" \
     --request PUT \
     --data '{"name": "Updated Product 2"}' \
     -v http://localhost:5000/product/2
```

* Updates product with ID 2
* Invalid ID (e.g., `/product/5`) returns:
  * `404 NOT FOUND`

#### 5. **DELETE /product/<id>**
```bash
curl --request DELETE \
     -v http://localhost:5000/product/2
```

* Deletes product with ID 2
* Invalid ID deletion returns:
  * `404 NOT FOUND`

<br>

### Summary
* All endpoints (`GET`, `POST`, `PUT`, `DELETE`) function as expected.
* Proper HTTP status codes are returned:
  * `200 OK`, `201 CREATED`, `404 NOT FOUND`
* curl is a reliable tool to simulate API interactions without a browser.


## Dockerizing Flask Application
### **Dockerfile**
* A text document containing **step-by-step commands** to build a Docker image.
* Represents all instructions that Docker executes to assemble an image.

### **Docker image**
* A **read-only template** with instructions for creating a container.
* The output of building a Dockerfile.
* Can be stored locally or pushed to a **Docker registry** (e.g., Docker Hub).

#### **Docker container**
* A **runtime instance** of a Docker image (like creating an object from a class).

<br>

### Lifecycle Flow
1. **Write a Dockerfile**
2. **Build the Dockerfile → Docker image**
3. **Run the Docker image → Docker container**

<br>

### Example: Minimal Debian Dockerfile
```Dockerfile
FROM scratch
ADD file.tar.xz /
CMD ["bash"]
```

* `FROM scratch`: Start with an empty image.
* `ADD file.tar.xz /`: Upload & decompress Debian OS to root.
* `CMD ["bash"]`: Start a Bash shell by default.

<br>

### Docker Hub
* [Docker Hub](https://hub.docker.com) is the largest repository of Docker images.
* Images can be:
  * **Official**: Curated, regularly updated (e.g., Python, MySQL, NGINX).
  * **Unofficial**: Community or individual contributions; fine for experimentation.

> **Tip:** For production apps, prefer official images for security and stability.

<br>

### Python Docker Image
* Official Python image: [`_/python`](https://hub.docker.com/_/python)
* Popular tag example: `3.9.2-buster`
* Provides pre-installed Python, ready for app deployment.

<br>

### Analogy
* Dockerfile = Python class definition
* Docker image = Compiled class structure
* Docker container = Instance (object) created from the class



## Creating a Dockerfile and Running a Container
### Docker Image Layers
A Docker image consists of read-only layers each of which represents a Dockerfile instruction. The layers are stacked and each one is a delta of the changes from the previous layer.

- **Create a `Dockerfile` descriptor that will contain the following Docker image build instructions**:
  - Start from the Python Official Image
  - Set the current working directory to `/code`
  - Copy the `requirements.txt` file to the working directory
  - Run `pip install` to install our dependencies (Flask)
  - Copy our source code to `/code/src/`
  - Run `python ./app.py`


- **Build a Docker Image**:<br>Docker images are built using the docker build command, specifying a tag (`-t` or `--tag`) and providing a name and optionally a tag, and the path that contains a Dockerfile<br>If you want to name your Dockerfile anything other than `Dockerfile`, you can specify the filename using the `-f` argument:

    ```sh
    docker build -t <name>:<tag> .
    docker build -d flask-app:1.0 .
    ```

- **Run container from the built image**:
  
    ```sh
    # Start container
    docker run -d -p 5000:5000 flask-app:laters

    # Check running container(s)
    docker ps | grep -E "flask|CONTAINER"

    # Trigger the endpoint
    curl http://localhost:5000/products

    # Open container terminal
    docker exec -it <container_id> bash
    
    # List content of container and exit
    ls -l && exit

    docker stop <container_id>
    ```

<br><br><br>



## Running Multiple Components with Docker Compose
#### **Module Focus**
* Build **multi-container Docker applications** using Docker Compose.
* Add components:
  * **Nginx reverse proxy**: Forwards requests to product service.
  * **MySQL**: Persists product data via **SQLAlchemy ORM**.
* Test end-to-end: Nginx → product service → MySQL persistence.

<br>

### **What is Docker Compose?**
* Tool for **defining and running multi-container Docker applications**.
* Uses a single **YAML file** to configure all services.
* Start everything with one command:

  ```sh
  docker-compose up
  ```

<br>

### **Benefits of Docker Compose**
* **Isolated environments** on a single host (isolated network for each app).
* **Preserves volume data** when containers are restarted (copies volumes from old containers).
* **Recreates only changed containers** (caches container configs for faster updates).
* **Supports variables** in YAML for easy environment customization (local vs production).

<br>

###  **Docker Compose YAML Structure**
#### Example:
```yaml
services:
  productservice:
    build: ./product-service

  web:
    build: ./nginx
    ports:
      - "80:80"

  db:
    image: mysql:latest
    command: --init-file /data/application/init.sql --default-authentication-plugin=mysql_native_password
    volumes:
      - ./db:/data/application
    environment:
      MYSQL_ROOT_PASSWORD: password
```

* `services`: Defines all app containers.
* `productservice`: Built from `product-service` directory’s Dockerfile.
* `web`: Nginx container, exposes port 80.
* `db`: Uses official MySQL image with:
  * **Init SQL** at `/data/application/init.sql` (mounted via volume).
  * `MYSQL_ROOT_PASSWORD=password`.

 **YAML indentation matters** — use 2 spaces for each level!

<br>

### **Common Docker Compose Commands**
```bash
docker-compose build     # Build all services (uses cache for unchanged ones)
docker-compose up        # Start all containers
docker-compose up -d     # Start containers in daemon/background mode
docker-compose down      # Stop and remove containers, networks, etc.
```

<br><br><br>

