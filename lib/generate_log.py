"""Automation tool: fetches data from a public API and writes a log file."""
from datetime import datetime

import requests  # external package installed with pip

API_URL = "https://jsonplaceholder.typicode.com/posts/1"


def generate_log(log_data):
    """Write each entry in log_data to a dated .txt file and return the filename.

    Raises ValueError if log_data is not a list.
    """
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    return filename


def fetch_data(url=API_URL):
    """Fetch JSON data from the API. Returns an empty dict if the request fails."""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException as error:
        print(f"Request failed: {error}")
    return {}


def main():
    """Fetch data from the API, then write it to a log file."""
    post = fetch_data()
    title = post.get("title", "No title found")
    print("Fetched Post Title:", title)

    entries = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched post title: {title}",
    ]
    filename = generate_log(entries)
    print(f"Log written to {filename}")


if __name__ == "__main__":
    main()
