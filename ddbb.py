import psycopg2
import json

# Configuración de conexión a PostgreSQL
db_config = {
    'host': '10.0.148.52',
    'port': '5432',
    'database': 'db_catalog',
    'user': 'users_catalog',
    'password': 'DVhfhgghjkg#@2029',
}

# Consulta SQL
sql_query = 'SELECT clave, valor FROM etl_map'

# Realizar la consulta y convertir los resultados a JSON
def query_and_convert_to_json():
    # Conectar a la base de datos
    conn = psycopg2.connect(**db_config)

    try:
        # Crear un cursor
        cursor = conn.cursor()

        # Ejecutar la consulta
        cursor.execute(sql_query)

        # Obtener los resultados
        rows = cursor.fetchall()

        # Convertir los resultados a una lista de diccionarios
        results = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]

        # Convertir la lista a JSON
        json_result = json.dumps(results, indent=2)

        # Imprimir el resultado
        print(json_result)

    except Exception as e:
        print(f'Error al ejecutar la consulta: {e}')

    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

# Uso de la función
query_and_convert_to_json()
