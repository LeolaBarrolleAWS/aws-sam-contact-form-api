import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    body = json.loads(event['body'])
    table.put_item(Item={
        'email': body['email'],
        'name': body['name'],
        'message': body['message']
    })
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Form submitted successfully!"})
    }
