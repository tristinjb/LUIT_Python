#Launching an EC2

import boto3
ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId="ami-0cff7528ff583bf9a",
InstanceType="t2.micro",
MaxCount=1,
MinCount=1)

