import json

# Cargar los archivos JSON
with open('a.json') as file_a:
    data_a = json.load(file_a)

with open('b.json') as file_b:
    data_b = json.load(file_b)

# Lista de claves a buscar en B.json para invoiceClass
claves_a_buscar_invoice_class = ["CC", "OO", "OR", "OC", "CO", "CR"]

# Lista de claves a buscar en B.json para invoiceDocument
claves_a_buscar_invoice_document = ["AF", "FC", "FA"]

# Buscar coincidencias en B.json para invoiceClass
for item_b in data_b['invoices']:
    invoice_class = item_b['invoiceHeader']['invoiceClass']
    
    if invoice_class in claves_a_buscar_invoice_class:
        # Encontrar el valor correspondiente en A.json
        matching_item = next((item_a for item_a in data_a if item_a['clave'] == invoice_class), None)
        
        if matching_item:
            # Añadir o actualizar la línea en mappedData en B.json
            mapped_data = item_b.get('mappedData', {})
            mapped_data['invoiceClassDescription'] = matching_item['valor']
            item_b['mappedData'] = mapped_data

# Buscar coincidencias en B.json para invoiceDocument
for item_b in data_b['invoices']:
    invoice_document = item_b['invoiceHeader']['invoiceDocument']
    
    if invoice_document in claves_a_buscar_invoice_document:
        # Encontrar el valor correspondiente en A.json
        matching_item = next((item_a for item_a in data_a if item_a['clave'] == invoice_document), None)
        
        if matching_item:
            # Añadir o actualizar la línea en mappedData en B.json
            mapped_data = item_b.get('mappedData', {})
            mapped_data['invoiceDocumentDescription'] = matching_item['valor']
            item_b['mappedData'] = mapped_data

# Guardar los cambios en C.json
with open('c.json', 'w') as file_c:
    json.dump(data_b, file_c, indent=2)
