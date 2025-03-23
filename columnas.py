import csv

# Ruta del archivo CSV
file_path = r'C:\Users\alexj\OneDrive\Escritorio\PL SQL ETL\Sample - Superstore.csv'

# Leer encabezados
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)  # Primera fila contiene los encabezados

    # Imprimir los nombres de las columnas
    print(headers)