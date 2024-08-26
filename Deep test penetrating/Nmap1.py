import nmap

scanner = nmap.PortScanner()

print('Welcome, this is a simple nmap automation tool')
print("<-------------------------------------------->")

ip_address = input("Please enter the IP address you want to scan: ")
print("The Ip you entered is", ip_address)
type(ip_address)

resp = input("""\nplease neter the type of scam you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive scan \n""")

print('you have selected option', resp)

def scanner_function(resp):
    # scanner version
    Nmap_version = scanner.nmap_version()
    # 
    ports_info = "1-1024"
    address_type = "tcp"
    if resp == "1":
        type_of_scan = "-v -sS"
    elif resp == "2":
        type_of_scan = "-v -sU"
        address_type = "udp"
    elif resp == "3":
        type_of_scan = "-v -sS -sV -sC -A"
    else:
        print("""wrong Input, try again \nplease neter the type of scam you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive scan \n""")
    scan_type = scanner.scan(ip_address, ports_info, type_of_scan)
    scan_info = scanner.scaninfo()
    ip_status = scanner[ip_address].state()
    scan_protocol = scanner[ip_address].all_protocols()
    open_ports = scanner[ip_address][address_type].keys()

    print(Nmap_version)
    print(scan_type)
    print(scan_info)
    print(ip_status)
    print(scan_protocol)
    print(open_ports)

scanner_function(resp)    