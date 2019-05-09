import json
import boto3
dynamodb = boto3.resource('dynamodb')

def handler(event, context):
    message = event["queryStringParameters"]["message"]

    try:
        insert_data(message)
        body = {
            "message": "Good job! Your serverless python-function executed successfully!",
            "input": event
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
    except Exception as e:
        print(e)
        body = {
            "message": "Damn something went wrong!",
            "input": event
        }
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

    return response

def insert_data(data):
    table = dynamodb.Table("jariTable")
    table.put_item(Item= {'message': data})
