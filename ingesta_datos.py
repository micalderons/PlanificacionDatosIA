import pandas as pd
import random

# Configuraciones iniciales
num_registros = 5000
random.seed(42) # Para que siempre genere los mismos datos si lo vuelves a correr

# Diccionario de medicamentos y sus temperaturas ideales de conservación
medicamentos_info = [
    {"nombre": "Insulina Glargina", "t_min": 2, "t_max": 8},
    {"nombre": "Vacuna ARNm COVID-19", "t_min": -80, "t_max": -60},
    {"nombre": "Suero Fisiologico", "t_min": 15, "t_max": 25},
    {"nombre": "Amoxicilina Suspension", "t_min": 2, "t_max": 8},
    {"nombre": "Paracetamol Inyectable", "t_min": 15, "t_max": 30}
]

datos = []

print("Generando datos simulados de logística farmacéutica...")

for i in range(1, num_registros + 1):
    med = random.choice(medicamentos_info)
    id_lote = f"LOTE-{str(i).zfill(5)}"
    dias_caducar = random.randint(1, 180) # Días de vida útil restantes
    distancia = random.randint(10, 800) # Distancia al destino en km
    trafico = random.choice(["Bajo", "Normal", "Alto"])
    
    # Simulamos la temperatura del viaje (15% de las veces la cadena de frío falla)
    if random.random() < 0.15: 
        temp_viaje = round(random.uniform(med["t_max"] + 1, med["t_max"] + 10), 1) # Falla (se calienta)
    else:
        temp_viaje = round(random.uniform(med["t_min"], med["t_max"]), 1) # Viaje perfecto
        
    # --- Lógica de riesgo ---
    riesgo = "Bajo"
    # Si la temperatura del viaje se sale del rango, el riesgo es ALTO
    if temp_viaje > med["t_max"] or temp_viaje < med["t_min"]:
        riesgo = "Alto"
    # Si le quedan pocos días para caducar y el viaje es muy largo, riesgo ALTO
    elif dias_caducar < 10 and distancia > 400:
        riesgo = "Alto"
    # Si hay mucho tráfico y faltan menos de 30 días, riesgo MEDIO
    elif dias_caducar < 30 and trafico == "Alto":
        riesgo = "Medio"

    datos.append([
        id_lote, med["nombre"], dias_caducar, med["t_min"], med["t_max"], 
        distancia, trafico, temp_viaje, riesgo
    ])

# Convertimos la lista en un DataFrame (tabla) usando Pandas
df = pd.DataFrame(datos, columns=[
    "id_lote", "medicamento", "dias_para_caducar", "temp_ideal_min", 
    "temp_ideal_max", "distancia_ruta_km", "trafico_estimado", 
    "temp_registrada_viaje", "riesgo_perdida"
])

# Guardamos los datos en un archivo CSV
nombre_archivo = "dataset_medicamentos.xlsx"
df.to_excel(nombre_archivo, index=False)

print(f"¡Éxito! Se generó el archivo '{nombre_archivo}' con {num_registros} registros.")