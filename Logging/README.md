# Python Logging

Python has several libraries and tools available for logging, ranging from the built-in `logging` module to powerful third-party libraries. Here's a categorized breakdown:

<br>

## **Built-in Logging Library**
1. `logging` (Standard Library)
   * Included in the Python standard library.
   * Thread-safe and highly configurable.
   * Supports multiple log levels, handlers, and formatters.
   * Configuration options: `basicConfig()`, `fileConfig()`, `dictConfig()`.



## **Third-Party Logging Libraries**
2. **Loguru**
   * Very user-friendly with a cleaner API.
   * No boilerplate setup—ready to use out of the box.
   * Built-in rotation, formatting, and exception logging.
   * Great for small-to-medium apps.

    ```bash
    pip install loguru
    ```

    ```python
    from loguru import logger
    logger.info("Hello with Loguru!")
    ```

<br>

3. **structlog**
   * Designed for structured (key-value) logging.
   * Excellent for JSON logging, especially in microservices or distributed systems.
   * Can be combined with standard `logging` for backend integration.

    ```bash
    pip install structlog
    ```

    ```python
    import structlog
    log = structlog.get_logger()
    log.info("event", user="alice", action="login")
    ```
