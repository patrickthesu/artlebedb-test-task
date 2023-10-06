import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from libraries.models import Library, Contacts, Coordinates

def get_data (page_url: str, download_path: str,  selector: str = ".download_btn") -> None:
        soup = BeautifulSoup (requests.get(page_url).text, "html.parser")
        versions = soup.select (selector)
        last_supported_version = None
        versions.reverse()
        for version in versions:
            if "data" in version.get("data-name") and "structure-3" in version.get("data-name") and "json" in version.get("data-formats"):
                last_supported_version = version
                break
        if not version:
            raise "Have no supported versions on page"
            
        data_url = f"{_get_host_from_url (page_url)}{last_supported_version.get('data-url')}{last_supported_version.get('data-name')}.json"
        with open (download_path, "wb") as file:
            file.write (requests.get (data_url).content)
        return None

def _get_host_from_url (url: str) -> str:
    return '{url.scheme}://{url.netloc}'.format(url = urlparse(url))

def append_library (libraryData: dict) -> Library:
    return Library.objects.create (
        timezone = "",
        name = "",
        description = "",
        fullAdress = "",
        coordintaes = "",
        )

def _append_contacts (contactsData: dict) -> Contacts:
    return Contacts.objects.create(
        email = "",
        phone = "",
        )

def _append_coordinates (coordinatesData: dict) -> Coordinates:
    return Coordinates.objects.create (
        posx = "",
        posy = "",
        )
