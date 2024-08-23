import nmap

scanner =  nmap.PortScanner()

print('welcome, This is a simple nmap automation tool')
print("<---------------------------------------------------->")

ip_address = input("Please enter the IP address you want to scan: ")
print("The Ip you entered is", ip_address)
type(ip_address)

resp = input("""\nplease neter the type of scam you want to run
                1)SYN ACK Scan
                2)USP Scan
                3)Comprehensive scan \n""")
print('you have selected option: ', resp)

if resp == '1':
    print('Nmap version: ', scanner.nmap_version())
    scanner.scan(ip_address,'1-1024', '-v -sS' )
    print(scanner.scaninfo())
    print("IP status", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print('open ports:', scanner[ip_address]['tcp'].keys())
elif resp == '2':
    print('Nmap version: ', scanner.nmap_version())
    scanner.scan(ip_address,'1-1024', '-v -sU' )
    print(scanner.scaninfo())
    print("IP status", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print('open ports:', scanner[ip_address]['udp'].keys())
elif resp == '3':
    print('Nmap version: ', scanner.nmap_version())
    scanner.scan(ip_address,'1-1024', '-v -sS -sV -sC -A ' )
    print(scanner.scaninfo())
    print("IP status", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print('open ports:', scanner[ip_address]['tcp'].keys())
elif resp >= '4':
    print("Please enter a valid option")
