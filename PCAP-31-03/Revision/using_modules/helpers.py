__all__ = ['extract_lower', 'extract_upper']
# Alternative approach to hide values is to use undersore ax prefix when naming entitites. 
# However, you will still be able to import those entities (_extract_upper()) by using 'from helper import _extract_upper'

print(f"\t__name__ in helpers.py:\t{__name__}")
def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

if __name__ == "__main__":
    print("Hello from HELPERS")