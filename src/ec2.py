import boto3

client = boto3.client('ec2')

def describe_ec2():
    ec2_data = client.describe_instances()
    idict={}
    ilist=[]

    for reservations in ec2_data['Reservations']:
        for instance in reservations['Instances']:
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        name = tag['Value']
                    elif "Env" in tag['Key']:
                        env = tag['Value']
            else:
                name = 'empty'
                env = 'empty'
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        instance_vpc = instance['VpcId']
        subnet_id = instance['SubnetId']
        for sec_group in  instance['SecurityGroups']:
            sg_id = sec_group['GroupId']
        iam_instance_profile = instance['IamInstanceProfile']['Arn']
        launch_time = instance['LaunchTime']
        private_ip = instance['PrivateIpAddress']
        state = instance['State']['Name']
        platform = instance['PlatformDetails']
        idict.update({
            'Name': name,
            'Environment': env,
            'Instance Id': instance_id,
            'Instance Type': instance_type,
            'Vpc Id': instance_vpc,
            'Subnet Id': subnet_id,
            'Security Group': sg_id,
            'IAM Instance profile': iam_instance_profile.split("/",1)[-1],
            'Lauched Time': launch_time,
            'Private IP': private_ip,
            'State': state,
            'OS Family': platform
        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['Name'])
    return sortedlist

def describe_vpcs():
    vpc_data = client.describe_vpcs()
    idict={}
    ilist=[]

    for vpc in vpc_data['Vpcs']:
        if 'Tags' in vpc:
            for tag in vpc['Tags']:
                if "Name" in tag['Key']:
                    vpc_name = tag['Value']
                elif "Env" in tag['Key']:
                    vpc_env = tag['Value']
        else:
            vpc_name = 'empty'
            vpc_env = 'empty'
        vpc_id = vpc['VpcId']
        vpc_cidr = vpc['CidrBlock']
        idict.update({
            'VPC Name': vpc_name,
            'Environment': vpc_env,
            'VPC Id': vpc_id,
            'VPC Cidr Block': vpc_cidr
        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['VPC Name'])
    return sortedlist

def describe_subnets():
    sn_data = client.describe_subnets()
    idict={}
    ilist=[]

    for subnet in sn_data['Subnets']:
        if 'Tags' in subnet:
            for tag in subnet['Tags']:
                if "Name" in tag['Key']:
                    sn_name = tag['Value']
                elif "Env" in tag['Key']:
                    sn_env = tag['Value']
        else:
            sn_name = 'empty'
            sn_env  = 'empty'
        sn_id = subnet['SubnetId']
        sn_cidr = subnet['CidrBlock']
        sn_vpc = subnet['VpcId']
        sn_az = subnet['AvailabilityZone']
        idict.update({
            'Subnet Name': sn_name,
            'Environment': sn_env,
            'Subnet Id': sn_id,
            'Subnet Cidr Block': sn_cidr,
            'VpcId': sn_vpc,
            'AvailabilityZone': sn_az
        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['Subnet Name'])
    return sortedlist

def describe_security_groups():
    sg_data = client.describe_security_groups()
    idict={}
    ilist=[]
    
    for sec_grp in sg_data['SecurityGroups']:
        sg_name = sec_grp['GroupName']
        sg_id = sec_grp['GroupId']
        sg_vpc = sec_grp['VpcId']
        sg_dpto = sec_grp['Description']
        idict.update({
            'Name': sg_name,
            'Id': sg_id,
            'VPC': sg_vpc,
            'Description': sg_dpto
        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['Name'])
    return sortedlist


def describe_security_group_rules():
    rules_data = client.describe_security_group_rules()
    idict={}
    ilist=[]

    for rule in rules_data['SecurityGroupRules']:
        rl_sgid = rule['GroupId']
        rl_grid = rule['SecurityGroupRuleId']
        if rule['IsEgress'] == True:
            rl_type = 'Egress'
        else: 
            rl_type = 'Ingress'
        rl_prot = rule['IpProtocol']
        rl_from = rule['FromPort']
        rl_to = rule['ToPort']
        if "CidrIpv4" in rule:
            rl_cidr = rule['CidrIpv4']
        elif "CidrIpv6" in rule: 
            rl_cidr = rule['CidrIpv6']
        else: 
            rl_cidr = rule['ReferencedGroupInfo']['GroupId']
        if "Description" in rule:
            rl_dpto = rule['Description']
        else:
            rl_dpto = 'No Description'
        idict.update({
            'Group Id': rl_sgid,
            'Rule Id': rl_grid,
            'Type': rl_type,
            'Protocol': rl_prot,
            'From Port': rl_from,
            'To Port': rl_to,
            'Cidr': rl_cidr,
            'Description': rl_dpto
        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['Group Id'])
    return sortedlist
