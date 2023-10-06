import json
from libraries.models import Library, Contacts, Coordinates


def load_json (path: str) -> list:
    with open (path) as file:
        librariesJson = json.loads(file.read())
    return librariesJson

def parse_json (data: list) -> None:
    for library in data:
        try:
            libraryData = get_dict_data(library["data"]["general"])
            append_library (libraryData)
        except Exception as err:
            print (err)

def get_dict_data (libraryData: dict) -> dict:
    return {
        "timezone": libraryData["locale"]["timezone"],
        "name": libraryData["name"],
        "description": libraryData["description"],
        "fullAddress": libraryData["address"]["fullAddress"],
        "coordinates": libraryData["address"]["mapPosition"]["coordinates"],
        "contacts": libraryData["contacts"], 
        }

def append_library (libraryData: dict) -> Library:
    contacts = _append_contacts (libraryData["contacts"])
    coordinates = _append_coordinates (libraryData["coordinates"])

    contacts.save()
    coordinates.save()
    
    library = Library.objects.create (
        timezone = libraryData["timezone"],
        name = libraryData["name"],
        description = libraryData["description"],
        fullAdress = libraryData["fullAddress"],
        coordinates = coordinates,
        contacts = contacts,
        )
    library.save()

    return library

def _append_contacts (contactsData: dict) -> Contacts:
    return Contacts.objects.create(
        email = contactsData["email"],
        phone = contactsData["phones"][0]["value"],
            )

def _append_coordinates (coordinatesData: dict) -> Coordinates:
    return Coordinates.objects.create (
        posx = coordinatesData[0],
        posy = coordinatesData[1],
            )
