import boto3

client = boto3.client('lambda')

def describe_lambda():
    response = client.list_functions()
    return response