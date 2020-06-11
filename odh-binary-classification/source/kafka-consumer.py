#!/usr/bin/python2

import time
import argparse
import os
import ssl

from kafka import KafkaConsumer
from kafka.errors import KafkaError


def parse_args():
    parser = argparse.ArgumentParser(description='Send bytes to a kafka topic')
    parser.add_argument('--topic', default="rhte")
    parser.add_argument('--brokers', required=True)
    parser.add_argument('--skip-tls-verify', action='store_true', default=True)
    parser.add_argument('--use-tls', action='store_true', default=False)
    return parser.parse_args()

def main():
    TEST_SIZE=1
    args = parse_args()
    brokers = args.brokers.split(',')
    if args.use_tls:
        consumer = KafkaConsumer(args.topic,
                         bootstrap_servers=brokers,
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         ssl_context= ssl._create_unverified_context(),
                         security_protocol='SSL',
                         heartbeat_interval_ms=1000,
                         max_poll_records=TEST_SIZE,
                         group_id='test-consumer-group')
    else:
        consumer = KafkaConsumer(args.topic,
                         bootstrap_servers=brokers,
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         heartbeat_interval_ms=1000,
                         max_poll_records=TEST_SIZE,
                         group_id='test-consumer-group')

    # pool kafka
    consumer.poll()
    # read
    for msg in consumer:
        message = msg.value
        fd = open('kafka-msg.jpg', 'wb')
        fd.write(message)
        fd.close()
        break
    
if __name__ == "__main__":
    main()
