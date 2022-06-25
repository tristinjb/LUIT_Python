import boto3
ec2_boto3=boto3.client("ec2")

ec2_boto3.describe_snapshots(SnapshotIDs=[
    'snap-0bca824c5b145e4e2'
    ])