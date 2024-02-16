# Object Oriented programming

## The foundations of OOP
- Python is a universal tool for both object and procedural programming.
- Procedural vs. the object-oriented approach

  In the procedural approach, it's possible to distinguish two different and completely separate worlds: the world of data, and the world of code. The world of data is populated with variables of different kinds, while the world of code is inhabited by code grouped into modules and functions.
    <br><br>
  The object approach suggests a completely different way of thinking. The data and the code are enclosed together in the same world, divided into classes.
  Every class is like a recipe which can be used when you want to create a useful object (this is where the name of the approach comes from). You may produce as many objects as you need to solve your problem.

<br><br>
### Inheritance
When a class is derived from another class, their relation is named **inheritance**. The class which derives from the other class is named a **subclass**. The second side of this relation is named **superclass**. A way to present such a relation is an **inheritance diagram**, where:
- superclasses are always presented **above** their subclasses;
- relations between classes are shown as arrows directed **from the subclass toward its superclass**.

<br><br>
### What does an object have?
  The object programming convention assumes that every existing object may be equipped with three groups of attributes:
  - an object has a **name** that uniquely identifies it within its home namespace (although there may be some anonymous objects, too)
  - an object has a **set of individual properties** which make it original, unique, or outstanding (although it's possible that some objects may have no properties at all)
  - an object has a **set of abilities to perform specific activities**, able to change the object itself, or some of the other objects.

<br>
There is a hint (although this doesn't always work) which can help you identify any of the three spheres above. Whenever you describe an object and you use:

a noun – you probably define the object's name;
an adjective – you probably define the object's property;
a verb – you probably define the object's activity.

![](../img/M4.4.png)

<br><br>
### Implementation
To define a Python class, you need to use the class keyword. For example:
```python
class This_Is_A_Class:
     pass
```

To create an object of the previously defined class, you need to use the class as if it were a function. For example:
```python
this_is_an_object = This_Is_A_Class()
```
<br><br><br>
## A short journey from procedural to object approach

### What is a stack?
**A stack is a structure developed to store data in a very specific way**. Imagine a stack of coins. You aren't able to put a coin anywhere else but on the top of the stack.

Similarly, you can't get a coin off the stack from any place other than the top of the stack. If you want to get the coin that lies on the bottom, you have to remove all the coins from the higher levels.

The alternative name for a stack (but only in IT terminology) is **LIFO**.

It's an abbreviation for a very clear description of the stack's behavior: **Last In - First Out**. The coin that came last onto the stack will leave first.

**A stack is an object** with two elementary operations, conventionally named **push** (when a new element is put on the top) and **pop** (when an existing element is taken away from the top).

Stacks are used very often in many classical algorithms, and it's hard to imagine the implementation of many widely used tools without the use of stacks.

![](../img/M4.5.png)

Let's implement a stack in Python. This will be a very simple stack, and we'll show you how to do it in two independent approaches: procedural and objective.

Let's start with the first one.

**The stack - the procedural approach**

First, you have to decide how to store the values which will arrive onto the stack. We suggest using the simplest of methods, and employing a list for this job. Let's assume that the size of the stack is not limited in any way. Let's also assume that the last element of the list stores the top element.

```python
stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
```




<br><br><br>
**The stack - the OOP approach**


```python
class Stack:
    def __init__(self):
        self.__stack_list = []

stack_object = Stack()
print(len(stack_object.__stack_list))
```
<br>

**Private variables**

When any class component has a **name starting with two underscores (__), it becomes private** - this means that it can be accessed only from within the class.

You cannot see it from the outside world. This is how Python implements the **encapsulation** concept.

Run the program to test our assumptions - an `AttributeError` exception should be raised.


**The object approach: a stack from scratch**

```python
class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
```
<br><br>
**Extend stack class with subclass**

- Add a new class for handling stacks.

- The new class should be able to evaluate the sum of all the elements currently stored on the stack.

- `Stack.__init__(self)`

    Contrary to many other languages, Python forces you to explicitly invoke a superclass's constructor. Omitting this point will have harmful effects - the object will be deprived of the __stack_list list. Such a stack will not function properly.

    you have to point to the object (the class's instance) which has to be initialized by the constructor - this is why you have to specify the argument and use the `self` variable here; note: **invoking any method (including constructors) from outside the class never requires you to put the `self` argument at the argument's list** - invoking a method from within the class demands explicit usage of the `self` argument, and it has to be put first on the list.

```python
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
#######################################
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
#######################################
stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
```

<br><br>

## Propoerties

### Instance variables
In general, a class can be equipped with two different kinds of data to form a class's properties. You already saw one of them when we were looking at stacks.

This kind of class property exists when and only when it is explicitly created and added to an object. As you already know, this can be done during the object's initialization, performed by the constructor.

Moreover, it can be done in any moment of the object's life. Furthermore, any existing property can be removed at any time.

Such an approach has some important consequences:

- different objects of the same class **may possess different sets of properties**;
- there must be a way to **safely check if a specific object owns the property** you want to utilize (unless you want to provoke an exception - it's always worth considering)
- each object c**arries its own set of properties** - they don't interfere with one another in any way.

Such variables (properties) are called **instance variables**.

The word instance suggests that they are closely connected to the objects (which are class instances), not to the classes themselves. Let's take a closer look at them.

Here is an example:

```python
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
```
Output:
```python
{'first': 1}
{'second': 3, 'first': 2}
{'third': 5, 'first': 4}
```

**Mangling hidden properties**

Take a look at the modified example in the editor.

It's nearly the same as the previous one. The only difference is in the property names. We've **added two underscores (__)** in front of them.

```python
class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val

example_object_1 = ExampleClass()

example_object_2 = ExampleClass(2)
example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
```

As you know, such an addition makes the instance variable **private** - it becomes inaccessible from the outer world.

The actual behavior of these names is a bit more complicated, so let's run the program. This is the output:

```python
{'_ExampleClass__first': 1}
{'_ExampleClass__first': 2, '_ExampleClass__second': 3}
{'_ExampleClass__first': 4, '__third': 5}
```

When Python sees that you want to add an instance variable to an object and you're going to do it inside any of the object's methods, it **mangles the operation** in the following way:

- it puts a class name before your name;
- it puts an additional underscore at the beginning.

This is why the `__first` becomes `_ExampleClass__first`.

**The name is now fully accessible from outside the class**. You can run a code like this:

```python
print(example_object_1._ExampleClass__first)
```

and you'll get a valid result with no errors or exceptions.

As you can see, making a property private is limited.

**The mangling won't work if you add a private instance variable outside the class code**. In this case, it'll behave like any other ordinary property.


<br><br>
### Class variables

A class variable is **a property which exists in just one copy and is stored outside any object**.

Note: no instance variable exists if there is no object in the class; a class variable exists in one copy even if there are no objects in the class.

Class variables are created differently to their instance siblings. The example will tell you more:

```python
class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)
```
Running the code will cause the following output:
```python
{'_ExampleClass__first': 1} 3
{'_ExampleClass__first': 2} 3
{'_ExampleClass__first': 4} 3
```
Two important conclusions come from the example:

- class variables **aren't shown in an object's** __dict__ (this is natural as class variables aren't parts of an object) but you can always try to look into the variable of the same name, but at the class level – we'll show you this very soon;
- a class variable **always presents the same value** in all class instances (objects)


<br><br>
### Check Attribute existence

Python's attitude to object instantiation raises one important issue - in contrast to other programming languages, **you may not expect that all objects of the same class have the same sets of properties**.

```python
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)
```

The object created by the constructor can have only one of two possible attributes: `a` or `b`.

Executing the code will produce the following output:

```python
1
Traceback (most recent call last):
  File ".main.py", line 11, in 
    print(example_object.b)
AttributeError: 'ExampleClass' object has no attribute 'b'
```

As you can see, accessing a non-existing object (class) attribute causes an `AttributeError` exception.


The try-except instruction gives you the chance to avoid issues with non-existent properties.
```python
example_object = ExampleClass(1)
try:
    print(example_object.a)
except AttributeError:
    print(example_object.b)
```


### `hasattr`
Fortunately, there is one more way to cope with the issue.

Python provides a function which is able to safely check if any object/class contains a specified property. The function is named hasattr, and expects two arguments to be passed to it:
- the class or the object being checked;
- the name of the property whose existence has to be reported (note: it has to be a string containing the attribute name, not the name alone)

The function returns `True` or `False`.

This is how you can utilize it:
```python
from random import randint()
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = "Odd number"
        else:
            self.b = "Even number"

example_object = ExampleClass(randint(1,2))

if hasattr(example_object, 'a'):
    print(example_object.a)
else:
    print(example_object.b)
```

Don't forget that the `hasattr()` function can operate on classes, too. You can use it **to find out if a class variable is available**, just like here in the example in the editor.

The function returns `True` if the specified class contains a given attribute, and `False` otherwise.

Can you guess the code's output? Run it to check your guesses.


And one more example - look at the code below and try to predict its output:

```python
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b')) # True
print(hasattr(example_object, 'a')) # True
print(hasattr(ExampleClass, 'b')) # True
print(hasattr(ExampleClass, 'a')) # False
```
<br><br>
## Methods

As you already know, a method is a function embedded inside a class.

There is one fundamental requirement - a **method is obliged to have at least one parameter** (there are no such thing as parameterless methods - a method may be invoked without an argument, but not declared without parameters).

The first (or only) parameter is usually named `self`. We suggest that you follow the convention - it's commonly used, and you'll cause a few surprises by using other names for it.

The name `self` suggests the parameter's purpose - **it identifies the object for which the method is invoked**.


If you're going to invoke a method, you mustn't pass the argument for the self parameter - Python will set it for you.

If you want the method to accept parameters other than self, you should:

- place them after self in the method's definition;
- deliver them during invocation without specifying self (as previously)

<br><br>
The `self` parameter is used **to obtain access to the object's instance and class variables**.

The example shows both ways of utilizing self:

```python
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)

obj = Classy()
obj.var = 3
obj.method()
```

The `self` parameter is also used **to invoke other object/class methods from inside the class**.

Just like here:
```python
class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()

obj = Classy()
obj.method()
```
<br><br>
### Constructor

If you name a method like this: `__init__`, it won't be a regular method - it will be a **constructor**.

The constructor:

- is **obliged to have the `self` parameter** (it's set automatically, as usual);
- **may (but doesn't need to) have more parameters** than just self; if this happens, the way in which the class name is used to create the object must reflect the `__init__` definition;
- **can be used to set up the object**, i.e., properly initialize its internal state, create instance variables, instantiate any other objects if their existence is needed, etc.

Note that the constructor:

- **cannot return a value**, as it is designed to return a newly created object and nothing else;
- **cannot be invoked directly either from the object or from inside the class** (you can invoke a constructor from any of the object's subclasses, but we'll discuss this issue later.)


<br><br>
### The inner life of classes and objects
Each Python class and each Python object is pre-equipped with a set of useful attributes which can be used to examine its capabilities.

- `__dict__`

    Let's observe how it deals with methods - look at the code in the editor.

    Run it to see what it outputs. Check the output carefully.

    Find all the defined methods and attributes. Locate the context in which they exist: inside the object or inside the class.

    ```python
    class Classy:
        varia = 1
        def __init__(self):
            self.var = 2

        def method(self):
            pass

        def __hidden(self):
            pass

    obj = Classy()
    print(obj.__dict__)
    print(Classy.__dict__)
    ```

    Output:
    ```python
    {'var': 2}
    {'__module__': '__main__', 'varia': 1, '__init__': <function Classy.__init__ at 0x7fa566064320>, 'method': <function Classy.method at 0x7fa5660643b0>, '_Classy__hidden': <function Classy.__hidden at 0x7fa566064440>, '__dict__': <attribute '__dict__' of 'Classy' objects>, '__weakref__': <attribute '__weakref__' of 'Classy' objects>, '__doc__': None}
    ```
<br><br>
- `__name__`

    The property contains the **name of the class**. It's nothing exciting, just a string.

    Note: the `__name__` attribute is absent from the object - **it exists only inside classes**.


    If you want to **find the class of a particular object**, you can use a function named type(), which is able (among other things) to find a class which has been used to instantiate any object.

    ```python
    class Classy:
        pass

    obj = Classy()
    print(Classy.__name__)
    print(type(obj).__name__)

    # Will trown an error
    # print(obj.__name__)
    ```
    Output:
    ```python
    Classy
    Classy
    ```
<br><br>
- `__module__`

    __module__ is a string, too - it stores the name of the module which contains the definition of the class.
    `print(Classy.__module__)`

<br><br>
- `__bases__`

    `__bases__` is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.

    The order is the same as that used inside the class definition.

    **Note**:<br> only classes have this attribute - objects don't.

    We've defined a function named `printbases()`, designed to present the tuple's contents clearly.

    Look at the code in the editor. Analyze it and run it. It will output:

    ```python
    class SuperOne:
        pass

    class SuperTwo:
        pass

    class Sub(SuperOne, SuperTwo):
        pass

    def printBases(cls):
        print('( ', end='')

        for x in cls.__bases__:
            print(x.__name__, end=' ')
        print(')')

    printBases(SuperOne)
    printBases(SuperTwo)
    printBases(Sub)
    ```
    Output:
    ```python
    ( object )
    ( object )
    ( SuperOne SuperTwo )
    ```
    **Note**:<br> **a class without explicit superclasses points to object** (a predefined Python class) as its direct ancestor.



<br><br><br>
### Reflection and introspection

All these means allow the Python programmer to perform two important activities specific to many objective languages. They are:

- **introspection**<br> which is the ability of a program to examine the type or properties of an object at runtime;
- **reflection**<br> which goes a step further, and is the ability of a program to manipulate the values, properties and/or functions of an object at runtime.

In other words, you don't have to know a complete class/object definition to manipulate the object, as the object and/or its class contain the metadata allowing you to recognize its features during program execution.

<br><br>
### Investigation classes

What can you find out about classes in Python? The answer is simple – everything.

Both reflection and introspection enable a programmer to do anything with any object, no matter where it comes from.

The function named `incIntsI()` gets an object of any class, scans its contents in order to find all integer attributes with names starting with `i`, and increments them by one.

```python
class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
```
Output:
```python
{'a': 1, 'b': 2, 'i': 3, 'ireal': 3.5, 'integer': 4, 'z': 5}
{'a': 1, 'b': 2, 'i': 4, 'ireal': 3.5, 'integer': 5, 'z': 5}
```


<br><br>
### Inheritance

Inheritance is a common practice (in object programming) of **passing attributes and methods from the superclass (defined and existing) to a newly created class, called the subclass**.

In other words, inheritance is **a way of building a new class, not from scratch, but by using an already defined repertoire of traits**. The new class inherits (and this is the key) all the already existing equipment, but is able to add some new ones if needed.

Thanks to that, it's possible to **build more specialized (more concrete) classes** using some sets of predefined general rules and behaviors.

Two-level inheritance example:
```python
class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass
```


<br><br>
- `issubclass()`

  Python offers a function which is able to **identify a relationship between two classes**, and although its diagnosis isn't complex, 
  it can check if a particular class is a subclass of any other class.

  This is how it looks:

  ```python
  issubclass(Class1, Class2)
  ```
  The function returns `True` if `Class1` is a subclass of `Class2`, and `False` otherwise.

  ```python
  class Vehicle:
      pass
  
  class LandVehicle(Vehicle):
      pass
  
  class TrackedVehicle(LandVehicle):
      pass
  
  for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
      for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
          print(issubclass(cls1, cls2), end="\t")
      print()
  ```
  Result:
  
  |is a subclass of|Vehicle|LandVehicle|TrackedVehicle|
  |---|---|---|---|
  |Vehicle|`True`|`False`|`False`|
  |LandVehicle|`True`|`True`|`False`|
  |TrackedVehicle|`True`|`True`|`True`|

  > There is one important observation to make: **each class is considered to be a subclass of itself.**

<br><br>
- `isinstance()`
  As you already know, **an object is an incarnation of a class**. This means that the object is like a cake baked using a recipe which is included inside the class.
  
  This can generate some important issues.
  
  Let's assume that you've got a cake (e.g., as an argument passed to your function). You want to know what recipe has been used to make it. Why? Because you want to know what to expect from it, e.g., whether it contains nuts or not, which is crucial information to some people.

  Similarly, it can be crucial if the object does have (or doesn't have) certain characteristics. In other words, **whether it is an object of a certain class or not**.

  **Being an instance of a class means that the object (the cake) has been prepared using a recipe contained in either the class or one of its superclasses**.

  ```python
  class Vehicle:
    pass
  
  class LandVehicle(Vehicle):
      pass
  
  class TrackedVehicle(LandVehicle):
      pass
  
  my_vehicle = Vehicle()
  my_land_vehicle = LandVehicle()
  my_tracked_vehicle = TrackedVehicle()
  
  for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
      for cls in [Vehicle, LandVehicle, TrackedVehicle]:
          print(isinstance(obj, cls), end="\t")
      print()
  ```
  Output:
  ```python
  True	False	False	
  True	True	False	
  True	True	True
  ```
<br><br>
- `is`
  
  - The `is` operator checks whether two variables (`object_one` and `object_two` here) refer to the same object.

  ```python
    object_one is object_two
  ```
  - Don't forget that variables don't store the objects themselves, but only the handles pointing to the internal Python memory.
  
    ```python
    class SampleClass:
    def __init__(self, val):
        self.val = val

    object_1 = SampleClass(0)
    object_2 = SampleClass(2)
    object_3 = object_1
    object_3.val += 1

    print(object_1 is object_2)
    print(object_2 is object_3)
    print(object_3 is object_1)
    print(object_1.val, object_2.val, object_3.val)

    string_1 = "Mary had a little "
    string_2 = "Mary had a little lamb"
    string_1 += "lamb"

    print(string_1 == string_2, string_1 is string_2)
    ```
    Output:
    ```python
    False
    False
    True
    1 2 1
    True False
    ```




<br><br>
- `__str__`
  
  When Python needs any class/object to be presented as a string (putting an object as an argument in the print() function invocation fits this condition) it tries to invoke a method named __str__() from the object and to use the string it returns.

  The default __str__() method returns the previous string - ugly and not very informative. You can change it just by defining your own method of the name.

  ```python
  class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy


  sun = Star("Sun", "Milky Way")
  print(sun)
  ```
  Output:
  ```python
  Sun in Milky Way
  ```


<br><br><br>
### How Python finds properties and methods

Now we're going to look at how Python deals with inheriting methods.

Take a look at the example in the editor. Let's analyze it:

- there is a class named `Super`, which defines its own constructor used to assign the object's property, named `name`.
- the class defines the `__str__()` method, too, which makes the class able to present its identity in clear text form.
- the class is next used as a base to create a subclass named `Sub`. The `Sub` class defines its own constructor, which invokes the one from the superclass. Note how we've done it: `Super.__init__(self, name)`.
- we've explicitly named the superclass, and pointed to the method to invoke `__init__()`, providing all needed arguments.
- we've instantiated one object of class `Sub` and printed it.
```python
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"

class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)

obj1 = Sub("Andy")
print(obj1)
```

The code outputs:
```python 
My name is Andy.

```

- `super()`

    In the last example, we explicitly named the superclass. In this example, we make use of the `super()` function, which **accesses the superclass without needing to know its name**:
    ```python
    class Sub(Super):
        def __init__(self,name):
            super().__init__(name)

    ```
    The `super()` function creates a context in which you don't have to (moreover, you mustn't) pass the self argument to the method being invoked - this is why it's possible to activate the superclass constructor using only one argument.

    Note: you can use this mechanism not only to **invoke the superclass constructor, but also to get access to any of the resources available inside the superclass**.


    - Propagating varaible values via superclass:
  
        ```python
        class Super:
            def __init__(self):
                self.supVar = 11

        class Sub(Super):
            def __init__(self):
                super().__init__()
                self.subVar = 12

        obj = Sub()
        print(obj.subVar) # 12
        print(obj.supVar) # 11
        ```

    - **Property and methoda resolution sequence in Python**
        - It's now possible to formulate a general statement describing Python's behavior.

        - When you try to access any object's entity, Python will try to (in this order):
            - find it **inside the object itself**;
            - find it **in all classes** involved in the object's inheritance line from bottom to top;
            - If both of the above fail, an **exception (`AttributeError`) is raised**.

        ```python
        class Level1:
            variable_1 = 100
            def __init__(self):
                self.var_1 = 101

            def fun_1(self):
                return 102


        class Level2(Level1):
            variable_2 = 200
            def __init__(self):
                super().__init__()
                self.var_2 = 201
            
            def fun_2(self):
                return 202


        class Level3(Level2):
            variable_3 = 300
            def __init__(self):
                super().__init__()
                self.var_3 = 301

            def fun_3(self):
                return 302


        obj = Level3()

        print(obj.variable_1, obj.var_1, obj.fun_1())
        print(obj.variable_2, obj.var_2, obj.fun_2())
        print(obj.variable_3, obj.var_3, obj.fun_3())
        ```

- **Inheritance with duplication**

    - **Three-level inheritance**
      ```python
      class Level1:
          var = 100
          def fun(self):
              return 101

      class Level2(Level1):
          var = 200
          def fun(self):
              return 201

      class Level3(Level2):
          pass

      obj = Level3()
      print(obj.var, obj.fun())
      ```


      Both, `Level1` and `Level2` classes define a method named `fun()` and a property named `var`. Does this mean that the `Level3` class object will be able to access two copies of each entity? **Not at all**.

      **The entity defined later (in the inheritance sense) overrides the same entity defined earlier**. 
      
      This is why the code produces the following output:
      `200 201`   

    - **Multi inheritance**

        ```python
        class Left:
            var = "L"
            var_left = "LL"
            def fun(self):
                return "Left"

        class Right:
            var = "R"
            var_right = "RR"
            def fun(self):
                return "Right"

        class Sub(Left, Right):
            pass

        obj = Sub()
        print(obj.var, obj.var_left, obj.var_right, obj.fun())
        ```

        Python looks for object components in the following order:
        - **inside the object** itself;
        - **in its superclasses**, from bottom to top;
        - if there is more than one class on a particular inheritance path, Python scans them from left to right.

        So the output will be the following:

       - `class Sub(Left, Right):`- >**L LL RR Left**
       - `class Sub(Right, Left):` -> **R LL RR Right**


### Composition

Inheritance is not the only way of constructing adaptable classes. You can achieve the same goals (not always, but very often) by using a technique named composition.

**Composition is the process of composing an object using other different objects**. The objects used in the composition deliver a set of desired traits (properties and/or methods) so we can say that they act like blocks used to build a more complicated structure.

It can be said that:
- **inheritance extends a class's capabilities** by adding new components and modifying existing ones; in other words, the complete recipe is contained inside the class itself and all its ancestors; the object takes all the class's belongings and makes use of them;
- **composition projects a class as a container** able to store and use other objects (derived from other classes) where each of the objects implements a part of a desired class's behavior.

The class - like in the previous example - is aware of how to turn the vehicle, but the actual turn is done by a specialized object stored in a property named `controller`. The `controller` is able to control the vehicle by manipulating the relevant vehicle's parts.

```python
import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)

class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)

class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)

wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)
```

This program dumps all predefined exception classes in the form of a tree-like printout.

Output:
```python
wheels:  True True
wheels:  True False
tracks:  False True
tracks:  False False
```

There are two classes named `Tracks` and `Wheels` - they know how to control the vehicle's direction. There is also a class named `Vehicle` which can use any of the available controllers (the two already defined, or any other defined in the future) - the `controller` itself is passed to the class during initialization.

In this way, the vehicle's ability to turn is composed using an external object, not implemented inside the `Vehicle` class.



<br><br><br>
## Exceptions

Discussing object programming offers a very good opportunity to return to exceptions. The object-oriented nature of Python's exceptions makes them a very flexible tool, able to fit to specific needs, even those you don't yet know about.

Before we dive into the **objective face of exceptions**, we want to show you some syntactical and semantic aspects of how Python treats the try-except block, as it offers a little more than what we have presented so far.

```python
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n
    finally:
        print("It's time to say goodbye")
        return n

print(reciprocal(2))
print(reciprocal(0))
```

Output:
```python
Everything went fine
It's time to say good bye
0.5
Division failed
It's time to say good bye
None
```

<br><br>
**Exceptions are classes**

You probably won't be surprised to learn that **exceptions are classes**. Furthermore, when an exception is raised, an object of the class is instantiated, and goes through all levels of program execution, looking for the except branch that is prepared to deal with it.

```python
try:
    i = int("Hello!")
except Exception as e:
    print(e)
    print(e.__str__())
```

Output:
```python
invalid literal for int() with base 10: 'Hello!'
invalid literal for int() with base 10: 'Hello!'
```

As you can see, the `except` statement is extended, and contains an additional phrase starting with the `as` keyword, followed by an identifier. The identifier is designed to catch the exception object so you can analyze its nature and draw proper conclusions.

The example presents a very simple way of utilizing the received object - just print it out (as you can see, the output is produced by the object's `__str__()` method) and it contains a brief message describing the reason.

```python
def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)
    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)

print_exception_tree(BaseException)
```
Output:
```python
BaseException
   +---Exception
   |   +---TypeError
   |   +---StopAsyncIteration
   |   +---StopIteration
   |   +---ImportError
   |   |   +---ModuleNotFoundError
   |   |   +---ZipImportError
   |   +---OSError
   |   |   +---ConnectionError
   |   |   |   +---BrokenPipeError
   |   |   |   +---ConnectionAbortedError
   |   |   |   +---ConnectionRefusedError
   |   |   |   +---ConnectionResetError
   |   |   +---BlockingIOError
   |   |   +---ChildProcessError
   |   |   +---FileExistsError
   |   |   +---FileNotFoundError
   |   |   +---IsADirectoryError
   |   |   +---NotADirectoryError
   |   |   +---InterruptedError
   |   |   +---PermissionError
   |   |   +---ProcessLookupError
   |   |   +---TimeoutError
   |   |   +---UnsupportedOperation
   |   |   +---ItimerError
   |   +---EOFError
   |   +---RuntimeError
   |   |   +---RecursionError
   |   |   +---NotImplementedError
   |   |   +---_DeadlockError
   |   +---NameError
   |   |   +---UnboundLocalError
   |   +---AttributeError
   |   +---SyntaxError
   |   |   +---IndentationError
   |   |   |   +---TabError
   |   +---LookupError
   |   |   +---IndexError
   |   |   +---KeyError
   |   |   +---CodecRegistryError
   |   +---ValueError
   |   |   +---UnicodeError
   |   |   |   +---UnicodeEncodeError
   |   |   |   +---UnicodeDecodeError
   |   |   |   +---UnicodeTranslateError
   |   |   +---UnsupportedOperation
   |   +---AssertionError
   |   +---ArithmeticError
   |   |   +---FloatingPointError
   |   |   +---OverflowError
   |   |   +---ZeroDivisionError
   |   +---SystemError
   |   |   +---CodecRegistryError
   |   +---ReferenceError
   |   +---MemoryError
   |   +---BufferError
   |   +---Warning
   |   |   +---UserWarning
   |   |   +---DeprecationWarning
   |   |   +---PendingDeprecationWarning
   |   |   +---SyntaxWarning
   |   |   +---RuntimeWarning
   |   |   +---FutureWarning
   |   |   +---ImportWarning
   |   |   +---UnicodeWarning
   |   |   +---BytesWarning
   |   |   +---ResourceWarning
   |   +---Error
   +---GeneratorExit
   +---SystemExit
   +---KeyboardInterrupt

```