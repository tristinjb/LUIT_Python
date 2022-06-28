#!/usr/bin/env Python3.7

#This scans the table

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movies')
response = table.scan()
response['Items']
print(len(response),"\n")
print('response')
