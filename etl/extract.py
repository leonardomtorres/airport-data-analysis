import requests
import pandas as pd
from datetime import datetime


API_URL = "https://opensky-network.org/api/states/all"


def fetch_flights():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Buscando voos na API...")

    try:
        response = requests.get(API_URL, timeout=15)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Timeout ao chamar a API. Tentando novamente na próxima execução.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na chamada da API: {e}")
        return None

    data = response.json()

    if not data.get("states"):
        print("API retornou vazio. Pode ser fora do horário ou limite de chamadas.")
        return None

    columns = [
        "icao24", "callsign", "origin_country", "time_position",
        "last_contact", "longitude", "latitude", "baro_altitude",
        "on_ground", "velocity", "true_track", "vertical_rate",
        "sensors", "geo_altitude", "squawk", "spi", "position_source"
    ]

    df = pd.DataFrame(data["states"], columns=columns)
    df["collected_at"] = datetime.now()

    print(f"Total de voos capturados: {len(df)}")
    return df
