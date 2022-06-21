#!usr/bin/env pyhton3.7
import boto3
resource=boto3.resource("s3")
for bucket in resource.buckets.all():
    print(bucket.name)
bucket_list=list(resource.buckets.all())
len(bucket_list)


