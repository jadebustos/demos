# How to use OpenShift and Opendatahub for Machine Learning workloads

This demo shows you how to create Machine Learning models and export them to be used for other applications.

In this demo you will train a Convolutional Neural Network to solve a binary classification problem. 

The data to train the model will be stored in a S3 bucket in Ceph.

Once the model is built you will test it sending pictures to a kafka topic to be predicted by your model.
