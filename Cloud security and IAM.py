Cloud security and IAM
{
 "Version": "2012-10-17",
 "Statement": [{
     "Effect": "Allow",
     "Action": ["s3:*"],
     "Resource": "*"
 }]
}
# Security Implementation Demo

import boto3

kms = boto3.client('kms')

def enable_encryption(bucket):
    s3 = boto3.client('s3')
    s3.put_bucket_encryption(
      Bucket=bucket,
      ServerSideEncryptionConfiguration={
        'Rules':[{
          'ApplyServerSideEncryptionByDefault':{
             'SSEAlgorithm':'AES256'
          }
        }]
      }
    )
    print("Encryption enabled")

enable_encryption("demo-bucket")
