import argparse
import json
import redis
import logging

logging.basicConfig(level=logging.INFO)

redis_client = redis.Redis()


def process_message(message, bad_guys):
    try:
        data = json.loads(message.decode('utf-8'))
        print(type(data))
        if 'metadata' not in data or 'amount' not in data:
            logging.error(f"Invalid message format: {data}")
            return
        metadata = data['metadata']
        from_account = metadata.get('from')
        to_account = metadata.get('to')
        amount = data['amount']
        if str(to_account) in bad_guys and amount > 0:
            metadata['from'] = to_account
            metadata['to'] = from_account
        data = {'metadata': metadata, 'amount': amount}
        json_data = json.dumps(data)
        logging.info(json_data)

    except AttributeError:
        logging.error(f"Could not decode message: {message}")
        pass


def consume(bad_guys):
    pubsub = redis_client.pubsub()
    pubsub.subscribe('transactions')
    while True:
        message = pubsub.get_message()
        if message:
            process_message(message['data'], bad_guys)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', type=str)
    args = parser.parse_args()
    bad_guys = args.e.split(',')
    consume(bad_guys)
