# Selected Python modules (platform)

### How to know where you are?
Sometimes, it may be necessary to find out information unrelated to Python. For example, you may need to know the location of our program within the greater environment of the computer. Imagine your program's environment as a pyramid consisting of a number of layers or platforms.

### The layers are:
* Your (running) code is located at the top of it;
* Python, or more precisely, its runtime environment, lies directly below it;
* The next layer of the pyramid is filled with the OS (operating system) - Python's environment provides some of its functionalities using the operating system's services; Python, although very powerful, isn't omnipotent - it's forced to use many helpers if it's going to process files or communicate with physical devices;
* The bottom-most layer is hardware - the processor (or processors), network interfaces, human interface devices (mouse, keyboards, etc.) and all other machinery needed to make the computer run; the OS knows how to drive it, and uses lots of tricks to conduct all parts in a consistent rhythm.

<br><br>

This means that some of your (or rather your program's) actions have to travel a long way to be successfully performed - imagine that:
* **your code** wants to create a file, so it invokes one of Python's functions;
* **Python** accepts the order, rearranges it to meet local OS requirements, which is like putting the stamp "approved" on your request, and sends it down (this may remind you of a chain of command)
* the **OS** checks if the request is reasonable and valid (e.g., whether the file name conforms to some syntax rules) and tries to create the file; such an operation, seemingly very simple, isn't atomic - it consists of many minor steps taken by...
* the **hardware**, which is responsible for activating storage devices (hard disk, solid state devices, etc.) to satisfy the OS's needs.

Usually, you're not aware of all that fuss - you want the file to be created and that's that.

But sometimes you want to know more for example, the name of the OS which hosts Python,
and some characteristics describing the hardware that hosts the OS.

There is a module providing some means to allow
you to know where you are and what
components work for you. The module is named **platform**. We'll show you some of the functions
it provides to you.

<br><br><br>

## Platform

Selected functions from the platform module

### The platform function

The platform module lets you access the underlying platform's data, i.e., hardware, operating system, and interpreter version information.

There is a function that can show you all the underlying layers in one glance, named platform, too. It just returns a string describing the environment; thus, its output is rather addressed to humans than to automated processing (you'll see it soon).

This is how you can invoke it:
```python
platform(aliased = False, terse = False)
```

And now:

* **aliased** → when set to ``` True ``` (or any non-zero value) it may cause the function to present the alternative underlying layer names instead of the common ones;
* **terse** → when set to ```True``` (or any non-zero value) it may convince the function to present a briefer form of the result (if possible)


## Sample output from: Intel x86 + Windows ® Vista (32 bit):
```python
Windows-Vista-6.0.6002-SP2
Windows-Vista-6.0.6002-SP2
Windows-Vista
```
<br><br>

## The `machine()` function

Sometimes, you may just want to know the generic name of the processor which runs your OS together with Python and your code - a function named **machine()** will tell you that. As previously, the function returns a string.

Again, we ran the sample program on **Intel x86 + Windows ® Vista (32 bit)**:
```python
from platform import machine

print(machine()) #output: x86
```
<br><br>

## The `processor()` function

The **processor()** function returns a string filled with the real processor name (if possible).

Once again, we ran the sample program on **Intel x86 + Windows ® Vista (32 bit)**:
```python
from platform import processor
print(processor()) #output: x86
```
<br><br>

## The `system()` function

A function named **system()** returns the generic OS name as a string.

Our example platforms presented themselves like this:

```python
from platform import system
print(system()) #output: Windows
```

<br><br>

## The `version()` function

The OS version is provided as a string by the version() function.

Run the code and check its output. This is what we got on Intel x86 + Windows ® Vista (32 bit):
```python
from platform import version
print(version()) #6.0.6002
```

<br><br>

### The `python_implementation()` and the `python_version_tuple()` functions

If you need to know what version of Python is running your code, you can check it using a number of dedicated functions - here are two of them:

* **`python_implementation()`** → returns a string denoting the Python implementation (expect CPython here, unless you decide to use any non-canonical Python branch)
* **`python_version_tuple()`** → returns a three-element tuple filled with:
  - the major part of Python's version;
  - the minor part;
  - the patch level number.

Our example program produced the following output:
```python
from platform import python_implementation, python_version_tuple

print(python_implementation()) #CPython

for atr in python_version_tuple(): #3 characters in tuple
    print(atr)
```
```output
CPython
3
7
10
```

<br><br><br><br>

## Python Module Index
You can read about all standard Python modules here: https://docs.python.org/3/py-modindex.html.

Don't worry - you won't need all these modules. Many of them are very specific.

All you need to do is find the modules you want, and teach yourself how to use them. It's easy.


<br><br>

## Section summary

### Key takeaways

1. A function named `dir()` can show you a list of the entities contained inside an imported module. For example:

```python
import os
dir(os)
```

prints out the list of all the `os` module's facilities you can use in your code.

2. The `math` module couples more than 50 symbols (functions and constants) that perform mathematical operations (like `sine()`, `pow()`, `factorial()`) or providing important values (like `π` and the Euler symbol `e`).

3. The `random` module groups more than 60 entities designed to help you use pseudo-random numbers. Don't forget the prefix "random", as there is no such thing as a real random number when it comes to generating them using the computer's algorithms.


4. The `platform` module contains about 70 functions which let you dive into the underlaying layers of the OS and hardware. Using them allows you to get to know more about the environment in which your code is executed.


5. **Python Module Index** (https://docs.python.org/3/py-modindex.html is a community-driven directory of modules available in the Python universe. If you want to find a module fitting your needs, start your search there.