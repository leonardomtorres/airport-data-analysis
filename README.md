# ✈️ Airport Data Analysis — Pipeline ETL de Voos em Tempo Real

Pipeline de engenharia de dados que coleta informações de voos ao vivo de todo o mundo, processa em camadas e disponibiliza para análise via dashboard.

---

## Sobre o projeto

A ideia surgiu da curiosidade de entender o volume e o comportamento do tráfego aéreo mundial em tempo real. A partir de uma API pública e gratuita, o pipeline captura milhares de voos ativos, limpa os dados, agrega por país e exporta para visualização.

Todo o processo roda de forma automatizada a cada 30 minutos.

---

## Arquitetura

OpenSky Network API
│
▼
extract.py → captura os voos em tempo real
│
▼
transform.py → limpa, tipifica e converte os dados
│
▼
load.py → salva no PostgreSQL e exporta CSV
│
▼ 
PostgreSQL exports/
(3 camadas) (Power BI)


### Camadas do banco de dados

| Camada | Tabela | Descrição |
|---|---|---|
| Bronze | `bronze_flights` | Dado cru direto da API |
| Silver | `silver_flights` | Dado limpo e padronizado |
| Gold | `gold_flights_summary` | Agregado por país para análise |

---

## Tecnologias utilizadas

- **Python 3.12** — linguagem principal
- **PostgreSQL 15** — banco de dados relacional
- **Docker & Docker Compose** — ambiente isolado e reproduzível
- **Pandas** — transformação e limpeza dos dados
- **SQLAlchemy + pg8000** — conexão Python com o banco
- **OpenSky Network API** — fonte dos dados de voos em tempo real
- **Power BI** — dashboard de visualização
- **pgAdmin** — interface visual do banco

---

## Como rodar o projeto

### Pré-requisitos

- Python 3.10+
- Docker Desktop instalado e rodando
- Git

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/leonardomtorres/airport-data-analysis.git
cd airport-data-analysis
```

2. Instale as dependências

pip install -r requirements.txt
3. Suba o banco de dados

docker-compose up -d
4. Rode o pipeline

cd etl
python pipeline.py
5. Para rodar automaticamente a cada 30 minutos

python scheduler.py

Estrutura do projeto

airport-data-analysis/
├── docker-compose.yml     
├── requirements.txt       
├── sql/
│   └── init.sql           # cria as tabelas automaticamente
├── etl/
│   ├── extract.py         # busca os dados na API
│   ├── transform.py       # limpa e agrega os dados
│   ├── load.py            # salva no banco e exporta CSV
│   ├── pipeline.py        # orquestra o fluxo completo
│   └── scheduler.py       # execução automática
└── exports/               # CSVs gerados para o Power BI



Resultado
A cada execução o pipeline captura entre 6.000 e 9.000 voos ativos de mais de 90 países e gera um resumo com:

Total de voos por país
Média de altitude e velocidade
Voos no ar vs em solo
Autor
Leonardo Torres
