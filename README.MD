# aws_inventory

This is a WIP for a tool that helps pulling some useful data from AWS using python boto3

## Observations
- Tool uses default aws configure profile

## Current State:
Pulls basic data for the following services:
- ec2
- vpc
- subnets
- security groups
- security group rules
- target groups
- loadbalancers
- s3
- dynamodb
- rds
- lambda

The solution runs using Flask

## How to use:

Pre-requirements
```bash
pip install -r requirements.txt
```

Run:
```bash
python app.py
```


