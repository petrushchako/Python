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


### What does an object have?
  The object programming convention assumes that every existing object may be equipped with three groups of attributes:
  - an object has a **name** that uniquely identifies it within its home namespace (although there may be some anonymous objects, too)
  - an object has a **set of individual properties** which make it original, unique, or outstanding (although it's possible that some objects may have no properties at all)
  - an object has a **set of abilities to perform specific activities**, able to change the object itself, or some of the other objects.

<br><br>
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