#!usr/bin/envpython3.7
#Describing the VPC

import boto3
client=boto3.client("ec2")

#how to describe all vpc in your account

#this code did return information for me
     #response=client.describe_vpcs()
     #print(response)

#alternate option
#this option did not return any feed back to me when code was ran
x=client.describe_vpcs()
number_of_vpcs=x["Vpcs"]
len(number_of_vpcs)
#Adding (print(number_of_vpcs) did return a response when add to the code above

#finding the ID's for your VPCS in a list format
for vpc in number_of_vpcs:
    print(vpc["VpcId"])

#how to describe your vpc using a vpc id
x=client.describe_vpcs(VpcId=["VpcId"])


