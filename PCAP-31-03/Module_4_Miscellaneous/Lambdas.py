# Simple lambda example
def increment_fn1(x):
    return x + 1

print(increment_fn1) # <function increment_fn at 0x109f4c900>

increment_fn2 = lambda x:x+1

print(increment_fn2) # <function <lambda> at 0x10c1b99d0>

# Invoke lambda function
print("Invoke Lambda function: increment_fn2(2) -> ", increment_fn2(2))