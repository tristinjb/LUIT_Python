#!usr/bin/env pyhton3.7

#delete s3 objects

import boto3

#delete single object
s3_resource=boto3.client("s3")
s3_resource.delete_object(
    Bucket='Newbucket',
    Key='filetxt.png')
    
#delete mutiple files

import os
import glob

#find all the objects from the bucket
objects=s3_resource.list_objects(Buckets="Newbucket")["Contents"]
len(objects)

for object in objects:
    reponse=s3_resource.delete_object(Bucket='Newbucket',
    Key=object["Key"])
    
    print(reponse)