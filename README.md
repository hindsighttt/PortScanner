# Port Scanner

This script is a lightweight and concurrent port scanner that can be used to scan ports on a range of IP addresses.

## Features

- Scans a range of IP addresses.
- Scans a specified range of ports.
- Utilizes threading for concurrent scanning.
- Outputs open ports to a specified file.
- Uses colorama for colored terminal output.
- Has a Flask GUI

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

## Commonly Used Ports

- `20/21` - FTP (File Transfer Protocol) for file transfers.
- `22` - SSH (Secure Shell) for secure remote logins.
- `23` - Telnet for unencrypted remote logins.
- `25` - SMTP (Simple Mail Transfer Protocol) for email delivery.
- `53` - DNS (Domain Name System) for resolving hostnames.
- `80` - HTTP (Hypertext Transfer Protocol) for web traffic.
- `110` - POP3 (Post Office Protocol version 3) for email retrieval.
- `143` - IMAP (Internet Message Access Protocol) for email retrieval.
- `443` - HTTPS (HTTP Secure) for secure web traffic.
- `465/587` - SMTPS (SMTP Secure) for secure email delivery.
- `993` - IMAPS (IMAP Secure) for secure email retrieval.
- `995` - POP3S (POP3 Secure) for secure email retrieval.
- `3306` - MySQL for database access.
- `3389` - RDP (Remote Desktop Protocol) for Windows remote desktop.
- `5432` - PostgreSQL for database access.
- `5900` - VNC (Virtual Network Computing) for screen sharing.
- `8080` - HTTP alternative, often used for web proxies or secondary web servers.

## Noteworthy Ports

- `137-139` - NetBIOS/Windows network file sharing.
- `161/162` - SNMP (Simple Network Management Protocol) for network management.
- `445` - SMB (Server Message Block) for Windows network file sharing (also used by the WannaCry ransomware).
- `1433/1434` - Microsoft SQL Server for database access.
- `1521` - Oracle database access.
- `5060/5061` - SIP (Session Initiation Protocol) for VoIP (Voice over IP) signaling.
- `6000` - X11 (used for Unix/Linux graphical systems).

## Ports Associated with Vulnerabilities

- `139/445` - Historically associated with Windows vulnerabilities.
- `1521` - Known for Oracle database exploits.
- `3306` - Targeted for MySQL database exploits.
- `3389` - Known vulnerabilities in RDP.
- `8080` - Often targeted as an alternate web server port.

Note that this is not an exhaustive list, and the significance of a port can change as new services become popular and old ones fall out of use. Additionally, many applications can be configured to use non-standard ports, which means that any port can potentially be "interesting" depending on the context and the network configuration.

## Notes

- The script uses threading to improve scan performance. However, creating a large number of threads may lead to resource exhaustion. Please adjust the range of IP addresses and ports according to your system's capabilities.
- The color-coded console output is optimized for terminals that support ANSI colors.

## Disclaimer

Port scanning can be perceived as an intrusive activity by network administrators and may be illegal in some contexts. Always ensure you have authorization before scanning networks that you do not own or have explicit permission to test.
