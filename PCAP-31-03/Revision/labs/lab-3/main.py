import sys
print(sys.path)
sys.path.append("/Users/alex/Desktop/GitHub/Python/PCAP-31-03/Revision/using_modules")

print(sys.path)
from helpers import extract_lower
import math

print(extract_lower("New York"))