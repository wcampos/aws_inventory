import boto3

def describe_rds():
    client = boto3.client('rds')
    response = client.describe_db_clusters()
    return response
