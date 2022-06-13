import tabulate
from ec2 import ec2 as ec2
import alb
import s3
import dynamo
import rds
import aws_lambda
import boto3

ec2_client = boto3.client('ec2')

def tabulate_instances_list(dataset):
    header = dataset[0].keys()
    rows =  [x.values() for x in dataset]
    tabulated_table = tabulate.tabulate(rows, header)
    print(tabulated_table)

def print_tb(data):
    print(tabulate_instances_list(data))

ec2_data = ec2.describe_ec2(ec2_client)
vpc_data = ec2.describe_vpcs(ec2_client)
sn_data = ec2.describe_subnets(ec2_client)
sg_data = ec2.describe_security_groups(ec2_client)
sgr_data = ec2.describe_security_group_rules(ec2_client)
tg_data = alb.describe_target_groups()
lb_data = alb.describe_loadbalancers()
s3_data = s3.describe_s3()
dy_data = dynamo.describe_dynamodb()
rds_data = rds.describe_rds()
lmd_data = aws_lambda.describe_lambda()

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
