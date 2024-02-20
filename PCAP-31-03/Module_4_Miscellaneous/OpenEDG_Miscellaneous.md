# Miscellaneous

## Generators, iterators, and closures

### Generators (Iterators)
A Python generator is a **piece of specialized code able to produce a series of values, and to control the iteration process**. This is why generators are very often called **iterators**, and although some may find a very subtle distinction between these two, we'll treat them as one.
<br><br>
### `range()`

The `range()` function is a generator, which is an iterator.

What is the difference?

A function returns one, well-defined value - it may be the result of a more or less complex evaluation of, e.g., a polynomial, and is invoked once - only once.

A generator returns a series of values, and in general, is (implicitly) invoked more than once.


```python
for i in range(5):
    print(i) #0 1 2 3 4
```
### Implement iterrator

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

<br><br>
### The `yield` statement

The iterator protocol isn't particularly difficult to understand and use, but it is also indisputable that the protocol is rather inconvenient.

The main discomfort it brings is the need to save the state of the iteration between subsequent `__iter__` invocations.

For example, the `Fib` iterator is forced to precisely store the place in which the last invocation has been stopped (i.e., the evaluated number and the values of the two previous elements). This makes the code larger and less comprehensible.

This is why Python offers a much more effective, convenient, and elegant way of writing iterators.

The concept is fundamentally based on a very specific and powerful mechanism provided by the `yield` **keyword**.

You may think of the `yield` keyword as a smarter sibling of the `return` statement, with one essential difference.

Take a look at this function:

```python
def fun(n):
for i in range(n):
    return i
```

It looks strange, doesn't it? It's clear that the for loop has no chance to finish its first execution, as the return will break it irrevocably.
Moreover, invoking the function won't change anything - the for loop will start from scratch and will be broken immediately.
We can say that such a function is not able to save and restore its state between subsequent invocations.
**This also means that a function like this cannot be used as a generator**.

```python
def fun(n):
for i in range(n):
    yield i
```

We've added `yield` instead of `return`. This little amendment **turns the function into a generator**, and executing the `yield` statement has some very interesting effects.

First of all, it provides the value of the expression specified after the `yield` keyword, just like `return`, but doesn't lose the state of the function.

All the variables' values are frozen, and wait for the next invocation, when the execution is resumed (not taken from scratch, like after `return`).

There is one important limitation: such a **function should not be invoked explicitly** as - in fact - it isn't a function anymore; **it's a generator object**.

The invocation will **return the object's identifier**, not the series we expect from the generator.

Due to the same reasons, the previous function (the one with the `return` statement) may only be invoked explicitly, and must not be used as a generator.

<br><br>
### How to build a generator

```python
def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)
```

### How to build your own generator

What if you need a **generator to produce the first n powers of 2**?

Nothing easier. Just look at the code below:

```python
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for i in powers_of_2(5) #1, 2, 4, 8, 16

# List comprehension
t = [x for x in powers_of_2(5)]
print(t) # [1, 2, 4, 8, 16]

# list()
l = list(powers_of_2(3))
print(l) # 1, 2, 4

# in operator
for i in range(20):
    if i in powers_of_2(4):
        print(i)    # 1, 2, 4, 8
```

<br><br>
**Fibanacci number generator**
Now let's see a **Fibonacci number generator**, and ensure that it looks much better than the objective version based on the direct iterator protocol implementation.

Here it is:
```python
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]



# Alternative
def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example: Generate the first 10 Fibonacci numbers
n = 10
fib_sequence = list(fibonacci_sequence(n))
print(fib_sequence)

```

## List comprehension

```python

list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1) # [1, 10, 100, 1000, 10000, 100000]
print(list_2) # [1, 10, 100, 1000, 10000, 100000]
```

### Ternary expression

It's a conditional expression - a way of selecting one of two different values based on the result of a Boolean expression.

```python
x if condition else y
```

```python
the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list) # [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
```

<br><br>
### List comprehension vs generators

Just one change can **turn any list comprehension into a generator**.

```python
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()
```
It's the **parentheses**. The brackets make a comprehension, the parentheses make a generator.

The code, however, when run, produces two identical lines:

```python
1 0 1 0 1 0 1 0 1 0
1 0 1 0 1 0 1 0 1 0
```

How can you know that the second assignment creates a generator, not a list?

There is some proof we can show you. Apply the `len()` function to both these entities.

`len(the_list)` will evaluate to `10`. Clear and predictable. `len(the_generator)` will raise an exception, and you will see the following message:

`TypeError: object of type 'generator' has no len()`


Of course, saving either the list or the generator is not necessary - you can create them exactly in the place where you need them - just like here:

```python
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()
```

Note: the same appearance of the output doesn't mean that both loops work in the same way. In the first loop, the list is created (and iterated through) as a whole - it actually exists when the loop is being executed.

In the second loop, there is no list at all - there are only subsequent values produced by the generator, one by one.

