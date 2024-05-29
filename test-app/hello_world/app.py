import json


def lambda_handler():
    return {
        "statusCode": 200,
        "body": json.dumps({
            "name": "Edwin Yaret Barragan Valdovinos CR7-FLUTTER",
            "grade": "9",
            "group": "C"
        }),
    }
