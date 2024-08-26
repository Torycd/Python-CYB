import socket

def banner(ip, port):
    s = socket.socket()
    try:
        # Set timeout for the socket
        s.settimeout(10)
        
        # Connect to the target IP and port
        s.connect((ip, int(port)))
        
        # Attempt to receive data (banner) from the server
        banner = s.recv(1024).strip('b')
        
        # Display the banner (if any)
        print(banner.decode('utf-8', errors='ignore'))
    except socket.timeout:
        print("Connection timed out. The server is not responding.")
    except socket.error as err:
        print(f"Socket error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure that the socket is closed properly
        s.close()

def main():
    ip = input("Please enter the IP: ")
    port = input("Please enter the PORT: ")

    # Run the banner grabbing function
    banner(ip, port)

if __name__ == "__main__":
    main()
