__all__ = ['extract_lower', 'extract_upper']
# Alternative approach to hide values is to use undersore ax prefix when naming entitites. 
# However, you will still be able to import those entities (_extract_upper()) by using 'from helper import _extract_upper'

def extract_upper(phrase):
    """
    extract_upper takes in iterables(string) and return a list containing only rhe uppercase letters

    >>> extract_upper("Hello BOB")
    ['H', 'B', 'O', 'B']
    """
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    """
    extract_lower takes in iterables(string) and return a list containing only rhe lowercase letters

    >>> extract_lower("Hello BOB")
    ['e', 'l', 'l', 'o']
    """
    return list(filter(str.islower, phrase))

if __name__ == "__main__":
    print("Hello from strings.py")