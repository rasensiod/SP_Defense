import boto3
import json


def covert_label(label):
    if label == 1:
        return "TFTP"
    elif label == 2:
        return "MSSQL"
    elif label == 3:
        return "NetBIOS"
    elif label == 4:
        return "UDP"
    elif label == 5:
        return "Syn"
    elif label == 6:
        return "DrDoS_SNMP"
    elif label == 7:
        return "DrDoS_DNS"
    elif label == 8:
        return "LDAP"
    elif label == 8:
        return "DrDoS_SSDP"
    elif label == 10:
        return "DrDoS_NTP"
    elif label == 11:
        return "UDPLag"
    elif label == 12:
        return "Portmap"
    elif label == 13:
        return "WebDDoS"
    else:
        return "BENIGN"

def notification(ddos_type):
    sns = boto3.client('sns',
                       region_name='eu-west-2',
                       aws_access_key_id='',
                       aws_secret_access_key='')

    message = f'Security Alerts: Detecting a new {ddos_type} attack. You should isolate the device or perform a reset or contact the manufactur at (help@manufacture.com)'
    response = sns.publish(
        TopicArn='arn:aws:sns:eu-west-2:207432807033:security',
        Message=message,
    )
    HTTPStatusCode = response['ResponseMetadata']['HTTPStatusCode']
    return HTTPStatusCode




