# cloudbox/__init__.py

import os
from flask import Flask
import boto3
from botocore.exceptions import NoCredentialsError

# Your AWS credentials and S3 settings
app.config['AWS_ACCESS_KEY_ID'] = os.getenv('AWS_ACCESS_KEY_ID')
app.config['AWS_SECRET_ACCESS_KEY'] = os.getenv('AWS_SECRET_ACCESS_KEY')
app.config['AWS_S3_BUCKET'] = os.getenv('AWS_S3_BUCKET')
app.config['AWS_REGION'] = os.getenv('AWS_REGION', 'us-east-1')
