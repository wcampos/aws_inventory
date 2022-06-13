import boto3

client = boto3.client('rds')

def describe_rds():
    rds_data = client.describe_db_instances()
    idict={}
    ilist=[]

    for rds_db in rds_data['DBInstances']:
        rds_name = rds_db['DBInstanceIdentifier']
        rds_engn = rds_db['Engine']
        rds_envs = rds_db['EngineVersion']
        rds_mazs = rds_db['MultiAZ']
        rds_inst = rds_db['DBInstanceClass']
        rds_cttm = rds_db['InstanceCreateTime']
        idict.update({
            'Name': rds_name,
            'Engine': rds_engn,
            'Version': rds_envs,
            'MultiAz': rds_mazs,
            'Instance Type': rds_inst,
            'Creation Time': rds_cttm
        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['Name'])
    return sortedlist
