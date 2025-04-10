import ipaddress
import time
import socket
from tabulate import tabulate
from scapy.all import ARP, Ether, srp
import signal
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# my_ip = 192.168.1.7

# Set a shorter timeout
TIMEOUT = 0.5


def get_hostname(ip):
    try:
        hostname = socket.getfqdn(ip)

        if hostname == ip:
            return "Unknown"
        return hostname
    except:
        return "Unknown"


def arp_scan(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = ether / arp

    result = srp(packet, timeout=TIMEOUT, verbose=0)[0]

    if result:
        for sent, received in result:
            ip_addr = received.psrc
            mac_addr = received.hwsrc
            hostname = get_hostname(ip)
            return (ip_addr, mac_addr, hostname)
    return None


def main():
    start_time = time.time()

    try:
        cidr = input("Enter CIDR (e.g., 192.168.1.0/24): ")
        ip_list = list(ipaddress.ip_network(cidr, strict=False).hosts())

        print(f"Starting scan of {len(ip_list)} hosts...")
        print("Scanning network for active devices...")

        discovered_devices = []
        try:
            with ThreadPoolExecutor(max_workers=50) as executer:
                futures = {executer.submit(
                    arp_scan, str(ip)): ip for ip in ip_list}

                # Simple Progress Indicator
                processed = 0
                for future in as_completed(futures):
                    processed += 1
                    progress = (processed / len(ip_list)) * 100

                    print(
                        f"\rProgress: {progress:.1f}% ({processed}/{len(ip_list)})", end="")

                    try:
                        result = future.result()
                        if result:
                            discovered_devices.append(result)
                    except Exception as e:
                        ip = futures[future]
                        print(f"\nError scanning {ip}: {e}")

            # Clear progress line
            print("\r" + " " * 50 + "\r", end="")

        except KeyboardInterrupt:
            print("\nScan interrupted by user. Exiting...")
            sys.exit(1)

        # Display Result Table
        if discovered_devices:

            # Sort Devices based on ip_addr
            discovered_devices.sort(
                key=lambda x: [int(part) for part in x[0].split('.')])

            headers = ["IP Address", "MAC Address", "Hostname"]
            table_data = [[ip, mac, hostname]
                          for ip, mac, hostname in discovered_devices]

            print("\nDiscovered Devices:")
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            print("\nNo devices Found.")

        end_time = time.time()
        duration = end_time - start_time

        print("\nScan Summary:")
        print(f"Total hosts scanned: {len(ip_list)}")
        print(f"Devices Found: {len(discovered_devices)}")
        print(f"Scan Duration: {duration:.2f} seconds")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
