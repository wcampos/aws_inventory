import boto3

client = boto3.client('elbv2')

def describe_target_groups():
    target_data = client.describe_target_groups()
    idict={}
    ilist=[]
    
    for target in target_data['TargetGroups']:
        tg_name = target['TargetGroupName']
        tg_prot = target['Protocol']
        tg_port = target['Port']
        tg_vpcn = target['VpcId']
        tg_type = target['TargetType']
        tg_albn = target['LoadBalancerArns']
        tg_hcpl = target['HealthCheckProtocol']
        tg_hcpt = target['HealthCheckPort']
        tg_hcph = target['HealthCheckPath']
        tg_hcmt = target['Matcher']['HttpCode']
        idict.update({
            'Name': tg_name,
            'Protocol': tg_prot,
            'Port': tg_port,
            'Type': tg_type,
            'Vpc Id': tg_vpcn,
            'LB Arn': tg_albn,
            'Health Check Protocol': tg_hcpl,
            'Health Check Port': tg_hcpt,
            'Health Check Path': tg_hcph,
            'Health Check HTTP Matcher': tg_hcmt
        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['Name'])
    return sortedlist

#print(client.describe_load_balancers())
#print(client.describe_listeners())
