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


## Overview of Dockerfiles
## Containerize (or Dockerize) your app

