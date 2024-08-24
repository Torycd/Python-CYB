import nmap
import paramiko

# Initialize Nmap
nm = nmap.PortScanner()

# Scan website
nm.scan('nkiri.com', '1-1024')

# Print scan results
for host in nm.all_hosts():
    print(f'Host: {host} ({nm[host].hostname()})')
    print(f'State: {nm[host].state()}')
    for proto in nm[host].all_protocols():
        print(f'----------')
        print(f'Protocol: {proto}')
        lport = nm[host][proto].keys()
        sorted(lport)
        for port in lport:
            print(f'Port: {port}\tState: {nm[host][proto][port]["state"]}')

# Vulnerability scanning (basic example)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        for port in nm[host][proto].keys():
            if nm[host][proto][port]['state'] == 'open':
                try:
                    ssh.connect(host, port, username='username', password='password')
                    stdin, stdout, stderr = ssh.exec_command('vuln_command')
                    print(f'Vulnerability found: {stdout.read().decode()}')
                except paramiko.AuthenticationException:
                    print(f'Authentication failed for {host}:{port}')
                except paramiko.SSHException:
                    print(f'SSH connection failed for {host}:{port}')
                finally:
                    ssh.close()
