import os

file_path = 'testFile-TOBEDELETED.txt'

try:
    os.remove(file_path)
    print(f"File '{file_path}' deleted successfully.")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except PermissionError:
    print(f"Permission error: Unable to delete '{file_path}'.")
except Exception as e:
    print(f"An error occurred: {str(e)}")