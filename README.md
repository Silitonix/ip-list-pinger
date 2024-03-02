## Introduction (Markdown Format)

This document, written in Markdown format, describes a Python application designed to ping multiple IP addresses listed in a text file on Linux systems. The application can handle IP addresses specified in CIDR notation (e.g., "0.0.0.0/24").

## Usage

### Requirements

* Python 3 (pre-installed on most Linux distributions)
* `ipaddress` module (optional, for CIDR notation support)

**Installing `ipaddress` (if needed):**

```bash
pip install ipaddress
```

### Script File

The script is provided as a Python file (e.g., `ping_cidr.py`). 

### Input File

Create a text file containing IP addresses in the following format:

```
0.0.0.0/24  # Example with CIDR notation
1.1.1.1/24  # Another example with CIDR notation
10.0.0.1     # Single IP address
```

**Note:** Ensure the filename matches what you provide as an argument when running the script.

### Running the Script

Open a terminal and navigate to the directory containing the script and input file. Use the following command, replacing `<filename>` with the actual filename:

```bash
python ping_cidr.py <filename>
```

**Example:**

```bash
python ping_cidr.py ip_addresses.txt
```

This will process the IP addresses from "ip_addresses.txt" and print the following for each IP:

* **Reachable:** If the ping was successful.
* **Not Reachable:** If the ping failed.

## Explanation

The script functions as follows:

1. **Imports:** Necessary modules (`os`, `subprocess`, and potentially `ipaddress`) are imported.
2. **`ping_ip_address` Function:** This function attempts to ping a single IP address and returns `True` if successful, `False` otherwise.
3. **`main` Function:**
   - The script checks for a valid number of arguments (script name and filename).
   - It retrieves the filename from the argument.
   - The script opens the file and reads IP addresses line by line.
   - For each IP address with CIDR notation:
     - It splits the address into network and netmask using `split("/")`.
     - It creates a network object using `ipaddress.ip_network` (if the module is installed).
     - It iterates through individual hosts within the network.
   - For each single IP address (or each host in a network):
     - It calls `ping_ip_address` and prints the reachability result.

## Conclusion

This Python application provides a convenient way to ping multiple IP addresses from a text file, handling CIDR notation for efficient network scanning. 
