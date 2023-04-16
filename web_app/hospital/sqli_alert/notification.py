import boto3


def notification(query):
    sns = boto3.client('sns',
                       region_name='eu-west-2',
                       aws_access_key_id='',        # insert personal AWS access key id
                       aws_secret_access_key='')    # insert personal AWS secret access key

    message = f'Security Alert: Detected and blocked SQL injection attack with the following query: {query}.'
    
    response = sns.publish(
        TopicArn='arn:aws:sns:eu-west-2:207432807033:security',
        Message=message,
    )
    HTTPStatusCode = response['ResponseMetadata']['HTTPStatusCode']
    return HTTPStatusCode