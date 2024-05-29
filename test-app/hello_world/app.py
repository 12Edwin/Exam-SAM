import json


def lambda_handler():
    return {
        "statusCode": 200,
        "body": json.dumps({
            "name": "Edwin Yaret Barragan Valdovinos CR7",
            "grade": "9",
            "group": "C"
        }),
    }
