import pandas as pd

print("Iniciando proceso de limpieza y transformación de datos...")

# 1. Cargar el dataset original
nombre_archivo_entrada = "dataset_medicamentos.xlsx"
try:
    df = pd.read_excel(nombre_archivo_entrada)
    print(f"Dataset cargado exitosamente. Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{nombre_archivo_entrada}'. Ejecuta primero el script de ingesta.")
    exit()

# 2. Limpieza básica (Verificar valores nulos)
nulos = df.isnull().sum().sum()
if nulos > 0:
    print(f"Se encontraron {nulos} valores nulos. Procediendo a limpiarlos...")
    df = df.dropna() # Elimina las filas con datos faltantes
else:
    print("No se encontraron valores nulos. El dataset está íntegro.")

# 3. Transformación de variables de texto a numéricas (Encoding para la IA)
print("Transformando variables categóricas a numéricas...")

# Mapeo de la columna 'trafico_estimado'
mapeo_trafico = {"Bajo": 0, "Normal": 1, "Alto": 2}
df["trafico_estimado_num"] = df["trafico_estimado"].map(mapeo_trafico)

# Mapeo de la columna 'riesgo_perdida' (Nuestra variable a predecir)
mapeo_riesgo = {"Bajo": 0, "Medio": 1, "Alto": 2}
df["riesgo_perdida_num"] = df["riesgo_perdida"].map(mapeo_riesgo)

# 4. Creación de nuevas características (Feature Engineering)
# Creamos una columna que marque con '1' si la temperatura del viaje se salió del rango ideal, y '0' si se mantuvo bien.
print("Calculando alertas de ruptura de cadena de frío...")
df["falla_cadena_frio"] = (df["temp_registrada_viaje"] > df["temp_ideal_max"]) | (df["temp_registrada_viaje"] < df["temp_ideal_min"])
df["falla_cadena_frio"] = df["falla_cadena_frio"].astype(int) # Convierte True/False a 1/0

# 5. Guardar el dataset limpio y transformado
nombre_archivo_salida = "dataset_medicamentos_limpio.xlsx"
df.to_excel(nombre_archivo_salida, index=False)

print(f"\n¡Proceso finalizado con éxito!")
print(f"Datos listos para la Base de Datos guardados en: '{nombre_archivo_salida}'")