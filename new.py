import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# User inputs
PORTAL_URL = "http://moodle.apsit.org.in/moodle/login/index.php"  # Replace with the portal login URL
COURSE_URL = "http://moodle.apsit.org.in/moodle/course/view.php?id=3441"  # Replace with the course page URL
USERNAME = "22102047"  # Replace with your username
PASSWORD = "Swayam1@moodleapsitnew"  # Replace with your password
DOWNLOAD_DIR = "downloads"  # Directory to save downloaded PDFs

# Create a session for persistent login
session = requests.Session()

def login():
    """Log in to the portal."""
    print("[*] Logging in...")
    login_payload = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = session.post(PORTAL_URL, data=login_payload)
    # if response.ok and "dashboard" in response.text:  # Check for successful login
    #     print("[+] Login successful!")
    # else:
    #     print(response)
    #     print("[-] Login failed. Please check credentials.")
    #     exit()

def fetch_pdfs():
    """Scrape and download all PDFs from the course page."""
    print("[*] Fetching course page...")
    response = session.get(COURSE_URL)
    # if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    pdf_links = []

    # Find all PDF links
    for link in soup.find_all("a", href=True):
        if link["href"].endswith(".pdf"):
            pdf_links.append(urljoin(COURSE_URL, link["href"]))

    if not pdf_links:
        print("[-] No PDFs found on the course page.")
        return

    print(f"[+] Found {len(pdf_links)} PDF(s). Downloading...")
    
    # Create download directory if it doesn't exist
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # Download each PDF
    for pdf_url in pdf_links:
        download_pdf(pdf_url)
    # else:
    #     print("[-] Failed to fetch course page. Please check the course URL.")
    #     exit()

def download_pdf(pdf_url):
    """Download a PDF file."""
    pdf_name = pdf_url.split("/")[-1]
    save_path = os.path.join(DOWNLOAD_DIR, pdf_name)

    print(f"[*] Downloading {pdf_name}...")
    response = session.get(pdf_url, stream=True)
    if response.ok:
        with open(save_path, "wb") as pdf_file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    pdf_file.write(chunk)
        print(f"[+] Saved {pdf_name} to {DOWNLOAD_DIR}")
    else:
        print(f"[-] Failed to download {pdf_name}")

if __name__ == "__main__":
    login()
    fetch_pdfs()
