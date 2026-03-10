"""
This module connects to the CryptoCompare WebSocket API, receives real-time
cryptocurrency price updates, and publishes them to a Google Cloud Pub/Sub topic.
Make sure to set up your Google Cloud credentials and install the required
libraries before running this code.
"""

import websocket
import json
import os
from dotenv import load_dotenv
from google.cloud import pubsub_v1


load_dotenv("../.env")
# Load environment variables for Google Cloud Pub/Sub configuration
PROJECT_ID = os.getenv("PROJECT_ID")
TOPIC_NAME = os.getenv("TOPIC_NAME")

publisher = pubsub_v1.PublisherClient()
topic = f"projects/{PROJECT_ID}/topics/{TOPIC_NAME}"


def on_error(ws, error):
    print(f"WebSocket error: {error}")


def on_close(ws):
    print("WebSocket connection closed")


def on_open(ws):
    print("WebSocket connection opened")
    subscribe_message = {
        "type": "subscribe",
        "channels": [{"name": "ticker", "product_ids": ["BTC-USD"]}],
    }
    ws.send(json.dumps(subscribe_message))


def on_message(ws, message):
    publisher.publish(topic, message.encode("utf-8"))


if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(
        "wss://ws-feed.exchange.coinbase.com",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.run_forever()
