# etl/transform_clean.py | 02 Proceso ETL: Limpiado de datos

import pandas as pd  # Librería para manejo de datos tabulares (DataFrames)

def transform_data():
    # Paso 1: Cargar el dataset original
    df = pd.read_csv("data/accidents_raw.csv")  # Leemos el CSV crudo extraído en el paso anterior

    # Paso 2: Selección de columnas relevantes
    columns = [
        "crash_date",             # Fecha del accidente
        "crash_time",             # Hora del accidente
        "collision_id",           # ID único del accidente
        "vehicle_type_code1",     # Tipo de vehículo 1
        "vehicle_type_code2",     # Tipo de vehículo 2 (si hay)
        "zip_code",               # Código postal
        "borough"                 # Distrito de NYC (Manhattan, Bronx, etc.)
    ]

    # Paso 3: Limpieza inicial
    df_clean = df[columns].dropna().copy()

    # Paso 4: Eliminación de valores indeseados (tipo 'UNK', 'unknown', 'unknow', etc.)
    patron_regex = r"^unk.*"
    mask = df_clean.apply(lambda col: col.astype(str).str.lower().str.contains(patron_regex, na=False)).any(axis=1)
    df_final = df_clean[~mask]

    # Paso 5: Guardar el resultado limpio
    df_final.to_csv("data/accidents_clean.csv", index=False)

    # Paso 6: Reporte del proceso
    print(f"Filas originales: {len(df)}")
    print(f"Filas limpias (sin NaN y sin 'unk*'): {len(df_final)}")
