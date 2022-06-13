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

## How to use:
Run:
```bash
python src/app.py
```


