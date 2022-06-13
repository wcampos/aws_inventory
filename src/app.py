import tabulate
import ec2
import alb
import s3
import dynamo
import rds
import aws_lambda

def tabulate_instances_list(dataset):
    header = dataset[0].keys()
    rows =  [x.values() for x in dataset]
    tabulated_table = tabulate.tabulate(rows, header)
    print(tabulated_table)

def print_tb(data):
    print(tabulate_instances_list(data))

ec2_data = ec2.describe_ec2()
vpc_data = ec2.describe_vpcs()
sn_data = ec2.describe_subnets()
sg_data = ec2.describe_security_groups()
sgr_data = ec2.describe_security_group_rules()
tg_data = alb.describe_target_groups()
lb_data = alb.describe_loadbalancers()
s3_data = s3.describe_s3()
dy_data = dynamo.describe_dynamodb()
rds_data = rds.describe_rds()
lmd_data = aws_lambda.describe_lambda()

print_tb(ec2_data)
print_tb(vpc_data)
print_tb(sn_data)
print_tb(sg_data)
print_tb(sgr_data)
print_tb(tg_data)
print_tb(lb_data)
print_tb(s3_data)
print_tb(dy_data)
print_tb(rds_data)
print_tb(lmd_data)
