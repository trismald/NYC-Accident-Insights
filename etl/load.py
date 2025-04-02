import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def load_data():
    load_dotenv()  # Carga las variables del archivo .env

    # Leer CSV limpio
    df = pd.read_csv("data/accidents_clean.csv")

    # Leer credenciales desde variables de entorno
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    db_url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(db_url)

    # Cargar datos en la tabla
    df.to_sql("accidents", con=engine, if_exists="append", index=False)
