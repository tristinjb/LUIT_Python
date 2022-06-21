#!usr/bin/env python3.7
import boto3
s3_resource=boto3.client("s3")
s3_resource.list_buckets()["Buckets"][0]["CreationDate"]
creation_date=s3_resource.list_buckets()["Buckets"][0]["CreationDate"]
creation_date.strftime("%d%m%y_%H:%M:%S")
for buckets in s3_resource.list_buckets()["Buckets"]:
    print(buckets["Name"])
    print(buckets["CreationDate"])