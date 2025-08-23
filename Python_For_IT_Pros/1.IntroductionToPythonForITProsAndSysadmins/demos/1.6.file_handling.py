# Output example
output_path = "output.txt"
message = "This is my message in the bottle\n"

try:
    with open(output_path, "w") as file:
        file.write(message)
    print(f"Data witten to a {output_path}")
except Exception as e:
    print("Error: ", e)


# Reading a file
# If file does not exist r/r+ the FileNotFoundError exception will be rissen
file_path = "example.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError as e:
    print("Error: ", e)
finally:
    print("Exiting application")


def openFileA():
    ' ' ' Pointer manipulation ' ' '
    # Opening file in 'a' mode, sets pointer to the end of the file
    with open(output_path, "a+") as file:
        position = file.tell()
        print(f"Content of the file (starting at position {position}):\n{file.read()}") 
        file.seek(0)
        position = file.tell()
        print(f"Content of the file (starting at position {position}):\n{file.read()}")

def openFileRB():
    """        
    seek(offset, whence)
    offset → number of bytes to move
    whence → reference point:
        0 = from start of file (default)
        1 = from current position
        2 = from end of file
    """
    with open(output_path, "rb") as file:
        
        # Switch poisiton of the point to 7 characters from the end and read the message
        file.seek(-7, 2)
        print(file.read())


print(openFileRB.__doc__)
print(openFileA.__doc__)