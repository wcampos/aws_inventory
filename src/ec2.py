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
                        iName = tag['Value']
                    elif "Env" in tag['Key']:
                        iEnvironment = tag['Value']
            else:
                iName = 'empty'
                iEnvironment = 'empty'
        iInstanceID = instance['InstanceId']            
        iInstanceType = instance['InstanceType']
        iInstanceVPC = instance['VpcId']
        iSubnetID = instance['SubnetId']
        for sg in  instance['SecurityGroups']:
            iSecGroup = sg['GroupId']
        iIAMProfile = instance['IamInstanceProfile']['Arn']
        iLaunchTime = instance['LaunchTime']
        iPrivateIP = instance['PrivateIpAddress']
        iState = instance['State']['Name']
        iPlatform = instance['PlatformDetails']
        idict.update({
            'Name': iName,
            'Environment': iEnvironment,
            'Instance Id': iInstanceID,
            'Instance Type': iInstanceType,
            'Vpc Id': iInstanceVPC,
            'Subnet Id': iSubnetID,
            'Security Group': iSecGroup,
            'IAM Instance profile': iIAMProfile.split("/",1)[-1],
            'Lauched Time': iLaunchTime,
            'Private IP': iPrivateIP,
            'State': iState,
            'OS Family': iPlatform
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
                    iVpcName = tag['Value']
                elif "Env" in tag['Key']:
                    iVpcEnv = tag['Value']
        else:
            iVpcName = 'empty'
            iVpcEnv = 'empty'
        iVpcId = vpc['VpcId']                
        iVpcCidr = vpc['CidrBlock']
        idict.update({
            'VPC Name': iVpcName,
            'Environment': iVpcEnv,
            'VPC Id': iVpcId,
            'VPC Cidr Block': iVpcCidr
        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['VPC Name'])
    return sortedlist



def describe_subnets():
    sn_data = client.describe_subnets()
    idict={}
    ilist=[]

    for sn in sn_data['Subnets']:
        if 'Tags' in sn:
            for tag in sn['Tags']:
                if "Name" in tag['Key']: 
                    iSnName = tag['Value']
                elif "Env" in tag['Key']:
                    iSnEnv = tag['Value']
        else:
            iSnName = 'empty'
            iSnEnv  = 'empty' 
        iSnId = sn['SubnetId']                
        iSnCidr = sn['CidrBlock']
        iSnAvZn = sn['AvailabilityZone']
        iSnVpcId = sn['VpcId']
        idict.update({
            'Subnet Name': iSnName,
            'Environment': iSnEnv,
            'Subnet Id': iSnId,
            'Subnet Cidr Block': iSnCidr,
            'AvailabilityZone': iSnAvZn,
            'VpcId': iSnVpcId

        })
        ilist.append(idict.copy())
    sortedlist = sorted(ilist, key=lambda i: i['Subnet Name'])
    return sortedlist
