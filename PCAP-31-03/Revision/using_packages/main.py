from helpers.strings import extract_lower as extr_low, extract_upper as extr_up
from helpers import variables
import helpers.strings

print(variables.name)
print(extr_up(variables.name))


import helpers
city = "New York"
print(city)
print(''.join(helpers.strings.extract_upper(city)))
print(''.join(helpers.extract_lower(city)))
print(''.join(helpers.extract_upper(city)))