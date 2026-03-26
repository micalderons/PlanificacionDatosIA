import pandas as pd
from sqlalchemy import create_engine
import re

print("--- INICIANDO PURGA TOTAL Y CARGA ---")

archivo = "dataset_medicamentos_limpio.xlsx"

try:
    # 1. Carga limpia
    df = pd.read_excel(archivo)
    print(f"1. Archivo cargado: {len(df)} filas.")

    # 2. LIMPIEZA RADICAL DE COLUMNAS
    # Quitamos espacios, tildes y caracteres raros de los encabezados
    df.columns = [re.sub(r'[^a-zA-Z0-9_]', '', str(c).lower()) for c in df.columns]
    print("2. Nombres de columnas simplificados (ej: 'id_medicamento').")

    # 3. LIMPIEZA RADICAL DE DATOS
    # Solo permitimos caracteres básicos (letras, números, espacios y puntos)
    def limpiar_celda(texto):
        if pd.isna(texto): return ""
        # Esta línea elimina CUALQUIER cosa que no sea texto estándar
        return re.sub(r'[^\x20-\x7E]', '', str(texto))

    for col in df.columns:
        df[col] = df[col].apply(limpiar_celda)
    print("3. Datos limpiados de caracteres invisibles.")

    # 4. Configuración de conexión
    engine = create_engine("postgresql://postgres:Naruto10@localhost:5432/farmaceutica_ia")

    # 5. Intento de subida con manejo de errores crudos
    print("4. Intentando inyectar datos...")
    df.to_sql('inventario_logistico', engine, if_exists='replace', index=False)
    
    print("\n" + "="*50)
    print("¡LO LOGRAMOS! La base de datos ha sido actualizada.")
    print("="*50)

except Exception as e:
    print("\n--- ERROR DETECTADO ---")
    # Intentamos mostrar el error de forma que no explote la terminal
    print(f"Detalle técnico: {str(e).encode('ascii', 'ignore').decode('ascii')}")
    print("\nSi el error persiste, intentaremos una ruta alternativa en el siguiente paso.")