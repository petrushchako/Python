# Miscellaneous

## Generators, iterators, and closures

### Generators (Iterators)
A Python generator is a **piece of specialized code able to produce a series of values, and to control the iteration process**. This is why generators are very often called **iterators**, and although some may find a very subtle distinction between these two, we'll treat them as one.

- `range()`

    The `range()` function is a generator, which is an iterator.

    What is the difference?

    A function returns one, well-defined value - it may be the result of a more or less complex evaluation of, e.g., a polynomial, and is invoked once - only once.

    A generator returns a series of values, and in general, is (implicitly) invoked more than once.


    ```python
    for i in range(5):
        print(i) #0 1 2 3 4
    ```
- **Implement iterrator**

    The **iterator protocol is a way in which an object should behave to conform to the rules imposed by the context of the** `for` **and** `in` **statements**. An object conforming to the iterator protocol is called an **iterator**.

    An iterator must provide two methods:
    - `__iter__()` which should **return the object itself** and which is invoked once (it's needed for Python to successfully start the iteration)
    - `__next__()` which is intended to **return the next value** (first, second, and so on) of the desired series - it will be invoked by the `for`/`in` statements in order to pass through the next iteration; if there are no more values to provide, the method should **raise the** `StopIteration` **exception**.

    ```python
    class Fib:
        def __init__(self, nn):
            print("__init__")
            self.__n = nn
            self.__i = 0
            self.__p1 = self.__p2 = 1

        def __iter__(self):
            print("__iter__")
            return self

        def __next__(self):
            print("__next__")				
            self.__i += 1
            if self.__i > self.__n:
                raise StopIteration
            if self.__i in [1, 2]:
                return 1
            ret = self.__p1 + self.__p2
            self.__p1, self.__p2 = self.__p2, ret
            return ret


    for i in Fib(10):
        print(i)
    ```

    Output:
    ```python
    __init__
    __iter__
    __next__
    1
    __next__
    1
    __next__
    2
    __next__
    3
    __next__
    5
    __next__
    8
    __next__
    13
    __next__
    21
    __next__
    34
    __next__
    55
    __next__
    ```

    We've built the `Fib` iterator into another class (we can say that we've composed it into the `Class` class). It's instantiated along with `Class`'s object.

    The object of the class may be used as an iterator when (and only when) it positively answers to the `__iter__` invocation - this class can do it, and if it's invoked in this way, it provides an object able to obey the iteration protocol.

    This is why the output of the code is the same as previously, although the object of the `Fib` class isn't used explicitly inside the `for` loop's context.

    ```python
    class Fib:
        def __init__(self, nn):
            self.__n = nn
            self.__i = 0
            self.__p1 = self.__p2 = 1

        def __iter__(self):
            print("Fib iter")
            return self

        def __next__(self):
            self.__i += 1
            if self.__i > self.__n:
                raise StopIteration
            if self.__i in [1, 2]:
                return 1
            ret = self.__p1 + self.__p2
            self.__p1, self.__p2 = self.__p2, ret
            return ret

    class Class:
        def __init__(self, n):
            self.__iter = Fib(n)

        def __iter__(self):
            print("Class iter")
            return self.__iter;

    object = Class(8)
    ```
    Output:
    ```python
    Class iter
    1
    1
    2
    3
    5
    8
    13
    21
    ```

