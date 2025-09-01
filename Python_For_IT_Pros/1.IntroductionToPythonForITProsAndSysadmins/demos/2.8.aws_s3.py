import boto3    # https://pypi.org/project/boto3/

aws_access_key = ""
aws_secret_key = ""
aws_region = "eu-west-1"

s3_client = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name= aws_region
)