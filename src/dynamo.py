import boto3

client = boto3.client('dynamodb')

def describe_dynamodb():
    dyn_data = client.list_tables()
    idict={}
    ilist=[]

    for dynamo in dyn_data['TableNames']:
        dy_name = dynamo
        idict.update({
            'Name': dy_name
        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['Name'])
    return sortedlist
