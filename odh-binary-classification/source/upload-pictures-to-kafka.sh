#!/bin/bash

# kafka endpoint
BROKER=kafka.example.org:443
# kafka topic where to send pictures
TOPIC=predict
# directory to read pictures to be send to kafka topic
DIR=predict

for item in $(ls $DIR/*.jpg)
do
  echo "Uploading "$item" to topic "$TOPIC
  python2 kafka_producer.py --topic $TOPIC --brokers $BROKER --skip-tls-verify --use-tls --file $item
  if [ $? -ne 0 ]
  then
    echo "Ocurrio un error."
  fi
done
