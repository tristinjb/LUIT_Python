#!usr/bin/env python3.7
import boto3
s3_resource=boto3.client("s3")
s3_resource.upload_file('Filename','Bucket','Key')

