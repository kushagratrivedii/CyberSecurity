# Any random scanning of ports of any random website or IP, I will not be responsible for any of it.
#Enjoy
import socket
from IPy import IP
def scan(target, port_range):
    converted_ip = ip_check(target) 
    print(f'\n[-_0 Scanning target {target}')
    for port in range(1, port_range):
        scan_port(converted_ip, port)
def ip_check(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)
def get_banner(s):
    return s.recv(1024)
def scan_port(ip, port):
    try:
        soc = socket.socket()
        soc.settimeout(0.5)
        soc.connect((ip, port))
        try:
            banner = get_banner(soc)
            print(f'[+]Open port {port} : {banner.decode()}')
        except:
            print(f'[+]Open port {port}')    
    except:
          pass
targets = input('[+]Enter the target/s to scan(if multiple targets then split using ","): ')
port_range = int(input(f'[+] Enter the range of port you want to scan(500 means first 500 ports): '))
if ',' in targets:
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '))
else:
    scan(targets, port_range)
