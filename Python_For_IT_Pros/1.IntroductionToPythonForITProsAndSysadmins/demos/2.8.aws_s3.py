import boto3    # https://pypi.org/project/boto3/

aws_access_key = ""
aws_secret_key = ""
aws_region = "eu-west-1"

bucket_name = "super_unique_bucket_12345"


s3_client = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name= aws_region 
)


def get_location_constraint(region_name):
    if region_name == "us-west-1":
        return ""
    else:
        return region_name
    

def create_s3_bucket(bucket_name):
    response = s3_client.create_bucket(Bucket=bucket_name)
    print(f"S3 Bucket '{bucket_name}' created successfully")


