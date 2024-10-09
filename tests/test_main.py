import pytest
from main import fetch_api_data, load_station_data

def test_fetch_api_data():
    """
    Testet die Funktion fetch_api_data, um sicherzustellen, dass die API-Daten korrekt abgerufen werden.
    """
    eva_nr = "8000105"  # Beispiel-EVA-Nummer (Berlin Hauptbahnhof)
    date = "230101"     # Beispiel-Datum (1. Januar 2023)
    hour = "12"         # Beispiel-Stunde (12 Uhr)

    response_plan, response_change = fetch_api_data(eva_nr, date, hour)

    assert response_plan is not None, "API-Aufruf für Plan-Daten ist fehlgeschlagen!"
    assert response_change is not None, "API-Aufruf für Änderungs-Daten ist fehlgeschlagen!"

def test_load_station_data():
    """
    Testet die Funktion load_station_data, um sicherzustellen, dass die Stationsdaten korrekt geladen werden.
    """
    filepath = "./01_data/01_raw/Stationen_S-Bahnnetz_Stuttgart.csv"

    eva_nrs, names, states, cities, zipcodes, longs, lats, categories = load_station_data(filepath)

    assert len(eva_nrs) > 0, "Keine EVA-Nummern gefunden!"
    assert len(names) > 0, "Keine Stationsnamen gefunden!"
    assert "Stuttgart Hbf" in names, "Stuttgart Hauptbahnhof nicht in den Stationsdaten gefunden!"
