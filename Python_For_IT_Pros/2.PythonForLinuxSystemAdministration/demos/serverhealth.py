# Import the required libraries
# Ensure psutil is installed before running this script.
# To install run pip install psutil
import psutil
import os
import platform
import time
import socket
from subprocess import call
# Ensure prettytable is installed before running this script.
# To install run pip install prettytable

from prettytable import PrettyTable

# Run infinite loop to check server health

while True:
    # Clear the screen using a bash command
    call('clear')

    print("="*20, " Server Health", "="*20)

    # PrettyTable is used to print data in the terminal
    # t = PrettyTable(<list of headings>)
    # t.add_row(<list of cells in the row>)

    # Server OS info
    print("\n")
    print("-------Operating System Information------")
    print("Operating System Type:", os.name)
    print("\nOperating Sysyem:", platform.system())
    print("\nOperating System Version:", platform.release())
    print("\nSystem Bit Architecture:", platform.architecture())
    print("\nComputer Name:", platform.node())
    hostname = platform.node()
    IPAddr = socket.gethostbyname(hostname)
    print("\nCompiter IP Address:", IPAddr)
    print("\n")