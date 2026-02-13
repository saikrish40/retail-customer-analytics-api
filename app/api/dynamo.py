import os
import boto3

AWS_REGION = os.getenv("AWS_REGION", "us-east-2")
DDB_CUSTOMER_TABLE = os.getenv("DDB_CUSTOMER_TABLE", "customer_features")

def get_table():
    """
    Returns a DynamoDB Table object using credentials provided by:
    - Mounted ~/.aws (your docker-compose volume), OR
    - Environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    """
    dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
    return dynamodb.Table(DDB_CUSTOMER_TABLE)
