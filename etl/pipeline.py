from extract import fetch_flights
from transform import transform_flights, aggregate_flights
from load import load_bronze, load_silver, load_gold, export_to_csv
from datetime import datetime


def run():
    print("=" * 50)
    print(f"Pipeline iniciado: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("=" * 50)

    raw_df = fetch_flights()
    if raw_df is None:
        print("Pipeline encerrado: sem dados para processar.")
        return

    load_bronze(raw_df)

    clean_df = transform_flights(raw_df)
    load_silver(clean_df)

    summary_df = aggregate_flights(clean_df)
    load_gold(summary_df)

    export_to_csv(summary_df, "gold_flights_summary.csv")
    export_to_csv(clean_df, "silver_flights.csv")

    print("=" * 50)
    print("Pipeline finalizado com sucesso!")
    print("=" * 50)


if __name__ == "__main__":
    run()
