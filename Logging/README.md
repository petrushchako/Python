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

<br>

4. **logbook**
   * Easier alternative to `logging` with better defaults.
   * Designed by Armin Ronacher (creator of Flask).
   * Offers similar features to `logging` but more Pythonic.

    ```bash
    pip install logbook
    ```

    ```python
    import logbook
    log = logbook.Logger('MyApp')
    log.info('Info message from Logbook')
    ```

<br>

5. **logging-tree**
   * Diagnostic tool—not a logging system itself.
   * Visualizes your current logging hierarchy.
   * Helps debug complex logging configurations.

   ```bash
   pip install logging-tree
   ```

   ```python
   import logging_tree
   print(logging_tree.format.build_description())
   ```

<br>

6. **sentry-sdk**
   * Sends error and exception logs to [Sentry](https://sentry.io/).
   * Great for production observability and real-time error tracking.

   ```bash
   pip install sentry-sdk
   ```

   ```python
   import sentry_sdk
   sentry_sdk.init("your-dsn-url")
   ```

<br>

7. **watchtower**
   * Logging handler for Amazon CloudWatch.
   * Useful when deploying to AWS.

   ```bash
   pip install watchtower
   ```

   ```python
   import logging
   import watchtower

   logger = logging.getLogger(__name__)
   logger.addHandler(watchtower.CloudWatchLogHandler())
   ```

<br>

8. **graypy**
   * Sends logs to Graylog over GELF (Graylog Extended Log Format).
   * Useful in centralized logging setups.

   ```bash
   pip install graypy
   ```

<br>

9. **python-json-logger**
   * JSON formatter for standard `logging` module.
   * Helps produce structured logs for ELK/EFK stacks.

   ```bash
   pip install python-json-logger
   ```


## When to Use What?

| **Use Case**                   | **Suggested Library **               |
| ------------------------------ | ------------------------------------ |
| Simple, standard logging       | `logging`                            |
| Minimal setup and elegance     | `Loguru`                             |
| Structured logging (JSON, ELK) | `structlog`, `python-json-logger`    |
| Centralized cloud logging      | `watchtower`, `graypy`, `sentry-sdk` |
| Better config visualization    | `logging-tree`                       |
| Replacing standard logging     | `logbook`                            |
