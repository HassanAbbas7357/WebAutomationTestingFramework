import requests
import json
import datetime
from random import randint


def LoginGetToken():
    url = "http://52.70.226.96:86/api/login"

    payload = json.dumps({
        "email_address": "Hassan.abbas@cloudprimero.com",
        "password": "PowerPoint@123"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['data']['token']


def populate_Car():
    url = "http://52.70.226.96:86/api/transport/store"

    payload = json.dumps({
        "car_name": "doloribus",
        "capacity": 10,
        "apk_data": "2021-11-09",
        "active_since": "2021-11-09",
        "car_type": "car",
        "lease_type": "long",
        "lease_partner": "veniam",
        "lease_end_date": "2023-11-09",
        "charges": {
            "lease_cost": 13,
            "fuel_cost": 17,
            "other_cost": 16,
            "costs_per_month": 11,
            "tax_value": 13
        },
        "license_plate": str(datetime.datetime.now()),
        "remarks": {
            "date": "2023-11-09",
            "status": "to-do",
            "remark": "eveniet"
        },
        "dynamic_fields": []
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {LoginGetToken()}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())


def populate_Bike():
    url = "http://52.70.226.96:86/api/transport/store"

    payload = json.dumps({
        "car_name": f'HONDA {randint(0, 1000)}',
        "capacity": 1,
        "apk_data": "2021-11-09",
        "active_since": "2021-11-09",
        "car_type": "bike",
        "lease_type": "long",
        "lease_partner": "some partner",
        "lease_end_date": "2023-11-09",
        "charges": {
            "lease_cost": 13,
            "fuel_cost": 17,
            "other_cost": 16,
            "costs_per_month": 11,
            "tax_value": 13
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {LoginGetToken()}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json())


populate_Car()
populate_Bike()
