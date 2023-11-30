import json

# Cargar los archivos JSON
with open('a.json') as file_a:
    data_a = json.load(file_a)

with open('b.json') as file_b:
    data_b = json.load(file_b)

# Lista de claves a buscar en B.json
claves_a_buscar = ["CC","OO", "OR", "OC","CO", "CR"]  # Agrega las claves que desees

# Buscar coincidencias en B.json
for item_b in data_b['invoices']:
    invoice_class = item_b['invoiceHeader']['invoiceClass']
    
    if invoice_class in claves_a_buscar:
        # Encontrar el valor correspondiente en A.json
        matching_item = next((item_a for item_a in data_a if item_a['clave'] == invoice_class), None)
        
        if matching_item:
            # Añadir la línea al mappedData en B.json
            if 'mappedData' not in item_b:
                item_b['mappedData'] = {}
            item_b['mappedData']['invoiceClassDescription'] = matching_item['valor']




# Lista de claves a buscar en B.json
claves_a_buscar = ["AF","FC", "FA"]  # Agrega las claves que desees

# Buscar coincidencias en B.json
for item_b in data_b['invoices']:
    invoice_class = item_b['invoiceHeader']['invoiceDocument']
    
    if invoice_class in claves_a_buscar:
        # Encontrar el valor correspondiente en A.json
        matching_item = next((item_a for item_a in data_a if item_a['clave'] == invoice_class), None)
        
        if matching_item:
            # Añadir la línea al mappedData en B.json
            if 'mappedData' not in item_b:
                item_b['mappedData'] = {}
            item_b['mappedData']['invoiceDocumentDescription'] = matching_item['valor']


# Guardar los cambios en C.json
with open('c.json', 'w') as file_c:
    json.dump(data_b, file_c, indent=2)
