# Network Scanner

A multi-threaded network scanner that discovers active devices on a local network using ARP requests, resolves hostnames, and displays results in a tabular format.

## Features

- **CIDR-based Scanning**: Scan entire subnets using CIDR notation (e.g., 192.168.1.0/24)
- **Rapid Discovery**: Multi-threaded scanning for fast network discovery
- **MAC Address Collection**: Retrieves MAC addresses of all active devices
- **Hostname Resolution**: Attempts to resolve device hostnames using reverse DNS lookup
- **Organized Results**: Displays findings in a clean, tabular format
- **Progress Tracking**: Shows real-time scan progress
- **Export Capability**: Option to save results as CSV for further analysis

## Requirements

- Python 3.6+
- scapy
- tabulate

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/network-scanner.git
   cd network-scanner
   ```

2. Install the required dependencies:
   ```
   pip install scapy tabulate
   ```

## Usage

Run the script:

```
python network_scanner.py
```

Follow the prompts:

1. Enter a CIDR range to scan (e.g., 192.168.1.0/24)
2. Wait for the scan to complete
3. View the results in the table
4. Optionally save results to a CSV file

## Example Output

```
Enter CIDR (e.g., 192.168.1.0/24): 192.168.1.0/24

Starting scan of 254 hosts...
Scanning network for active devices...
Progress: 100.0% (254/254)

Discovered Devices:
+---------------+-------------------+--------------------+
| IP Address    | MAC Address       | Hostname           |
+===============+===================+====================+
| 192.168.1.1   | e4:8d:8c:12:34:56 | router.local       |
+---------------+-------------------+--------------------+
| 192.168.1.5   | a4:83:e7:ab:cd:ef | desktop-pc.local   |
+---------------+-------------------+--------------------+
| 192.168.1.10  | b8:27:eb:12:34:56 | raspberry-pi.local |
+---------------+-------------------+--------------------+
| 192.168.1.15  | 40:b0:76:ab:cd:ef | Unknown            |
+---------------+-------------------+--------------------+
| 192.168.1.20  | f8:1a:67:12:34:56 | laptop.local       |
+---------------+-------------------+--------------------+

Scan Summary:
Total hosts scanned: 254
Devices found: 5
Scan duration: 12.35 seconds

Save results to file? (y/n): y
Enter filename (default: network_scan_results.csv):
Results saved to network_scan_results.csv
```

## How It Works

1. **User Input**: The user provides a CIDR-based network address
2. **IP Address Extraction**: The script extracts all valid host IPs from the provided subnet
3. **ARP Request**: Each IP address is scanned using an ARP (Address Resolution Protocol) request
4. **MAC Address Retrieval**: If the device is active, its MAC address is collected
5. **Hostname Resolution**: The scanner attempts to fetch the hostname using reverse DNS lookup
6. **Multi-threading**: The script uses multiple threads to scan multiple devices in parallel
7. **Results Display**: The discovered devices are displayed in a tabular format with their IP address, MAC address, and hostname

## Limitations

- Works best on local networks where ARP requests can reach devices
- Hostname resolution depends on proper DNS configuration in the network
- Some devices may block ARP requests or have firewall settings that prevent discovery
- Requires administrator/root privileges on some operating systems due to low-level network operations

## License

[MIT License](LICENSE)

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/network-scanner/issues).

## Disclaimer

This tool is intended for network administrators to audit their own networks. Always ensure you have permission to scan a network before running this tool. Unauthorized scanning of networks may violate local laws and regulations.
