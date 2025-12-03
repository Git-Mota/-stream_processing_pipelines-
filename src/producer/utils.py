import os
from dotenv import load_dotenv
import boto3
import json
import random
from faker import Faker
from datetime import datetime

load_dotenv()
fake = Faker()

PRODUCT_CATALOG = [
    {"product_id": "p123", "name": "Camiseta Básica", "price": 49.90},
    {"product_id": "p456", "name": "Calça Jeans", "price": 129.90},
    {"product_id": "p789", "name": "Tênis Esportivo", "price": 299.00},
    {"product_id": "p321", "name": "Boné Preto", "price": 39.90},
    {"product_id": "p654", "name": "Mochila Escolar", "price": 89.90}
]

def get_env(key, default=None):
    return os.getenv(key, default)

def create_kinesis_client():
    region = get_env("AWS_REGION")
    return boto3.client("kinesis", region_name=region)

def get_stream_name():
    return get_env("KINESIS_STREAM_NAME")

def pick_product():
    return random.choice(PRODUCT_CATALOG)

def now_iso():
    return datetime.utcnow().isoformat()

def uuid():
    return fake.uuid4()

def send_to_kinesis(kinesis, stream, event):
    kinesis.put_record(
        StreamName=stream,
        Data=json.dumps(event),
        PartitionKey=event["user_id"]
    )
