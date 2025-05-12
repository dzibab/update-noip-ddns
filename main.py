"""
Python script to update No-IP Dynamic DNS service with the current public IP address.
"""
import os
import time
import logging

import requests
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

NOIP_USERNAME = os.getenv("NOIP_USERNAME")
NOIP_PASSWORD = os.getenv("NOIP_PASSWORD")
NOIP_HOSTNAME = os.getenv("NOIP_HOSTNAME")


def get_public_ip():
    return requests.get("https://api.ipify.org").text.strip()


def update_noip_ddns(ip, hostname, username, password):
    url = f"https://dynupdate.no-ip.com/nic/update?hostname={hostname}&myip={ip}"
    response = requests.get(
        url,
        auth=(username, password),
        headers={"User-Agent": "Python DDNS Client/1.0"},
    )
    return response.text


def main():
    if not (NOIP_USERNAME and NOIP_PASSWORD and NOIP_HOSTNAME):
        logging.error("Missing required environment variables.")
        raise ValueError(
            "Please set NOIP_USERNAME, NOIP_PASSWORD, and NOIP_HOSTNAME environment variables."
            )
    while True:
        ip = get_public_ip()
        logging.info(f"Current public IP: {ip}")
        result = update_noip_ddns(ip, NOIP_HOSTNAME, NOIP_USERNAME, NOIP_PASSWORD)
        logging.info(f"Update result: {result}")
        time.sleep(300)  # Wait for 5 minutes (300 seconds)


if __name__ == "__main__":
    main()
