import tabulate
import ec2

def tabulate_instances_list(dataset):
    header = dataset[0].keys()
    rows =  [x.values() for x in dataset]
    tabulated_table = tabulate.tabulate(rows, header)
    print(tabulated_table)


print("---------------------")
print('EC2 Report')
print("---------------------")
print()
print('Instances')
ec2_data = ec2.describe_ec2()
print(tabulate_instances_list(ec2_data))
print()
print('VPC')
vpc_data = ec2.describe_vpcs()
print(tabulate_instances_list(vpc_data))
print()
print('Subnets')
sn_data = ec2.describe_subnets()
print(tabulate_instances_list(sn_data))