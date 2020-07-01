# Machine Learning in OpenShift (Binary Classification) Materials

## Requirements

You will need a machine which can get OpenShift meeting the following requirements:

* python
* **urllib.request**, **ssl** and **kafka** python modules.

## Files

+ [demo-odh.ipynb](demo-odh.ipynb) jupyter notebook to train a Convolutional Neural Network.
+ [demo-odh-prod.ipynb](demo-odh-prod.ipynb) jupyter notebook which will use the model trained using the previous jupyter notebook.
+ [download-some-pictures.py](download-some-pictures.py) script to download some pictures from the internet. You can use these pictures to send them to kafka to be classified by a neural network. You will have to edit the script and configure the directory where you want the pictures to be downloaded.
+ [kafka-producer.py](kafka-producer.py) python script to send one picture to kafka.
+ [kafka-consumer.py](kafka-consumer.py) python script to get one picture from kafka.
+ [upload-pictures-to-kafka.sh](upload-pictures-to-kafka.sh) bash script to send all jpg pictures from a directory to kafka.
+ [well-trained-model.h5](well-trained-model.h5) weights for a model which was trained using 25000 images.