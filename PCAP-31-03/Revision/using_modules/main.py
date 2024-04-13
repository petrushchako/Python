print(f"\t__name__ in main.py:\t{__name__}")
print("Importing 'helpers' from 'main'")
import helpers
from helpers import extract_lower as e_low, extract_upper




hw = ["HELLO", "world"]


print(helpers.extract_upper(hw))
print(helpers.extract_lower(hw))


print("Importing 'extras' from 'main'")
import extras

print(f"Uppercase letter: {extract_upper(extras.name)}")
print(f"Lowercase letter: {e_low(extras.name)}")