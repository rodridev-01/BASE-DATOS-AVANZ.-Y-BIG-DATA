import pandas as pd
from sqlalchemy import create_engine

SERVIDOR = 'localhost' 
BASE_DATOS = 'DataSalud_DIRESA'

conexion_str = f"mssql+pyodbc://@{SERVIDOR}/{BASE_DATOS}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
motor = create_engine(conexion_str)

print("Subiendo Dengue a SQL Server...")
df_dengue = pd.read_csv(
    './Datasets/datos_abiertos_vigilancia_dengue_normalizado.csv', 
    sep=',', 
    encoding='utf-8-sig', 
    engine='python',
    on_bad_lines='skip'
)
df_dengue.to_sql('stg_vigilancia_dengue', con=motor, if_exists='replace', index=False, chunksize=50000)
print("¡Tabla stg_vigilancia_dengue cargada con éxito!")

print("Subiendo IRA a SQL Server...")
df_ira = pd.read_csv(
    './Datasets/datos_abiertos_vigilancia_iras_normalizado.csv', 
    sep=';', 
    encoding='utf-8-sig', 
    engine='python',
    on_bad_lines='skip'
)
df_ira.to_sql('stg_vigilancia_ira', con=motor, if_exists='replace', index=False, chunksize=50000)
print("¡Tabla stg_vigilancia_ira cargada con éxito!")

print("¡Proceso completo de Big Data finalizado con éxito para ambas tablas!")