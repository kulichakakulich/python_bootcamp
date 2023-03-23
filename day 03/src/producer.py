import json
import random
import redis
import logging
import time

logging.basicConfig(level=logging.INFO)

redis_client = redis.Redis()


def generate_account_number():
    return random.randint(1000000000, 9999999999)


def generate_message():
    from_account = generate_account_number()
    to_account = generate_account_number()
    amount = random.randint(-10000, 10000)
    return {
        "metadata": {
            "from": from_account,
            "to": to_account
        },
        "amount": amount
    }


def produce():
    r = redis.Redis(host='127.0.0.1', port=6379, db=0,)
    while True:
        message = generate_message()
        json_message = json.dumps(message)
        r.publish('transactions', json_message)
        logging.info(json_message)
        time.sleep(0.2)


if __name__ == '__main__':
    produce()
