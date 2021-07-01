"""[summary]
"""
from pprint import pprint
from decimal import Decimal
import traceback
from botocore.exceptions import ClientError
import boto3

TABLE_NAME = 'Movie12'
DYNNAMO_DB = boto3.resource(
    'dynamodb', endpoint_url="http://localhost:8000", region_name='eu-west-1')


def create_movie():
    """[summary]

    Args:
        TABLE_NAME ([type]): [description]

    Returns:
        [type]: [description]
    """
    try:
        table = DYNNAMO_DB.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {
                    'AttributeName': 'year',
                    'KeyType': 'HASH'    # Partition key
                },
                {
                    'AttributeName': 'title',
                    'KeyType': 'RANGE'      # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'year',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'title',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
    except Exception as err:
        print(err)

    return table


def add_movie(title, year, plot, rating):
    """[summary]

    Args:
        title ([type]): [description]
        year ([type]): [description]
        plot ([type]): [description]
        rating ([type]): [description]
        TABLE_NAME ([type]): [description]

    Returns:
        [type]: [description]
    """
    table = DYNNAMO_DB.Table(TABLE_NAME)
    response = table.put_item(
        Item={
            'year': year,
            'title': title,
            'info': {
                'plot': plot,
                'rating': rating
            }
        }
    )
    return response


def get_movie(title, year):
    """[summary]

    Args:
        title ([type]): [description]
        year ([type]): [description]
        TABLE_NAME ([type]): [description]

    Returns:
        [type]: [description]
    """
    table = DYNNAMO_DB.Table(TABLE_NAME)

    try:
        response = table.get_item(
            Key={
                'year': year,
                'title': title
            })
    except ClientError as err:
        print(err.response['Error']['Message'])
    else:
        return response['Item']


def update_movie(title, year):
    """[summary]

    Args:
        title ([type]): [description]
        year ([type]): [description]
        TABLE_NAME ([type]): [description]

    Returns:
        [type]: [description]
    """
    table = DYNNAMO_DB.Table(TABLE_NAME)

    try:
        response = table.update_item(
            Key={
                'year': year,
                'title': title
            },
            UpdateExpression="set info.rating= :r",
            ExpressionAttributeValues={
                ':r': Decimal(1)
            },
            ReturnValues="UPDATED_NEW"
        )
    except Exception:
        print(traceback.format_exc())
    else:
        return response


if __name__ == "__main__":
    out = create_movie()
    print(out)

    movie_resp = add_movie("The Big New Movie",
                           2015, "Nothing happens at all.", 0)
    print("Put movie succeeded:")
    pprint(movie_resp)

    movie = get_movie("The Big New Movie", 2015)
    if movie:
        print("Get movie succeeded:")
        pprint(movie)

    update = update_movie("The Big New Movie", 2015)
    if update:
        pprint(update)

    movie = get_movie("The Big New Movie", 2015)
    if movie:
        print("Get movie succeeded:")
        pprint(movie)
