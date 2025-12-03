import os
from producer_core import run_producer

origin = os.getenv("EVENT_ORIGIN_WEB")
eps = int(os.getenv("EVENTS_PER_SECOND_WEB"))

run_producer(event_origin=origin, events_per_second=eps)
