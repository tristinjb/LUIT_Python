import boto3
ec2_client=boto3.client("ec2")

ec2_client.delete_snapshot('snap-0bca824c5b145e4e2')
