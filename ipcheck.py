import requests
import json
import sys
import time

def abused(IPv4, key):
    start_time = time.time()

    print("\n--- AbuseIPDB Results ---\n") or [
        (
            print(f"Checking {ip} ({i + 1}/{len(IPv4)})..."),
            (response := requests.get(f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}", headers={'Accept': 'application/json', 'Key': key})),
            (data := response.json().get("data", {})),
            print(f"IPv4: {data.get('ipAddress', 'N/A')}\nCountry: {data.get('countryCode', 'N/A')}\nISP: {data.get('isp', 'N/A')}\nDomain: {data.get('domain', 'N/A')}\nAbuse Confidence Score: {data.get('abuseConfidenceScore', 'N/A')}%\nTotal Reports: {data.get('totalReports', 'N/A')}\nLast Reported At: {data.get('lastReportedAt', 'N/A')}\n{'-' * 40}") if response.status_code == 200 else print(f"Error: Failed to process IP {ip}. Response code: {response.status_code}\n{'-' * 40}")
        )
        for i, ip in enumerate(IPv4)
    ] or print(f"\nSUCCESS: {len(IPv4)} IPs in {round(time.time() - start_time, 2)} seconds.")

def main(): [print("Usage: python ipcheck.py '<ip1,ip2,ip3>' <key>'\nExample: python ipcheck.py '8.8.8.8,1.1.1.1' YOUR_key") or sys.exit(1) if len(sys.argv) != 3 else abused([ip.strip() for ip in sys.argv[1].split(',') if ip.strip()], sys.argv[2]) if [ip.strip() for ip in sys.argv[1].split(',') if ip.strip()] else (print("Error: No valid IPs provided."), sys.exit(1))]

if __name__ == "__main__":
    main()
