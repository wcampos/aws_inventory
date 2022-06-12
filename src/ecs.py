import boto3

client = boto3.client('ecs')

def describe_ecs():
    response = client.describe_cluster()
    return response
