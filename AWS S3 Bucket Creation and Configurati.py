# AWS S3 Bucket Creation and Configuration
# Requires: pip install boto3

import boto3
from botocore.exceptions import ClientError

AWS_REGION = "ap-south-1"
BUCKET_NAME = "nidhi-workplace-demo-bucket"

s3 = boto3.client('s3', region_name=AWS_REGION)

def create_bucket():
    try:
        s3.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={'LocationConstraint': AWS_REGION}
        )
        print("Bucket created successfully")
    except ClientError as e:
        print(e)

def upload_example_files():
    # uploading demo files
    files = ["demo1.txt", "demo2.txt"]
    for f in files:
        s3.upload_file(f, BUCKET_NAME, f)
    print("Files uploaded")

def set_public_read_permission():
    policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "PublicRead",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*"
        }]
    }

    s3.put_bucket_policy(
        Bucket=BUCKET_NAME,
        Policy=str(policy)
    )
    print("Permission configured")

create_bucket()
upload_example_files()
set_public_read_permission()
