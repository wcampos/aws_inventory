from flask import Flask
from flask import render_template
from src import aws_classes as awsc

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html.j2")


@app.route("/alb")
def alb():
    albx = awsc.Alb()
    tg_results = albx.describe_target_groups()
    lb_results = albx.describe_loadbalancers()
    return render_template("alb.html.j2", tg_results=tg_results, lb_results=lb_results)


@app.route("/dynamodb")
def dynamodb():
    dynx = awsc.DynamoDB()
    dyn_results = dynx.describe_dynamodb()
    return render_template("dynamodb.html.j2", dyn_results=dyn_results)


@app.route("/ec2")
def ec2():
    ec2x = awsc.Ec2()
    ec2_results = ec2x.describe_ec2()
    return render_template("ec2.html.j2", ec2_results=ec2_results)


@app.route("/lambda")
def lambdax():
    lmbx = awsc.AwsLambda()
    lmb_results = lmbx.describe_lambda()
    return render_template("lambda.html.j2", lmb_results=lmb_results)


@app.route("/networks")
def networking():
    ec2x = awsc.Ec2()
    vpc_results = ec2x.describe_vpcs()
    subnet_results = ec2x.describe_subnets()
    return render_template("networks.html.j2", vpc_results=vpc_results, subnet_results=subnet_results)


@app.route("/rds")
def rds():
    rdsx = awsc.Rds()
    rds_results = rdsx.describe_rds()
    return render_template("rds.html.j2", rds_results=rds_results)


@app.route("/s3")
def s3():
    s3x = awsc.S3()
    s3_results = s3x.describe_s3()
    return render_template("s3.html.j2", s3_results=s3_results)


@app.route("/sgs")
def sgs():
    ec2x = awsc.Ec2()
    sgs_results = ec2x.describe_security_groups()
    sgr_results = ec2x.describe_security_group_rules()
    return render_template("sgs.html.j2", sgs_results=sgs_results, sgr_results=sgr_results)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
