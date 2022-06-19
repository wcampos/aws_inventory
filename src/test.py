import aws_classes as awsc

svc = awsc.S3()
data = svc.describe_s3()
print(data)
