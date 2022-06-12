import boto3

client = boto3.client('rds')

def describe_rds():
    response = client.describe_db_clusters()
    return response
