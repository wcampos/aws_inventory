import boto3

client = boto3.client('eks')

def describe_eks():
    response = client.list_clusters()
    return response
