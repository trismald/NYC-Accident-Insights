# etl/extract.py | 01 Proceso ETL: Extracción de la información

# Importaciones
import requests  # Librería para solicitar descargas de HTTP
import pandas as pd  # Librería para manejar dataframes

def extract_data():
    # URL pública de la ciudad de Nueva York
    URL_JSON = "https://data.cityofnewyork.us/resource/h9gi-nx95.json"
    params = {"$limit": 1000000}  # Límite de filas (1,000,000)

    # Métodos para la descarga de la información y almacenado en dataframes
    reponse = requests.get(URL_JSON, params=params)
    data = reponse.json()
    df = pd.DataFrame(data)

    # Archivo extraído
    df.to_csv("data/accidents_raw.csv")
