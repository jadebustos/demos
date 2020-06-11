# Machine Learning in OpenShift (Binary Classification) Materials

## Requirements

You will need a machine which can get OpenShift meeting the following requirements:

* python 3.7
* **urllib.request**, **ssl** and **kafka** python modules.

## Scripts

+ [download-some-pictures.py](download-some-pictures.py) script to download some pictures from the internet. You can use these pictures to send them to kafka to be classified by a neural network. You will have to edit the script and configure the directory where you want the pictures to be downloaded.
+ [kafka-producer.py](kafka-producer.py) python script to send one picture to kafka.
+ [kafka-consumer.py](kafka-consumer.py) python script to get one picture from kafka.
+ [upload-pictures-to-kafka.sh](upload-pictures-to-kafka.sh) bash script to send all jpg pictures from a directory to kafka.