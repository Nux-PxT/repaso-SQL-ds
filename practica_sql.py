import pandas as pd
import sqlite3

# 1. Cargar el archivo CSV en un DataFrame
df = pd.read_csv("data/ventas_tecnologia.csv")

# 2. Crear una conexión con una base de datos SQLite en memoria
conexion = sqlite3.connect(":memory:")

# 3. Crear la tabla ventas_tecnologia a partir del DataFrame
df.to_sql(
    "ventas_tecnologia",
    conexion,
    index=False,
    if_exists="replace"
)

# ---------------------------------------------------------
# CONSIGNA 1: Selección simple
# Obtener los nombres de los productos y sus precios,
# ordenados alfabéticamente por nombre.
# ---------------------------------------------------------
seleccion_simple = pd.read_sql_query(
    """
    SELECT producto, precio_unitario
    FROM ventas_tecnologia
    ORDER BY producto ASC;
    """,
    conexion
)

print("SELECCIÓN SIMPLE")
print(seleccion_simple)
print()


# ---------------------------------------------------------
# CONSIGNA 2: Filtrado crítico
# Obtener todas las ventas realizadas en Colombia
# cuyo precio unitario sea mayor a 500.
# ---------------------------------------------------------
filtrado_critico = pd.read_sql_query(
    """
    SELECT *
    FROM ventas_tecnologia
    WHERE pais = 'Colombia'
      AND precio_unitario > 500;
    """,
    conexion
)

print("FILTRADO CRÍTICO")
print(filtrado_critico)
print()


# ---------------------------------------------------------
# CONSIGNA 3: Búsqueda de valores nulos
# Identificar los registros cuya categoría no está informada.
# ---------------------------------------------------------
busqueda_nulos = pd.read_sql_query(
    """
    SELECT *
    FROM ventas_tecnologia
    WHERE categoria IS NULL;
    """,
    conexion
)

print("BÚSQUEDA DE NULOS")
print(busqueda_nulos)
print()


# ---------------------------------------------------------
# CONSIGNA 4: Análisis de rendimiento (agregación)
# Calcular los ingresos totales por categoría:
# cantidad multiplicada por precio_unitario, sumado por grupo.
# ---------------------------------------------------------
analisis_de_rendimiento = pd.read_sql_query(
    """
    SELECT
        categoria,
        SUM(cantidad * precio_unitario) AS ingresos_totales
    FROM ventas_tecnologia
    GROUP BY categoria;
    """,
    conexion
)

print("ANÁLISIS DE RENDIMIENTO")
print(analisis_de_rendimiento)
print()


# ---------------------------------------------------------
# CONSIGNA 5: Filtro de élite (HAVING)
# Mostrar únicamente las categorías cuyos ingresos totales
# superan los 10.000.
# ---------------------------------------------------------
filtro_elite = pd.read_sql_query(
    """
    SELECT
        categoria,
        SUM(cantidad * precio_unitario) AS ingresos_totales
    FROM ventas_tecnologia
    GROUP BY categoria
    HAVING SUM(cantidad * precio_unitario) > 10000;
    """,
    conexion
)

print("FILTRO DE ÉLITE")
print(filtro_elite)
print()


# 6. Cerrar la conexión con SQLite
conexion.close()
