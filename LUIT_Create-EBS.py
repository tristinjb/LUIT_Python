import boto3
ec2_client=boto3.client("ec2")
ec2_client.create_volume(AvailabiltyZone='us-east-1a',
      Encrypted=True,
      Size=12,
      SnapShotId='snap-0bca824c5b145e4e2',
      VolumeType='gp2')
      