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