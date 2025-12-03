import random
from utils import pick_product, now_iso, uuid


def generate_pageview(origin):
    product = pick_product()
    return {
        "event_origin": origin,
        "event_type": "pageview",
        "event_id": uuid(),
        "user_id": uuid(),
        "session_id": uuid(),
        "page": random.choice(["home", "product", "checkout", "cart"]),
        "product": {
            "product_id": product["product_id"],
            "product_name": product["name"],
            "price": product["price"],
        },
        "timestamp": now_iso(),
    }


def generate_add_to_cart(origin):
    product = pick_product()
    return {
        "event_origin": origin,
        "event_type": "add_to_cart",
        "event_id": uuid(),
        "user_id": uuid(),
        "session_id": uuid(),
        "product": {
            "product_id": product["product_id"],
            "product_name": product["name"],
            "price": product["price"]
        },
        "quantity": random.randint(1, 3),
        "timestamp": now_iso(),
    }


def generate_checkout(origin):
    import random

    items = []
    total = 0
    for _ in range(random.randint(1, 4)):
        product = pick_product()
        qty = random.randint(1, 3)
        items.append({
            "product_id": product["product_id"],
            "product_name": product["name"],
            "price": product["price"],
            "quantity": qty
        })
        total += product["price"] * qty

    return {
        "event_origin": origin,
        "event_type": "checkout",
        "event_id": uuid(),
        "user_id": uuid(),
        "session_id": uuid(),
        "cart_items": items,
        "cart_value": round(total, 2),
        "timestamp": now_iso(),
    }


def generate_order_confirmed(origin):
    product = pick_product()
    qty = random.randint(1, 3)
    total = product["price"] * qty

    return {
        "event_origin": origin,
        "event_type": "order_confirmed",
        "event_id": uuid(),
        "user_id": uuid(),
        "session_id": uuid(),
        "order_id": uuid(),
        "product": {
            "product_id": product["product_id"],
            "product_name": product["name"],
            "price": product["price"]
        },
        "quantity": qty,
        "total_value": round(total, 2),
        "timestamp": now_iso(),
    }


EVENT_GENERATORS = [
    generate_pageview,
    generate_add_to_cart,
    generate_checkout,
    generate_order_confirmed
]
