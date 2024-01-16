# Closures
In Python, a closure is a nested or inner function that captures and remembers the values in the enclosing function's local scope, even if the outer function has finished execution. 
This allows the inner function to access the variables and parameters of the outer function, creating a closure over those variables.

Here's a simple example to illustrate closures in Python:

```python
def outer_function(x):
    # This inner function is a closure because it "closes over" the variable 'x'
    def inner_function(y):
        return x + y
    return inner_function

# Create closures
closure_1 = outer_function(10)
closure_2 = outer_function(20)

# Use closures
result_1 = closure_1(5)  # Result: 10 + 5 = 15
result_2 = closure_2(5)  # Result: 20 + 5 = 25
```

In this example, `outer_function` takes a parameter `x` and defines an inner function `inner_function`. The inner_function is a closure because it references the variable x from the outer function's scope. When outer_function is called with different values of x, it returns different closures that remember the specific value of x.

When you later call the closures (closure_1 and closure_2), they remember the values of x from the respective calls to outer_function. This behavior allows closures to retain the state of the outer function even after it has completed execution.

**Key points about closures in Python:**
- **Closures "close over" variables:**<br> Closures have access to variables in the containing (enclosing) function's scope, and they "close over" those variables, meaning they remember their values.
- **Closures are functions:**<br> Closures are essentially functions, and you can pass them around, store them in data structures, and invoke them like regular functions.
- **Closures enable functional programming patterns:**<br> Closures are commonly used in functional programming to create functions with behavior that depends on some persistent state. They are useful for creating decorators, callback functions, and other advanced programming patterns.

Understanding closures is fundamental to writing more advanced and expressive Python code, especially in scenarios where you need functions with encapsulated state.
