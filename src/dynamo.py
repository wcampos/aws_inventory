import boto3

client = boto3.client('dynamodb')

def describe_dynamodb():
    response = client.list_tables()
    return response