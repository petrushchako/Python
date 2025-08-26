import subprocess

def createFile(filename):
    res = subprocess.run(f"touch {filename}", shell=True, capture_output=True, text=True)
    print(subprocess.run(f"ls -al | grep {filename}", shell=True, capture_output=True, text=True).stdout)
    return res.stdout


if __name__ == "__main__":
    createFile("2.2.network.py")