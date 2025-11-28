import boto3
import json
import random
import time
from faker import Faker
from datetime import datetime

# ============================
# CONFIGURAÇÕES
# ============================
STREAM_NAME = "shoptrend-events-stream"
REGION = "us-east-1"
EVENTS_PER_SECOND = 2

fake = Faker()
kinesis = boto3.client("kinesis", region_name=REGION)

# ============================
# CATÁLOGO DE PRODUTOS (fixo e identificável)
# ============================
PRODUCT_CATALOG = [
    {"product_id": "p123", "name": "Camiseta Básica", "price": 49.90},
    {"product_id": "p456", "name": "Calça Jeans", "price": 129.90},
    {"product_id": "p789", "name": "Tênis Esportivo", "price": 299.00},
    {"product_id": "p321", "name": "Boné Preto", "price": 39.90},
    {"product_id": "p654", "name": "Mochila Escolar", "price": 89.90}
]

def pick_product():
    """Escolhe um produto aleatório do catálogo."""
    return random.choice(PRODUCT_CATALOG)

# ============================
# GERADORES DE EVENTOS
# ============================
def generate_pageview():
    product = pick_product()
    return {
        "event_type": "pageview",
        "event_id": fake.uuid4(),
        "user_id": fake.uuid4(),
        "session_id": fake.uuid4(),
        "page": random.choice(["home", "product", "checkout", "cart"]),
        "product": {
            "product_id": product["product_id"],
            "product_name": product["name"],
            "price": product["price"],
        },
        "timestamp": datetime.utcnow().isoformat(),
    }


def generate_add_to_cart():
    product = pick_product()
    return {
        "event_type": "add_to_cart",
        "event_id": fake.uuid4(),
        "user_id": fake.uuid4(),
        "session_id": fake.uuid4(),
        "product": {
            "product_id": product["product_id"],
            "product_name": product["name"],
            "price": product["price"]
        },
        "quantity": random.randint(1, 3),
        "timestamp": datetime.utcnow().isoformat(),
    }


def generate_checkout():

    num_items = random.randint(1, 4)
    cart_items = []
    total_value = 0

    for _ in range(num_items):
        product = pick_product()
        quantity = random.randint(1, 3)

        cart_items.append({
            "product_id": product["product_id"],
            "product_name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })

        total_value += product["price"] * quantity

    return {
        "event_type": "checkout",
        "event_id": fake.uuid4(),
        "user_id": fake.uuid4(),
        "session_id": fake.uuid4(),
        "cart_items": cart_items,
        "cart_value": round(total_value, 2),
        "timestamp": datetime.utcnow().isoformat(),
    }


def generate_order_confirmed():
    product = pick_product()
    quantity = random.randint(1, 3)
    total_value = round(product["price"] * quantity, 2)

    return {
        "event_type": "order_confirmed",
        "event_id": fake.uuid4(),
        "user_id": fake.uuid4(),
        "session_id": fake.uuid4(),
        "order_id": fake.uuid4(),

        "product": {
            "product_id": product["product_id"],
            "product_name": product["name"],
            "price": product["price"]
        },

        "quantity": quantity,
        "total_value": total_value,
        "timestamp": datetime.utcnow().isoformat(),
    }


# ============================
# LOOP PRINCIPAL
# ============================
EVENT_GENERATORS = [
    generate_pageview,
    generate_add_to_cart,
    generate_checkout,
    generate_order_confirmed
]

print(f"Enviando eventos para o Kinesis Stream: {STREAM_NAME}")

while True:
    for _ in range(EVENTS_PER_SECOND):
        event = random.choice(EVENT_GENERATORS)()
        kinesis.put_record(
            StreamName=STREAM_NAME,
            Data=json.dumps(event),
            PartitionKey=event["user_id"]
        )
        print("Enviado:", event)

    time.sleep(1)
