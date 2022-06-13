import tabulate
import ec2
import alb

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

print_tb(ec2_data)
print_tb(vpc_data)
print_tb(sn_data)
print_tb(sg_data)
print_tb(sgr_data)
print_tb(tg_data)
