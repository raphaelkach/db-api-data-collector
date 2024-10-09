import sys
import os
from unittest.mock import patch

# Füge den Root-Pfad hinzu, damit main.py gefunden wird
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import fetch_api_data, load_station_data  # noqa: E402


@patch('main.requests.get')  # Mocke den requests.get-Aufruf
def test_fetch_api_data(mock_get):
    """
    Testet die Funktion fetch_api_data, um sicherzustellen,
    dass die API-Daten korrekt abgerufen werden.
    """
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b"<xml>valid response</xml>"

    eva_nr = "8000096"  # Beispiel-EVA-Nummer
    date = "241008"  # Beispiel-Datum
    hour = "10"  # Beispiel-Stunde

    response_plan, response_change = fetch_api_data(eva_nr, date, hour)

    assert response_plan is not None, (
        "API-Aufruf für Plan-Daten ist fehlgeschlagen!")
    assert response_change is not None, (
        "API-Aufruf für Änderungs-Daten ist fehlgeschlagen!")


def test_load_station_data():
    """
    Testet die Funktion load_station_data, um sicherzustellen,
    dass die Stationsdaten korrekt geladen werden.
    """
    filepath = "./01_data/01_raw/Stationen_S-Bahnnetz_Stuttgart.csv"

    eva_nrs, names, states, cities, zipcodes, longs, lats, categories = (
        load_station_data(filepath)
    )

    assert len(eva_nrs) > 0, "Keine EVA-Nummern gefunden!"
    assert len(names) > 0, "Keine Stationsnamen gefunden!"
    assert "Stuttgart Hbf" in names, (
        "Stuttgart Hauptbahnhof nicht in den Stationsdaten gefunden!"
    )
