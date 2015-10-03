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

    def on_schedule_message(self, message, source):
        print(self.now(), source, "Schedule")

    def on_deactivated_message(self, message, source):
        print(self.now(), source, "Deactivated message")

    def on_association_message(self, message, source):
        print(self.now(), source, "Association")

    def on_alarm_message(self, message, source):
        print(self.now(), source, "Alarm message")

    def on_station_message(self, message, source):
        print(self.now(), source, "Station message")

    def on_tracking_id_message(self, message, source):
        print(self.now(), source, "Tracking ID message")

    def on_train_alert_message(self, message, source):
        print(self.now(), source, "Train alert message")

    def on_train_order_message(self, message, source):
        print(self.now(), source, "Train order message")

    def on_train_status_message(self, message, source):
        print(self.now(), source, "Train status message")

if __name__ == "__main__":
    # Instantiate the Push Port client.
    client = Client(
        os.environ["STOMP_USER"],
        os.environ["STOMP_PASS"],
        os.environ["STOMP_QUEUE"],
        MyListener,
        ftp_user=os.environ["FTP_USER"],
        ftp_passwd=os.environ["FTP_PASSWD"]
    )

    # Do not connect to stomp, just download and parse the logs from FTP for
    # the last `downtime` seconds and quit.
    client.connect(downtime=600, stomp=False)
    print("All done. Bye :)")
    client.disconnect()
