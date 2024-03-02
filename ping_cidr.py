import os
import subprocess
import sys

def ping_ip_address(ip_address):
    """Pings an IP address and returns True if successful, False otherwise."""
    try:
        response = subprocess.check_output(["ping", "-c", "1", ip_address], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    """Reads IP addresses from a specified file and pings each one."""

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        exit(1)

    filename = sys.argv[1]

    with open(filename, "r") as file:
        ip_addresses = file.read().splitlines()

    for ip_address in ip_addresses:
      network, netmask = ip_address.split("/")
      net = ipaddress.ip_network(f"{network}/{netmask}")

      for host in net.hosts():
        if ping_ip_address(str(host)):
          print(f"{host} is reachable")
        else:
          print(f"{host} is not reachable")

if __name__ == "__main__":
    try:
        import ipaddress
    except ImportError:
        print("The 'ipaddress' module is required. Please install it using pip:")
        print("pip install ipaddress")
        exit()

    main()

