import os
import pandas as pd
from sqlalchemy import create_engine, text

DB_USER = "postgres"
DB_PASSWORD = "postgres123"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "airport_etl"


def get_engine():
    url = f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(url)


def load_bronze(df: pd.DataFrame):
    engine = get_engine()
    df_bronze = df[["icao24", "callsign", "origin_country", "longitude",
                    "latitude", "baro_altitude", "velocity", "on_ground", "collected_at"]].copy()

    df_bronze.rename(columns={
        "baro_altitude": "altitude"
    }, inplace=True)

    df_bronze.to_sql("bronze_flights", engine, if_exists="append", index=False)
    print(f"Bronze: {len(df_bronze)} registros inseridos.")


def load_silver(df: pd.DataFrame):
    engine = get_engine()
    df.to_sql("silver_flights", engine, if_exists="append", index=False)
    print(f"Silver: {len(df)} registros inseridos.")


def load_gold(df: pd.DataFrame):
    engine = get_engine()

    with engine.connect() as conn:
        conn.execute(text("DELETE FROM gold_flights_summary WHERE reference_date = CURRENT_DATE"))
        conn.commit()

    df.to_sql("gold_flights_summary", engine, if_exists="append", index=False)
    print(f"Gold: {len(df)} países agregados.")


def export_to_csv(df: pd.DataFrame, filename: str):
    path = f"../exports/{filename}"
    df.to_csv(path, index=False, encoding="utf-8-sig")
    print(f"CSV exportado: {path}")
