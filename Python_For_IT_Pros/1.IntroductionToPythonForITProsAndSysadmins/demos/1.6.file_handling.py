file_path = "example.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError as e:
    print("Error: ", e)