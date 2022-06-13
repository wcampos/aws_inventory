import boto3

client = boto3.client('s3')

def describe_s3():
    s3_data = client.list_buckets()
    idict={}
    ilist=[]

    for bucket in s3_data['Buckets']:
        bk_name = bucket['Name']
        bk_crtm = bucket['CreationDate']
        idict.update({
            'Name': bk_name,
            'Creation Date': bk_crtm
        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['Name'])
    return sortedlist
