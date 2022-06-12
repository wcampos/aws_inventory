import boto3

client = boto3.client('s3')

def describe_s3():
    response = client.list_buckets()
    return response
