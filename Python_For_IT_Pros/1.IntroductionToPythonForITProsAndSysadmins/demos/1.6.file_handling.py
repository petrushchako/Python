def writeToFile():
    # Output example
    message = "This is my message in the bottle\n"

    try:
        with open(output_path, "w") as file:
            file.write(message)
        print(f"Data witten to a {output_path}")
    except Exception as e:
        print("Error: ", e)


def openFileA():
    " " " Pointer manipulation " " "
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


# Print single line dosctring
# print(openFileA.__doc__)

# Print multi-line docstring
# print(openFileRB.__doc__)


def readMultiLineFile():
    try:
        with open(output_path, "a+") as file:
            file.writelines(["SOS", "\n", "I'm stuck in tutorial hell :)"])
            file.seek(0)
            lines = file.readlines()
        print("\nLines from the file:")
        for line in lines:
            print(line, end="")
    except FileNotFoundError as fe:
        print("Error: ", fe)
    finally:
        print()


def readMissingFile():
    # Reading a missing file
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


if __name__ == "__main__":
    output_path = "output.txt"
    writeToFile()
    readMultiLineFile()
    openFileA()
    openFileRB()
