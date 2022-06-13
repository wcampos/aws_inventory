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
        if 'HealthCheckPath' in target:
            tg_hcph = target['HealthCheckPath']
        else:
            tg_hcph = 'unknown'
        if 'Matcher' in target:
            tg_hcmt = target['Matcher']['HttpCode']
        else:
            tg_hcmt = 'unknown'
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

def describe_loadbalancers():
    lb_data = client.describe_load_balancers()
    idict={}
    ilist=[]

    for loadbalancer in lb_data['LoadBalancers']:
        lb_name = loadbalancer['LoadBalancerName']
        lb_scheme = loadbalancer['Scheme']
        lb_state = loadbalancer['State']['Code']
        lb_type = loadbalancer['Type']
        lb_lbtp = loadbalancer['IpAddressType']
        lb_arn = loadbalancer['LoadBalancerArn']
        lb_dns_name = loadbalancer['DNSName']
        idict.update({
            'Name': lb_name,
            'Scheme': lb_scheme,
            'State': lb_state,
            'Type': lb_type,
            'IpAddressType': lb_lbtp,
            'Arn': lb_arn,
            'DNS Name': lb_dns_name
        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['Name'])
    return sortedlist
