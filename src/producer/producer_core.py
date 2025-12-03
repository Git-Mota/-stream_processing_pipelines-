import time
import random
from utils import create_kinesis_client, get_stream_name, send_to_kinesis
from events import EVENT_GENERATORS

def run_producer(event_origin: str, events_per_second: int):
    kinesis = create_kinesis_client()
    stream = get_stream_name()

    print(f"[START] Producer iniciado para: {event_origin}")
    print(f"[STREAM] Stream: {stream}")

    while True:
        for _ in range(events_per_second):
            event_fn = random.choice(EVENT_GENERATORS)
            event = event_fn(event_origin)
            send_to_kinesis(kinesis, stream, event)
            print("Enviado:", event)

        time.sleep(1)
