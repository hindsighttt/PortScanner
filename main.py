import socket
import ipaddress
import threading
from colorama import Fore, Style, init

init()

def scan_ports(start_ip, end_ip, start_port, end_port, output_file):
    ip_range = list(ipaddress.summarize_address_range(ipaddress.IPv4Address(start_ip), ipaddress.IPv4Address(end_ip)))
    
    with open(output_file, 'w') as file:
        for ip_network in ip_range:
            for ip in ip_network:
                for port in range(start_port, end_port + 1):
                    print(Fore.YELLOW,f'Scanning {ip}:{port}', Fore.RESET)
                    threading.Thread(target=scan_port, args=(ip, port, file)).start()

def scan_port(ip, port, file):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((str(ip), port))
    if result == 0:
        file.write(f"{ip}:{port}\n,")
        print(Fore.GREEN,f'{ip}:{port} is open', Fore.RESET)
    else:
        print(Fore.RED, f'{ip}:{port} is closed', Fore.RESET)
    sock.close()

# Example usage:
start_ip = '172.16.10.1'
end_ip = '172.16.10.255'
start_port = 1
end_port = 5000
output_file = 'output.txt'

scan_ports(start_ip, end_ip, start_port, end_port, output_file)
