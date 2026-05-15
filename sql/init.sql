-- Camada bronze: dados crus vindos direto da API
CREATE TABLE IF NOT EXISTS bronze_flights (
    id SERIAL PRIMARY KEY,
    icao24 VARCHAR(10),
    callsign VARCHAR(20),
    origin_country VARCHAR(100),
    longitude FLOAT,
    latitude FLOAT,
    altitude FLOAT,
    velocity FLOAT,
    on_ground BOOLEAN,
    collected_at TIMESTAMP DEFAULT NOW()
);

-- Camada silver: dados limpos e tipados
CREATE TABLE IF NOT EXISTS silver_flights (
    id SERIAL PRIMARY KEY,
    icao24 VARCHAR(10),
    callsign VARCHAR(20),
    origin_country VARCHAR(100),
    longitude FLOAT,
    latitude FLOAT,
    altitude_meters FLOAT,
    velocity_kmh FLOAT,
    on_ground BOOLEAN,
    collected_at TIMESTAMP
);

-- Camada gold: dados agregados prontos para o dashboard
CREATE TABLE IF NOT EXISTS gold_flights_summary (
    id SERIAL PRIMARY KEY,
    origin_country VARCHAR(100),
    total_flights INT,
    avg_altitude FLOAT,
    avg_velocity FLOAT,
    flights_on_ground INT,
    flights_in_air INT,
    reference_date DATE,
    updated_at TIMESTAMP DEFAULT NOW()
);
