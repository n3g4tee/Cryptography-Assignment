import requests
url = f"https://crt.sh/?q=cryptohack.org"
response = requests.get(url)
certificates = response.text
print("Subdomain:", certificates)
# Visit the subdomain to obtain the flag

