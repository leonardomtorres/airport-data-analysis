import pandas as pd


def transform_flights(df: pd.DataFrame) -> pd.DataFrame:
    print("Transformando dados...")

    df = df[["icao24", "callsign", "origin_country", "longitude",
             "latitude", "baro_altitude", "velocity", "on_ground", "collected_at"]].copy()

    df.rename(columns={"baro_altitude": "altitude"}, inplace=True)

    df = df[df["origin_country"].notna()]

    df["callsign"] = df["callsign"].str.strip()

    df["altitude_meters"] = pd.to_numeric(df["altitude"], errors="coerce").round(2)

    # velocidade vem em m/s, converte para km/h
    df["velocity_kmh"] = (pd.to_numeric(df["velocity"], errors="coerce") * 3.6).round(2)

    df["on_ground"] = df["on_ground"].astype(bool)

    df_clean = df[["icao24", "callsign", "origin_country", "longitude",
                   "latitude", "altitude_meters", "velocity_kmh", "on_ground", "collected_at"]]

    print(f"Dados após limpeza: {len(df_clean)} registros")
    return df_clean


def aggregate_flights(df: pd.DataFrame) -> pd.DataFrame:
    print("Agregando dados para camada gold...")

    summary = df.groupby("origin_country").agg(
        total_flights=("icao24", "count"),
        avg_altitude=("altitude_meters", "mean"),
        avg_velocity=("velocity_kmh", "mean"),
        flights_on_ground=("on_ground", "sum"),
    ).reset_index()

    summary["flights_in_air"] = summary["total_flights"] - summary["flights_on_ground"]
    summary["avg_altitude"] = summary["avg_altitude"].round(2)
    summary["avg_velocity"] = summary["avg_velocity"].round(2)
    summary["reference_date"] = pd.Timestamp.now().date()

    return summary
