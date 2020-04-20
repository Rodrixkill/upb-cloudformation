import boto3

PROJECT="upb-cloudformation"

client = boto3.client('cloudformation')
with open('template.yaml','r') as file:
    template = file.read()
    
response = client.create_stack(
    StackName=PROJECT,
    TemplateBody=template
)
print(response)