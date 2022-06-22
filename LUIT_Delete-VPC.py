#!usr/bin/envpython3.7

import boto3
client=boto3.client("ec2")
response=client.delete_vpc(
    VpcId='vpc-0ddfcf3301260fd62')
