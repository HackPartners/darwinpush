#!/usr/bin/env python3

from darwinpush import Client, Listener
from darwinpush.messages.AssociationMessage import AssociationCategory

import os
import time

# Create a listener to process the messages.
class MyListener(Listener):
    def __init__(self, q, quit_event):
        # Any setup if needed.

        # Finally, call the Super Class initialiser.
        super().__init__(q, quit_event)

    def now(self):
        return time.strftime("%d/%m/%y %H:%M:%S")

    def on_schedule_message(self, message):
        print(self.now(), "Schedule")

    def on_deactivated_message(self, message):
        print(self.now(), "Deactivated message")

    def on_association_message(self, message):
        print(self.now(), "Association")

    def on_alarm_message(self, message):
        print(self.now(), "Alarm message")

    def on_station_message(self, message):
        print(self.now(), "Station message")

    def on_tracking_id_message(self, message):
        print(self.now(), "Tracking ID message")

    def on_train_alert_message(self, message):
        print(self.now(), "Train alert message")

    def on_train_order_message(self, message):
        print(self.now(), "Train order message")

    def on_train_status_message(self, message):
        print(self.now(), "Train status message")

if __name__ == "__main__":
    # Instantiate the Push Port client.
    client = Client(
        os.environ["STOMP_USER"],
        os.environ["STOMP_PASS"],
        os.environ["STOMP_QUEUE"],
        MyListener
    )

    # Connect the Push Port client.
    client.connect()
    print("Connected")
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print("Disconnecting client...")
        client.disconnect()
        print("Bye")
