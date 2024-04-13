import helpers
from helpers import extract_lower as e_low, extract_upper

hw = ["HELLO", "world"]


print(helpers.extract_upper(hw))
print(helpers.extract_lower(hw))



name = "Keith Thomson"

print(f"Uppercase letter: {extract_upper(name)}")
print(f"Lowercase letter: {e_low(name)}")