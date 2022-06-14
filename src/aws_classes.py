class alb:
    def describe_target_groups(client):
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

    def describe_loadbalancers(client):
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

class dynamodb:
    def describe_dynamodb(client):
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

class ec2:
    def describe_ec2(client):
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

    def describe_vpcs(client):
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

    def describe_subnets(client):
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

    def describe_security_groups(client):
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

    def describe_security_group_rules(client):
        rules_data = client.describe_security_group_rules()
        idict={}
        ilist=[]
        for rule in rules_data['SecurityGroupRules']:
            rl_sgid = rule['GroupId']
            rl_grid = rule['SecurityGroupRuleId']
            if rule['IsEgress'] == 'True':
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

class aws_lambda:
    def describe_lambda(client):
        ld_data = client.list_functions()
        idict={}
        ilist=[]
        for ld_func in ld_data['Functions']:
            ld_name = ld_func['FunctionName']
            ld_rntm = ld_func['Runtime']
            ld_hdlr = ld_func['Handler']
            ld_mmsz = ld_func['MemorySize']
            ld_strg = ld_func['EphemeralStorage']['Size']
            ld_pktp = ld_func['PackageType']
            ld_mftm = ld_func['LastModified']
            idict.update({
                'Name': ld_name,
                'Runtime': ld_rntm,
                'Handler': ld_hdlr,
                'Memory': ld_mmsz,
                'Storage Size': ld_strg,
                'Package Type': ld_pktp,
                'Last Modified': ld_mftm
            })
            ilist.append(idict.copy())
        sortedlist = sorted(ilist, key=lambda i: i['Name'])
        return sortedlist

class rds:
    def describe_rds(client):
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

class s3:
    def describe_s3(client):
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
