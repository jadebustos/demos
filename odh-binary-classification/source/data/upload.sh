#!/bin/bash


#s3cmd -c s3cfg.cfg mb s3://validation-cat
#s3cmd -c s3cfg.cfg mb s3://validation-dog
#s3cmd -c s3cfg.cfg mb s3://train-cat
#s3cmd -c s3cfg.cfg mb s3://train-dog
#s3cmd -c s3cfg.cfg mb s3://test-cat
#s3cmd -c s3cfg.cfg mb s3://test-dog

for i in $(seq 1 10)
do
  filename=$i".jpg"
  DIR="training/cat"
  BUCKET="train-cat"
  s3cmd -c s3cfg.cfg put $DIR"/"$filename s3://$BUCKET/$filename
  DIR="training/dog"
  BUCKET="train-dog"
  s3cmd -c s3cfg.cfg put $DIR"/"$filename s3://$BUCKET/$filename
  DIR="validation/dog"
  BUCKET="validation-dog"
  s3cmd -c s3cfg.cfg put $DIR"/"$filename s3://$BUCKET/$filename
  DIR="validation/cat"
  BUCKET="validation-cat"
  s3cmd -c s3cfg.cfg put $DIR"/"$filename s3://$BUCKET/$filename
  DIR="test/cat"
  BUCKET="test-cat"
  s3cmd -c s3cfg.cfg put $DIR"/"$filename s3://$BUCKET/$filename
  DIR="test/dog"
  BUCKET="test-dog"
  s3cmd -c s3cfg.cfg put $DIR"/"$filename s3://$BUCKET/$filename
done
