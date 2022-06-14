import tabulate
import aws_classes as aws
import boto3

"""
Clients
"""
alb_client = boto3.client('elbv2')
dyn_client = boto3.client('dynamodb')
ec2_client = boto3.client('ec2')
lmd_client = boto3.client('lambda')
rds_client = boto3.client('rds')
s3b_client = boto3.client('s3')

"""
Data
"""
ec2_data = aws.ec2Class.describe_ec2(ec2_client)
vpc_data = aws.ec2Class.describe_vpcs(ec2_client)
sn_data = aws.ec2Class.describe_subnets(ec2_client)
sg_data = aws.ec2Class.describe_security_groups(ec2_client)
sgr_data = aws.ec2Class.describe_security_group_rules(ec2_client)
tg_data = aws.albClass.describe_target_groups(alb_client)
lb_data = aws.albClass.describe_loadbalancers(alb_client)
s3_data = aws.s3Class.describe_s3(s3b_client)
dy_data = aws.dynamodbClass.describe_dynamodb(dyn_client)
rds_data = aws.rdsClass.describe_rds(rds_client)
lmd_data = aws.awsLambdaClass.describe_lambda(lmd_client)


def tabulate_instances_list(dataset):
    header = dataset[0].keys()
    rows =  [x.values() for x in dataset]
    tabulated_table = tabulate.tabulate(rows, header)
    print(tabulated_table)

def print_tb(data):
    print(tabulate_instances_list(data))



print('EC2')
print_tb(ec2_data)
print()
print('VPC')
print_tb(vpc_data)
print()
print('Subnets')
print_tb(sn_data)
print()
print('Security Groups')
print_tb(sg_data)
print()
print('Security Group Rules')
print_tb(sgr_data)
print()
print('Target Groups')
print_tb(tg_data)
print()
print('Loadbalancers')
print_tb(lb_data)
print()
print('S3')
print_tb(s3_data)
print()
print('DynamoDB')
print_tb(dy_data)
print()
print('RDS')
print_tb(rds_data)
print()
print('Lambda')
print_tb(lmd_data)
