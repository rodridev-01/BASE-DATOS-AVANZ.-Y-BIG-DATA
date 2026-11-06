import pandas as pd
import os

archivos = [
    {
        "entrada": "./Datasets/datos_abiertos_vigilancia_dengue_2000_2025_0.csv",
        "salida": "./Datasets/datos_abiertos_vigilancia_dengue_normalizado.csv"
    },
    {
        "entrada": "./Datasets/datos_abiertos_vigilancia_iras_2000_2025.csv",
        "salida": "./Datasets/datos_abiertos_vigilancia_iras_normalizado.csv"
    }
]

for item in archivos:
    ruta_entrada = item["entrada"]
    ruta_salida = item["salida"]
    
    if not os.path.exists(ruta_entrada):
        print(f"No se encontró el archivo: {ruta_entrada}")
        continue

    print(f"Procesando: {ruta_entrada}...")
    df = pd.read_csv(ruta_entrada, sep=';', encoding='utf-8', low_memory=False)

    columnas_texto = df.select_dtypes(include=['object']).columns
    
    for col in columnas_texto:
        df[col] = df[col].astype(str).str.replace('"', '', regex=False).str.strip().str.upper()
        df[col] = df[col].replace({'NAN': '', 'NONE': ''})

    df.to_csv(ruta_salida, sep=';', index=False, encoding='utf-8-sig')
    print(f"¡Éxito! Guardado: {ruta_salida}\n")

print("¡Proceso completado!")