# Concept Demo — AWS + Google Cloud Interoperability
# pip install boto3 google-cloud-storage

import boto3
from google.cloud import storage

AWS_BUCKET = "aws-bucket"
GCP_BUCKET = "gcp-bucket"

def move_aws_to_gcp(filename):
    # download from aws
    s3 = boto3.client('s3')
    s3.download_file(AWS_BUCKET, filename, filename)

    # upload to gcp
    client = storage.Client()
    bucket = client.bucket(GCP_BUCKET)
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)

    print("Interoperability success")

move_aws_to_gcp("demo.txt")
