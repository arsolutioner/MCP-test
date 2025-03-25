import socket
import sys
import ipaddress
import concurrent.futures

def scan_port(host, port):
    """
    Attempt to connect to a specific port and return its status
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a short timeout
        sock.settimeout(1)
        
        # Attempt to connect to the port
        result = sock.connect_ex((host, port))
        
        # Check if connection was successful
        if result == 0:
            return port, True
        else:
            return port, False
    except Exception:
        return port, False
    finally:
        sock.close()

def port_scan(target, start_port=1, end_port=1024, max_threads=100):
    """
    Scan a range of ports for a given target
    """
    try:
        # Resolve hostname to IP if needed
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {target}")
        return []

    print(f"Scanning target: {target_ip}")
    open_ports = []

    # Use ThreadPoolExecutor for concurrent scanning
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        # Create futures for port scanning
        futures = {
            executor.submit(scan_port, target_ip, port): port 
            for port in range(start_port, end_port + 1)
        }

        # Collect results
        for future in concurrent.futures.as_completed(futures):
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)
                print(f"Port {port} is open")

    return open_ports

def main():
    # Default scan parameters
    target = "scanme.nmap.org"  # Default target
    start_port = 1
    end_port = 1024

    # Allow command-line arguments
    if len(sys.argv) > 1:
        target = sys.argv[1]
    if len(sys.argv) > 2:
        start_port = int(sys.argv[2])
    if len(sys.argv) > 3:
        end_port = int(sys.argv[3])

    print(f"Hello, World from MCP-test!")
    print(f"Initializing port scanner...")
    
    # Perform port scan
    open_ports = port_scan(target, start_port, end_port)
    
    # Print final summary
    print("\nPort Scan Complete.")
    print(f"Open ports on {target}: {open_ports}")

if __name__ == '__main__':
    main()
