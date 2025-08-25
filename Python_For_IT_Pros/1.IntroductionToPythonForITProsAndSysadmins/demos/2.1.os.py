import os
import subprocess
import datetime


# List current working directory(cwd) or pwd in shell
current_directory = os.getcwd()
cwd = current_directory.split("/")
print(f"Current working directory is: {cwd[-1]}")

# List content of cwd
dir_content = os.listdir(current_directory)
print(f"Content of the current working directory is:")
for x in dir_content:
    print(f"\t{x}")

def makeDirectory(dir_name):
    os.mkdir(dir_name)
    print(f"\tCreated new directory {dir_name}")

def renameDirectory(current_name, new_name):
    os.rename(current_name, new_name)
    print(f"\tDirectory {current_name} renamed to {new_name}")

def deleteDirectory(dir_name):
    os.rmdir(dir_name)
    print(f"\tRemoved directory {dir_name}")

if __name__ == "__main__":
    user = os.getenv("USER")
    print(f"Hi, {user}!\nStaring folder operations:")
    makeDirectory("new-folder")
    renameDirectory("new-folder", "new-folder1")
    deleteDirectory("new-folder1")
    

