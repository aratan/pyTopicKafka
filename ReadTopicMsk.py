# Configura los detalles de tu broker
brokers = 'b-2.asdfghjk.c8.kafka.eu-west-1.amazonaws.com:9092'
group_id = 'tu_group_id'  # Asigna un ID de grupo único para consumidores
topic = 'invoice.v1.annotated'  # Nombre del tema

# Configuración del productor (si necesitas producir mensajes)
producer_config = {
    'bootstrap.servers': brokers,
    # Agrega más configuraciones según sea necesario
}

# Configuración del consumidor (si necesitas consumir mensajes)
consumer_config = {
    'bootstrap.servers': brokers,
    'group.id': group_id,
    # Agrega más configuraciones según sea necesario
}

# Ejemplo de productor
def produce_hello_world_message():
    producer = Producer(producer_config)

    try:
        # Produce un mensaje en el tema especificado
        producer.produce(topic, key='HOLA', value='MUNDO')

        # Espera a que todos los mensajes sean entregados o haya un error
        producer.flush()

    except Exception as e:
        print(f'Error al producir mensaje: {e}')

    finally:
        # Cierra el productor
        producer.close()

# Ejemplo de consumidor
def consume_messages():
# Configuración del productor (si necesitas producir mensajes)
    producer_config = {
        'bootstrap.servers': 'b-2.devarya.uh9pny.c8.kafka.eu-west-1.amazonaws.com:9092',
        'client.id': 'your_client_id',
        'acks': 'all',
        'retries': 3,
    'batch.size': 16384,
    'linger.ms': 1,
    'compression.type': 'gzip',
    # Agrega más configuraciones según sea necesario
    }
    consumer = Consumer(consumer_config)

    # Suscríbete al tema de interés
    consumer.subscribe([topic])

    try:
        while True:
            # Espera mensajes y procesa
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # No hay más mensajes en la partición
                    continue
                else:
                    print(f'Error al consumir mensaje: {msg.error()}')
                    break

            # Procesa el mensaje
            print(f'Mensaje recibido: {msg.value().decode("utf-8")}')

    except KeyboardInterrupt:
        pass

    finally:
        # Cierra el consumidor
        consumer.close()

# Uso de los ejemplos
consume_messages()  # Consume mensajes del tema
produce_hello_world_message()  # Produce un mensaje con clave "HOLA" y valor "MUNDO"
