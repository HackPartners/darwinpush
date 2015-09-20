#!/usr/bin/env python3

from darwinpush import Client, Listener
from darwinpush.messages.AssociationMessage import AssociationCategory

import os
import time

# Create a listener to process the messages.
class MyListener(Listener):
    def __init__(self, q):
        # Any setup if needed.

        # Finally, call the Super Class initialiser.
        super().__init__(q)

    def on_schedule_message(self, message):
        print("Schedule")

    def on_deactivated_message(self, message):
        print("Deactivated message")

    def on_association_message(self, message):
        print("Association")

    def on_alarm_message(self, message):
        print("Alarm message")

    def on_station_message(self, message):
        print("Station message")

    def on_tracking_id_message(self, message):
        print("Tracking ID message")

    def on_train_alert_message(self, message):
        print("Train alert message")

    def on_train_order_message(self, message):
        print("Train order message")
    
    def on_train_status_message(self, message):
        print("Train status message")

# Instantiate the Push Port client.
client = Client(
    os.environ["STOMP_USER"],
    os.environ["STOMP_PASS"],
    os.environ["STOMP_QUEUE"],
    MyListener
)

# Connect the Push Port client.
client.connect()

# Keep the main thread running indefinitely while we receive messages.
while True:
    time.sleep(1)


