import boto3

def describe_ec2():
    client = boto3.client('ec2')
    response = client.describe_instances()
    return response
