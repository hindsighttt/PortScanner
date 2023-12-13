# Port Scanner

This script is a lightweight and concurrent port scanner that can be used to scan ports on a range of IP addresses.

## Features

- Scans a range of IP addresses.
- Scans a specified range of ports.
- Utilizes threading for concurrent scanning.
- Outputs open ports to a specified file.
- Uses colorama for colored terminal output.

## Prerequisites

Before you can run this script, you must have the following installed:
- Python 3
- colorama (`pip install colorama`)

## Usage

To use this script, simply provide the starting and ending IP addresses, the range of ports you wish to scan, and an output file name for the results.

```python
start_ip = '172.16.10.1'
end_ip = '172.16.10.255'
start_port = 1
end_port = 5000
output_file = 'output.txt'

scan_ports(start_ip, end_ip, start_port, end_port, output_file)
```

## Functions

- `scan_ports(start_ip, end_ip, start_port, end_port, output_file)`: Initiates the scanning process across the specified IP address range and port range. It manages threading and writes out scan results to the output file.
- `scan_port(ip, port, file)`: Scans an individual IP and port pair. If the port is open on the given IP, it records the result in the output file. This function also prints the result of each scan attempt to the console with color-coded output.

## Notes

- The script uses threading to improve scan performance. However, creating a large number of threads may lead to resource exhaustion. Please adjust the range of IP addresses and ports according to your system's capabilities.
- The color-coded console output is optimized for terminals that support ANSI colors.

## Disclaimer

Port scanning can be perceived as an intrusive activity by network administrators and may be illegal in some contexts. Always ensure you have authorization before scanning networks that you do not own or have explicit permission to test.
