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
    print("-------Operating System Information-------")
    print("Operating System Type:", os.name)
    print("\nOperating Sysyem:", platform.system())
    print("\nOperating System Version:", platform.release())
    print("\nSystem Bit Architecture:", platform.architecture())
    print("\nComputer Name:", platform.node())
    hostname = platform.node()
    IPAddr = socket.gethostbyname(hostname)
    print("\nCompiter IP Address:", IPAddr)
    print("\n")

    # Fetch Network Information
    print("-------Network Status-------")
    table = PrettyTable(["Network", "Status", "Speed"])
    for key in psutil.net_if_stats().key():
        name = key
        up = "Up" if psutil.net_if_stats()[key].isup else "Down"
        speed = psutil.net_if_stats()[key].speed
        table.add_row([name, up, speed])
    print(table)
    print("\n")

    # Fetch the memory information
    print("-------Memory Usage-------")
    memory_table = PrettyTable(["Total(GB)", "Used(GB)", "Available(GB)", "Percentage"])
    vm = psutil.vitual_memory()
    memory_table.add_row([
        f"{vm.total / 1e9:.3f}",
        f"{vm.used / 1e9:.3f}",
        f"{vm.available / 1e9:.3f}",
        vm.percent
    ])
    print(memory_table)
    print("\n")

    # Fetch the disk information
    print("-------Disk Usage------")
    disk_table = PrettyTable(["Total Usage(GB)","Used(GB)","Free(GB)","Percentage"])
    disk = psutil.disk_usage('/')
    disk_table.add_row([
        f"{disk.total / 1e9:.3f}",
        f"{disk.used / 1e9:.3f}",
        f"{disk.free / 1e9:.3f}",
        disk.percent
    ])
    print(disk_table)
    print("\n")

    