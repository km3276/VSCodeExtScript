import subprocess
import json
import re
from bs4 import BeautifulSoup
from datetime import datetime

HEADERS = [
    "-H", "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "-H", "Accept-Language: en-US,en;q=0.9",
    "-H", "Upgrade-Insecure-Requests: 1"
]


def format_date(date_str):
    """
    Convert:
    Wed, 14 Jun 2023 18:20:56 GMT
    -> 6/14/2023 18:20:56
    """
    dt = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S GMT")
    return dt.strftime("%-m/%-d/%Y %H:%M:%S")


def fetch_extension_page(unique_identifier):
    url = f"https://marketplace.visualstudio.com/items?itemName={unique_identifier}"

    curl_cmd = ["curl", "-s", url] + HEADERS

    result = subprocess.run(
        curl_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise Exception(f"curl failed: {result.stderr}")

    return result.stdout


def parse_extension_data(html):
    soup = BeautifulSoup(html, "html.parser")

    # -------------------------
    # Install Count
    # -------------------------
    install_span = soup.find("span", class_="installs-text")
    install_count = None
    if install_span:
        match = re.search(r"([\d,]+)", install_span.text)
        if match:
            install_count = match.group(1)

    # -------------------------
    # Verified
    # -------------------------
    verified = "N"
    if soup.find("div", class_="ux-marketplace-verified-doamin-icon"):
        verified = "Y"

    # -------------------------
    # Release / Updated Dates
    # -------------------------
    release_date = None
    last_updated_date = None

    for script in soup.find_all("script", type="application/json"):
        try:
            data = json.loads(script.string)
            if "ReleaseDateString" in data:
                release_date = format_date(data["ReleaseDateString"])
                last_updated_date = format_date(data["LastUpdatedDateString"])
                break
        except Exception:
            continue

    return {
        "verified": verified,
        "releaseDate": release_date,
        "lastUpdatedDate": last_updated_date,
        "installCount": install_count
    }


def main():
    publisher = input("Enter publisher name (e.g. ms-python): ").strip()
    extension = input("Enter VSCode extension name (e.g. debugpy): ").strip()

    unique_identifier = f"{publisher}.{extension}"
    print(f"\nFetching data for: {unique_identifier}\n")

    html = fetch_extension_page(unique_identifier)
    data = parse_extension_data(html)

    print(f"verified: '{data['verified']}'")
    print(f"releaseDate: '{data['releaseDate']}'")
    print(f"lastUpdatedDate: '{data['lastUpdatedDate']}'")
    print(f"installCount: '{data['installCount']}'")


if __name__ == "__main__":
    main()
