from scapy.all import ARP, Ether, srp
import nmap
import argparse
import json

# Argument Parsing
parser = argparse.ArgumentParser(description="Network Scanner")
parser.add_argument("network", help="Network range to scan, e.g., 192.168.1.0/24")
parser.add_argument("--ports", help="Port range to scan, e.g., 1-1024", default="1-1024")
args = parser.parse_args()

network_range = args.network
port_range = args.ports

# Network Discovery
arp = ARP(pdst=network_range)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
try:
    result = srp(packet, timeout=2, verbose=False)[0]
except Exception as e:
    print(f"Error during network discovery: {e}")
    result = []

devices = []
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

print("Available devices in the network:")
for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}")

# Initialize Nmap Scanner
nm = nmap.PortScanner()
nm.nmap_executable = r"C:\Program Files (x86)\Nmap\nmap.exe"  # Update this path to your Nmap executable path

def scan_ports(ip, port_range="1-1024"):
    try:
        nm.scan(ip, port_range)
        return nm[ip]
    except Exception as e:
        print(f"Error scanning ports for {ip}: {e}")
        return {}

# Port Scanning
for device in devices:
    print(f"Scanning ports for {device['ip']}...")
    scan_result = scan_ports(device['ip'], port_range)
    for protocol in scan_result.all_protocols():
        ports = scan_result[protocol].keys()
        for port in ports:
            print(f"Port: {port}, State: {scan_result[protocol][port]['state']}, Service: {scan_result[protocol][port]['name']}")

# Save Results to JSON File
with open("scan_results.json", "w") as f:
    json.dump(devices, f, indent=4)
