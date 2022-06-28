#!/usr/bin/env Python3.7

#1)Create a DynamoDB table for something of your choosing (e.g. movies, food, games).

#Creating a movies table
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table (
    TableName = 'Movies',
       KeySchema = [
           {
               'AttributeName': 'Title',
               'KeyType': 'HASH'
           },
           {
               'AttributeName': 'Genres',
               'KeyType': 'RANGE'
           }
           ],
           AttributeDefiitions = [
               {
                   'AttributeName': 'Ttile',
                   'AttributeType': 'S'
               },
               {
                   'AttributeName': 'Genres',
                   'AttributeType': 'S'
                }   
               ],
               ProvisionedThroughput={
                   'ReadCapacityUnits':1,
                   'WriteCapacityUnits':1
               }
               
    )
print(table)
