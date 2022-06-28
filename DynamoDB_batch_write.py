#!/usr/bin/env Python3.7

# Script adds multiple items to the table

import boto3

dynamodb = boto3.resource('DynamoDB')
table = dynamodb.Tables('Movies')

with table.batch_write() as batch:
    batch.put_item(Item={"Title": "Monster Inc.01", "Genres": "Comedy"})
    batch.put_item(Item={"Title": "Monster Inc.02", "Genres": "Horror"})
    batch.put_item(Item={"Title": "Monster Inc.03", "Genres": "Comedy"})
    batch.put_item(Item={"Title": "Monster Inc.04", "Genres": "Horror"})
    batch.put_item(Item={"Title": "Monster Inc.05", "Genres": "Comedy"})
    batch.put_item(Item={"Title": "Monster Inc.06", "Genres": "Horror"})
    batch.put_item(Item={"Title": "Monster Inc.07", "Genres": "Comedy"})
    batch.put_item(Item={"Title": "Monster Inc.08", "Genres": "Horror"})
    batch.put_item(Item={"Title": "Monster Inc.09", "Genres": "Comedy"})
    batch.put_item(Item={"Title": "Monster Inc.10", "Genres": "Horror"})
    
#Could have been more creative I know!