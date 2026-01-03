import requests
import sys

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"[+] {url} is UP (Status Code: {response.status_code})")
    except requests.exceptions.RequestException:
        print(f"[-] {url} is DOWN or unreachable")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 checker.py <website>")
        print("Example: python3 checker.py https://google.com")
        sys.exit(1)

    website = sys.argv[1]
    check_website(website)

if __name__ == "__main__":
    main()
