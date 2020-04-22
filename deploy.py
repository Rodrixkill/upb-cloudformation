#!/usr/bin/python3
import getopt, sys

argument_list = sys.argv[1:]
short_options = "cduw"
long_options = ["create", "delete", "update", "website"]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
    command = arguments[0][0]
except getopt.error as err:
    print (str(err))
    sys.exit(2)

import boto3
PROJECT = "aws-cloudformation"
BUCKET_NAME = f"{PROJECT}cloudformation"
cf = boto3.client('cloudformation')
template=""
with open('template.yaml', 'r') as file:
    template = file.read()
   
if command in ("--create","-c"):
    response = cf.create_stack(
        Parameters=[
            {
                'ParameterKey': 'BucketName',
                'ParameterValue': BUCKET_NAME
            },
        ],
        StackName = PROJECT,
        TemplateBody = template
    )
 
    print(response)
elif command in ("--update", "-u"):
    response = cf.update_stack(
        StackName = PROJECT,
        TemplateBody = template
    )
    print(response)
elif command in ("--delete", "-d"):
    response = cf.delete_stack(
        StackName = PROJECT
    )
    print(response)