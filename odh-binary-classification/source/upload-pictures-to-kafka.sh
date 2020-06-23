#!/bin/bash

# kafka endpoint
BROKER=odh-message-bus-kafka-bootstrap-binary-classification.apps.cluster-syone-a5ce.syone-a5ce.example.opentlc.com:443
# kafka topic where to send pictures
TOPIC=predict
# directory to read pictures to be send to kafka topic
DIR=data/predict

rm -Rf $DIR
mkdir -p $DIR

for item in $(ls $DIR/*.jpg)
do
  echo "Uploading "$item" to topic "$TOPIC
  python2 kafka-producer.py --topic $TOPIC --brokers $BROKER --skip-tls-verify --use-tls --file $item
  if [ $? -ne 0 ]
  then
    echo "Ocurrio un error."
  fi
done
